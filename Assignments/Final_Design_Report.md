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

## 5. Spring Final PPT Presentation

## 6. Final Expo Poster

## 7. Assessments
### 1. Initial Self-Assessments (Fall Sem)
### 2. Final Self-Assessments (Spring Sem)

## 8. Summary of Hours and Justification

## 9. Summary of Expenses

## 10. Appendix

