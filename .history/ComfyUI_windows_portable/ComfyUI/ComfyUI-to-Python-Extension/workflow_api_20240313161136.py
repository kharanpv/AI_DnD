import os
import random
import sys
from typing import Sequence, Mapping, Any, Union
import torch
import json
import importlib.util

def get_value_at_index(obj: Union[Sequence, Mapping], index: int) -> Any:
    """Returns the value at the given index of a sequence or mapping.

    If the object is a sequence (like list or string), returns the value at the given index.
    If the object is a mapping (like a dictionary), returns the value at the index-th key.

    Some return a dictionary, in these cases, we look for the "results" key

    Args:
        obj (Union[Sequence, Mapping]): The object to retrieve the value from.
        index (int): The index of the value to retrieve.

    Returns:
        Any: The value at the given index.

    Raises:
        IndexError: If the index is out of bounds for the object and the object is not a mapping.
    """
    try:
        return obj[index]
    except KeyError:
        return obj["result"][index]


def find_path(name: str, path: str = None) -> str:
    """
    Recursively looks at parent folders starting from the given path until it finds the given name.
    Returns the path as a Path object if found, or None otherwise.
    """
    # If no path is given, use the current working directory
    if path is None:
        path = os.getcwd()

    # Check if the current directory contains the name
    if name in os.listdir(path):
        path_name = os.path.join(path, name)
        print(f"{name} found: {path_name}")
        return path_name

    # Get the parent directory
    parent_directory = os.path.dirname(path)

    # If the parent directory is the same as the current directory, we've reached the root and stop the search
    if parent_directory == path:
        print(f"Reached root directory {path} and {name} was not found.")
        return None

    # Recursively call the function with the parent directory
    return find_path(name, parent_directory)


def add_comfyui_directory_to_sys_path() -> None:
    """
    Add 'ComfyUI' to the sys.path
    """
    comfyui_path = find_path("ComfyUI")
    if comfyui_path is not None and os.path.isdir(comfyui_path):
        sys.path.append(comfyui_path)
        print(f"'{comfyui_path}' added to sys.path")

def import_as_module(name: str, path: str) -> None:
    """
    Import the given file as a module with the given name.
    """
    spec = importlib.util.spec_from_file_location(name, path)
    module = importlib.util.module_from_spec(spec)
    spec.loader.exec_module(module)
    sys.modules[name] = module

def add_extra_model_paths() -> None:
    """
    Parse the optional extra_model_paths.yaml file and add the parsed paths to the sys.path.
    """
    # from main import load_extra_path_config
    load_extra_path_config = sys.modules['main'].load_extra_path_config

    extra_model_paths = find_path("extra_model_paths.yaml")

    if extra_model_paths is not None:
        load_extra_path_config(extra_model_paths)
    else:
        print("Could not find the extra_model_paths config file.")


add_comfyui_directory_to_sys_path()
import_as_module("main", find_path("main.py") + '\\main.py')
add_extra_model_paths()

from nodes import (
    EmptyLatentImage,
    LoraLoader,
    NODE_CLASS_MAPPINGS,
    SaveImage,
    VAEDecode,
    KSampler,
    CheckpointLoaderSimple,
    CLIPTextEncode,
)

    

def get_prompts_and_samples():
    with open("request.json", "r") as file:
        data = json.load(file)
        positive_prompt = data.get("positive_prompt")
        negative_prompt = data.get("negative_prompt")
        num_samples = data.get("num_samples", 5)

    return positive_prompt, negative_prompt, num_samples

def main() -> None:
    positive_prompt, negative_prompt, num_samples = get_prompts_and_samples()
    
    with torch.inference_mode():
        checkpointloadersimple = CheckpointLoaderSimple()
        checkpointloadersimple_4 = checkpointloadersimple.load_checkpoint(
            ckpt_name="sdXL_v10VAEFix.safetensors"
        )

        emptylatentimage = EmptyLatentImage()
        emptylatentimage_5 = emptylatentimage.generate(
            width=512, height=512, batch_size=1
        )

        loraloader = LoraLoader()
        loraloader_10 = loraloader.load_lora(
            lora_name="pixel-art-xl-v1.1.safetensors",
            strength_model=1,
            strength_clip=1,
            model=get_value_at_index(checkpointloadersimple_4, 0),
            clip=get_value_at_index(checkpointloadersimple_4, 1),
        )

        # positive_prompt = input("\nEnter the positive prompt:")
        # negative_prompt = input("Enter the negative prompt:")

        print('\nPositive prompt:', positive_prompt)
        print('\nNegative prompt:', negative_prompt) if negative_prompt is not None else print('\n')
        positive_prompt = positive_prompt
        negative_prompt = "" if negative_prompt is None else negative_prompt

        # write positive prompt to temporary file. If negative prompt exists, write that too.
        with open("temp.txt", "w") as file:
            file.write(f"{positive_prompt}")
            if negative_prompt != "":
                file.write(f"\n{negative_prompt}\n")
            else:
                file.write("\n")

        # num_samples = input("Enter the number of samples (>=1 and <=20):")
        # num_samples = 1 if num_samples == "" or int(num_samples) < 1 else 20 if int(num_samples) > 20 else int(num_samples)
        print('\nNumber of samples:', 5 if num_samples is None else num_samples)

        cliptextencode = CLIPTextEncode()
        cliptextencode_6 = cliptextencode.encode(
            text=positive_prompt + ', white background',
            clip=get_value_at_index(loraloader_10, 1),
        )

        cliptextencode_7 = cliptextencode.encode(
            text=negative_prompt,
            clip=get_value_at_index(loraloader_10, 1)
        )

        ksampler = KSampler()
        vaedecode = VAEDecode()
        saveimage = SaveImage()

        for q in range(num_samples):
            ksampler_3 = ksampler.sample(
                seed=random.randint(1, 2**64),
                steps=20,
                cfg=8,
                sampler_name="euler",
                scheduler="normal",
                denoise=1,
                model=get_value_at_index(loraloader_10, 0),
                positive=get_value_at_index(cliptextencode_6, 0),
                negative=get_value_at_index(cliptextencode_7, 0),
                latent_image=get_value_at_index(emptylatentimage_5, 0),
            )

            vaedecode_8 = vaedecode.decode(
                samples=get_value_at_index(ksampler_3, 0),
                vae=get_value_at_index(checkpointloadersimple_4, 2),
            )

            saveimage_9 = saveimage.save_images(
                filename_prefix="ComfyUI", images=get_value_at_index(vaedecode_8, 0)
            )

if __name__ == "__main__":
    main()


