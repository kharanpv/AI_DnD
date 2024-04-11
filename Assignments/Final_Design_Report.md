# Final Design Report
## Ai-DnD
**Team Name: The Jaran Project**

Team Members: 
1. Prateek Kharangate
2. Sam Weese

## Table of Contents

| No.| Title|
|---|-------------|
| 1 | Project Description |
| 2 | User Interface Specification |
| 3 | Test Plan and Results |
| 4 | User Manual |
| 5 | Spring Final PPT Presentation |
| 6 | Final Expo Poster |
| 7 | Assessments<br> 1. Initial Self-Assessments (Fall Sem<br> 2. Final Self-Assessments (Spring Sem) |
| 8 | Summary of Hours and Justification |
| 9 | Summary of Expenses |
| 10 | Appendix |

## 1. Project Description

AI-DnD is a prototype map-generation tool for the tabletop game Dungeons and Dragons with an LLM-based Dungeon Master (DM) and a text-to-image model for asset generation. The DM, based upon Chat GPT 3.5 Turbo API, generates descriptions to user requests of map objects such as name, paragraph description, size, and location. The Stable Diffusion image model using the Pixel-art-xl LORA is used to generate assets and sprites based the DM's descriptions.

## 2. User Interface Specification

The user interface (UI) was developed using the PyQt5 Python library. The UI consists of two sections:

1. Map Canvas
2. Chat Section
   * Chat History
   * Prompt Box
   
![image](https://github.com/kharanpv/AI_DnD/assets/126278220/004b67c7-3ea0-4ac8-a8b9-b5a4881fa0a9)

### Map Canvas

### Chat Section

#### Chat History

#### Prompt Box

## 3. Test Plan and Results

1. ChatGPT API Connection Test

   **Description:** This test checks whether the Chat GPT API is set up correctly with a working API key and is being queried to properly. To test this, a prompt is made through the prompt box, and it is determined if the response received is "RESPONSE ERROR" or not. 
   
    **Input:** Any prompt in the prompt box
   
    **Result:** PASS - No "RESPONSE ERROR" message received.
   
2. Stable Diffusion Load Test
   
    **Description:** This test verifies that Stable Diffusion is present and running. For this test, the `workflow_api.py` is executed with an empty `request.json` file. If the program generates an image in the `output` folder, the test passes.
   
    **Input:** The `workflow_api.py` script is executed in terminal with an empty `request.json` file present in the same directory.
   
    **Result:** PASS - Stable Diffusion is able to generate an image to the `output` folder. 

3. Image Pipeline Test

   **Description:** This test executes the entire image pipeline with a prompt to determine whether it indicates that it successfully generated an image and also places the image in the right folder. To pass this test, the message that the image was successfully moved must be seen and a new image must appear in the `UI_EndUser/test_images` folder.
   
    **Input:** A prompt passed directly to `create_assets.py`
   
    **Result:** PASS - The "image moved to `UI_EndUser/test_images`" message was seen and it appeared successfully in `UI_EndUser/test_images`

4. Blip Image Captioning Load Test

   **Description:** This test verifies whether the Blip Image Captioning Image-to-Text model is working correctly. The example `tree.png` image is passed via argument to `image_to_text.py` script and if the program successfully prints a text reponse to the terminal, it is considered to have passed.
   
    **Input:** `tree.png` passed as argument to `image_to_text.py`.
   
    **Result:** PASS - A reverse prompt is successfully generated for `tree.png`

5. Image Load Test

   **Description:** This test verifies whether images can successfully be loaded from the UI's menu onto the map canvas. This involves interacting with File > Load Image and selecting an image from the file dialog, which is then expected to be visible on the screen.
   
    **Input:** Clicking File > Load Image and choosing `tree.png` from a discrete folder.
   
    **Result:** PASS - `tree.png` is visible on the map canvas.

6. Image Deletion Test

   **Description:** This test verifies that the image deletion option removes an image from the map canvas. For this, an image is left-clicked and the "Delete" button is pressed on the "Delete" tab.
   
    **Input:** A loaded map canvas with only the `tree.png` image.
   
    **Result:** PASS - `tree.png` image is no longer visible on the map canvas.

7. Image Displacement Test

    **Description:** The X, Y, and Z co-ordinates of an image on Canvas are changed in the MOVE tab to a random set of co-ordinates. If the image successfully moves to its new location on Canvas, then the test passes.
   
    **Input:** The X, Y, and Z co-ordinates of `tree.png` are changed to random integers within the bound (-1500,5500)
   
    **Result:** PASS - `tree.png` moves to the new location described by the random co-ordinates.

8. Image Rotation Test

    **Description:** A random degree of rotation between 0 and 360 is given as input in the ROTATION tab. It is expected that the image will be rotated accordingly by the right amount.
   
    **Input:** A random degree number between 0 and 360 is entered in the ROTATION tab for `tree.png`.
   
    **Result:** PASS - The `tree.png` image is rotated correctly by the right degree with respect to its current position.

9. Image Scale Test

    **Description:** A Scale factor is provided to an image in the SCALE tab. The X-axis and Y-axis length of the image should grow by that many times.
   
    **Input:** A random scale factor between 0.1 and 5.0 is entered into the SCALE tab for `tree.png`.
   
    **Result:** PASS - The `tree.png` image's X and Y axes length increases by the random scale and image size changes. 

10. Map Save Test

    **Description:** A map canvas that has been populated with some images is saved from File > Save State. This should open a file dialogbox to save a .lobj file.
    
    **Input:** Four `tree.png` instances placed randomly on the map canvas are saved through the File > Save State option with the name `tree.lobj` in `UI_EndUser/save`.
    
    **Result:** PASS - `tree.lobj` is present in `UI_EndUser/save`.

11. Savefile Load Test

    **Description:** A savefile that was previously created is loaded from the file dialogbox generated by File > Load State. The images in the savefile should be populated into the map canvas.
    
    **Input:** `tree.lobj`, a save file consisting of four `tree.png` instances with random size and co-ordinates is loaded via File > Load State.
    
    **Result:** PASS - All four instances of `tree.png` are loaded onto the canvas with their original properties from the savefile.



## 4. User Manual

The purpose of the user manual is to provide instructions on how to run this application, and how to interact with it within its intended use. As such, this section of the documents will primarily consist of how-to's for different components/aspects of the applications.

### How to install AI DnD

In order to install AI DnD, one must first clone the repository found here on GitHub. [To learn more about how to clone repositories on GitHub here](https://docs.github.com/en/repositories/creating-and-managing-repositories/cloning-a-repository). Next, you must download the `Models` folder [found on Onedrive here](https://mailuc-my.sharepoint.com/:f:/g/personal/kharanpv_mail_uc_edu/EmVYlTuEC3FAi6xZJqB-GHkB6rmDqU_5euftu4KqU--LSw?e=L2svGm).

After the necessary files and folders have been cloned and downloaded, the next step is open Terminal in the `AI_DnD/UI_EndUser`  (right-click in the folder specified and this should be one option), and then, execute the command `python main.py`.

### Running AI DnD for the first time

Once you enter a game session, you will see two windows. One is a larger window to the right called the "World" window and a smaller window to the left called the "Chat" window.
- Chat Window: The chat window is where you will interact with the (LLM-powered) Dungeon Master (DM). This is also the only way you can interact with the game. At the bottom of this window you will see another text-box. The prompt you want to pose to the DM will be entered into this text box, that we will call the prompt box. Once you are ready with the prompt in the box, you must hit _Enter_ on your keyboard to send it through. The prompt you put in will be displayed just above the text box. The DM will process this prompt and then above the text box and below your prompt displayed. Older conversations will be pushed upwards as the conversation progresses. There is a scroll-bar to the right to access older parts of the conversation that may have left the screen.
  
- World Window: The world window reflects the consequences/output generated from the reaction of the AI models running behind the scenes in the form of images that stitch themselves together to create a cohesive world/map of the immediate surrounding. You will be able to zoom in and zoom out (using the mouse scroll wheel) and drag around the map to view all different parts of it (using the mouse left and right buttons). It only reacts after you put in a prompt, and until then, the world remains stationary. At the top-left of the world window is the _options_ menu.
  
- Options: In the top-left of the screen, there exist options _File_ and _Canvas_ that have the ability to load save states or individual images, save states, clear the World Window, and list all images on the Window. The metadata for the images and the save files are of the `.lobj` format.

### Playing AI DnD

#### Dungeon Master Interaction
In this game, the dungeon Master (DM) is operated by a Large Language Model (LLM), which means it is run by AI. No human input is needed to asssume the role of the DM. In the text box at the bottom of the _chat window_, you will interact with the DM, and above, in the chat history, the DM will respond. Simultaneously, AI-generated images will populate the _world window_ reflecting any changes that occured since your prompt was entered. If you do not like the assets/sprites the DM generates or believe there is an issue with the DM's response, you can ask to create the sprites or a new response again.

#### World Map Interaction
The world map of the Dungeons and Dragons game will be displayed on the _world view_ window. Aside from the controls described in the [Running AI DnD for the first time](#running-ai-dnd-for-the-first-time) section, you will be able to move, rotate, and scale AI-generated sprites spawned in. This feature is intended to be used if the AI-determined placement is incorrect, but it is not limited to such uses.

## 5. Spring Final PPT Presentation

![Slide1](https://github.com/kharanpv/AI_DnD/assets/126278220/b68899f8-0320-4171-a589-6b6a793c8322)
![Slide2](https://github.com/kharanpv/AI_DnD/assets/126278220/75f893c1-ed72-4f19-b096-0cdfcf6b7f79)
![Slide3](https://github.com/kharanpv/AI_DnD/assets/126278220/c6c9b525-7306-487a-916f-9a319f07455a)




## 6. Final Expo Poster

## 7. Assessments
### 1. Initial Self-Assessments (Fall Sem)
### 2. Final Self-Assessments (Spring Sem)

## 8. Summary of Hours and Justification

## 9. Summary of Expenses

## 10. Appendix

