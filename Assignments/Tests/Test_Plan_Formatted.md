# Test Plan

## Description of Overall Test Plan

For this project, we will primarily focus on black-box style testing because of our employment of multiple systems not developed by us in our project. To be specific, we are employing mainstream AI models available publically on the internet. As such, we assume their internal working has been thoroughly tested and are sufficiently functional for our purposes. We will also not focus on performance tests as our project is a proof-of-concept and experimental in nature, and so performance optimization is not a priority. We will focus on a unit-testing scaled up to integration-testing format; testing inidividual components of our system followed by testing the interaction between these components.

## Test Case Descriptions

**ST1.1 Stable Diffusion Boot-up Test**
ST1.2 This test aims to ensure the successful initialization and running of Stable Diffusion, the generative AI model for creating image assets.
ST1.3 The test involves executing the script responsible for initializing Stable Diffusion and feeding an empty prompt to it. Verification includes checking that the associated process is active and running on the computer.
ST1.4 **Inputs:** Execution of the Stable Diffusion Boot Script with an empty prompt.
ST1.5 **Outputs:** Actively running process for Stable Diffusion present upon process look-up.
ST1.6 Functional
ST1.7 Blackbox
ST1.8 Unit Test
ST1.9 **Results:** The Stable Diffusion process is actively running after script execution.

**BI2.1 Blip Image Captioning Model Boot-up Test**
BI2.2 This test aims to ensure the successful initialization and running of the Blip Image Captioning image-to-text AI model.
BI2.3 The test involves running the image_to_text.py script with a blank-white image target. The expected output is any text description returned for the image.
BI2.4 **Inputs:** Execution of the image_to_text.py script with a blank-white image target.
BI2.5 **Outputs:** Any text description returned for the image.
BI2.6 Functional
BI2.7 Blackbox
BI2.8 Unit Test
BI2.9 **Results:** The Blip Image Captioning model successfully provides a text description for the given image.

**ML3.1 MiniLlama Boot-up Test**
ML3.2 This test aims to ensure the successful initialization and running of MiniLlama, the large language model overseeing background processes.
ML3.3 The test involves executing the MiniLlama boot script with an empty string prompt. The expected output is any prompt response by the MiniLlama model.
ML3.4 **Inputs:** Execution of the MiniLlama boot script with an empty string prompt.
ML3.5 **Outputs:** Any prompt response by the MiniLlama model.
ML3.6 Functional
ML3.7 Blackbox
ML3.8 Unit Test
ML3.9 **Results:** MiniLlama generates a prompt response after script execution.

**CG4.1 ChatGPT API Connectivity Test**
CG4.2 This test aims to ensure successful communication with the ChatGPT API, including sending requests and receiving responses.
CG4.3 The test involves sending a sample HTTP request curled to the ChatGPT API and verifying if the response has a status code of 200, indicating success.
CG4.4 **Inputs:** A sample HTTP request curled to the ChatGPT API.
CG4.5 **Outputs:** A response with HTTP status code 200.
CG4.6 Functional
CG4.7 Blackbox
CG4.8 Unit Test
CG4.9 **Results:** Successful communication with the ChatGPT API, and a response with status code 200.

**IP5.1 Image Pipeline Test**
IP5.2 This integration, functional test aims to ensure the success of the image generation pipeline, involving Stable Diffusion, Blip Image Captioning, and MiniLlama.
IP5.3 The test involves feeding a sample prompt "golden sword" to the image generation pipeline and expecting new image files added to the Assets folder.
IP5.4 **Inputs:** A sample prompt "golden sword" fed to the image generation pipeline.
IP5.5 **Outputs:** New image files added to the Assets folder.
IP5.6 Integration
IP5.7 Functional
IP5.8 **Results:** Successful generation and addition of new images to the Assets folder.

**AP6.1 Asset Placement Test**
AP6.2 This functional, unit test aims to verify the successful placement of asset images on the canvas.
AP6.3 The test involves feeding an example image into the asset placement queue, and when the MiniLlama instance for positional tracking is ready, recalling the placed image on the map.
AP6.4 **Inputs:** An example image fed into the asset placement queue.
AP6.5 **Outputs:** When the MiniLlama instance for positional tracking is ready, it successfully recalls the image placed into the queue on the map.
AP6.6 Functional
AP6.7 Unit Test
AP6.8 **Results:** Successful placement and recall of the image on the map.

**APA7.1 Asset Placement Accuracy Test**
APA7.2 This normal/functional test aims to verify the accuracy of placing an image in or near the specified location on the map.
APA7.3 The test involves queuing a test image into the asset placement pipeline with the location of "upper-right corner" and verifying the coordinates of the placed image.
APA7.4 **Inputs:** A test image fed into the asset placement queue.
APA7.5 **Outputs:** A coordinate for the placed image that has at least 75% X and 75% Y in coordinates.
APA7.6 Normal
APA7.7 Functional
APA7.8 **Results:** Successful placement with coordinates indicating at least 75% X and 75% Y.

**OM8.1 Outdoor Map Creation Test**
OM8.2 This normal/functional test aims to verify the successful creation and placement of assets in an outdoor environment.
OM8.3 The test involves feeding a specific prompt related to outdoor environments into the image generation pipeline and expecting asset images depicting outdoor scenes added to the Assets folder.
OM8.4 **Inputs:** A specific prompt related to outdoor environments.
OM8.5 **Outputs:** Asset images depicting outdoor scenes added to the Assets folder.
OM8.6 Normal
OM8.7 Functional
OM8.8 **Results:** Successful creation and placement of outdoor assets in the map.

**IC9.1 Indoor/Cave Creation Test**
IC9.2 This normal/functional test aims to verify the successful creation and placement of assets in an indoor or cave environment.
IC9.3 The test involves feeding a specific prompt related to indoor or cave environments into the image generation pipeline and expecting asset images related to indoor or cave walls added to the Assets folder.
IC9.4 **Inputs:** A specific prompt related to indoor or cave environments with enumerated entrances/exits.
IC9.5 **Outputs:** Asset images related to indoor or cave walls added to the Assets folder, proper assembly without gaps, visible entrances/exits.
IC9.6 Normal
IC9.7 Functional
IC9.8 **Results:** Successful creation and placement of indoor/cave assets in the map.

**PT10.1 Performance Test**
PT10.2 This performance test aims to evaluate the system's performance under different conditions, including load testing and response time analysis.
PT10.3 The test involves using prompts from previous tests [1-9] and an additional input to simulate high volume requests. The system's response time should remain within 30 seconds for any prompt.
PT10.4 **Inputs:** Prompts from previous tests [1-9], additional input with item fills from 0 to 100.
PT10.5 **Outputs:** System handles increased load, response times within 30 seconds.
PT10.6 Performance
PT10.7 **Results:** Successful handling of increased load, response times within acceptable limits.

## Test Case Matrix
