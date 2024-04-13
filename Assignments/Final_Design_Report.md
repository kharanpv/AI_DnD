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
![Slide4](https://github.com/kharanpv/AI_DnD/assets/126278220/c2cd183e-0263-4abd-99c6-d5c31c2748fd)
![Slide5](https://github.com/kharanpv/AI_DnD/assets/126278220/6851ad9a-b3d4-46e4-8dce-3729e000723d)
![Slide6](https://github.com/kharanpv/AI_DnD/assets/126278220/97614771-2c66-44bc-a5a5-ad7dbe6e545b)
![Slide7](https://github.com/kharanpv/AI_DnD/assets/126278220/a0b34c26-6b25-4834-96b1-2f4bbcca18ff)
![Slide8](https://github.com/kharanpv/AI_DnD/assets/126278220/28a4bc31-fcfd-4430-b71f-7e58a6add68e)
![Slide9](https://github.com/kharanpv/AI_DnD/assets/126278220/df621bd0-9bef-47d9-874d-3193ff624854)
![Slide10](https://github.com/kharanpv/AI_DnD/assets/126278220/844e8431-ea72-4d44-87ac-f0692a752523)
![Slide11](https://github.com/kharanpv/AI_DnD/assets/126278220/7eec753a-abd1-4aca-951a-4b9cf1f356ca)
![Slide12](https://github.com/kharanpv/AI_DnD/assets/126278220/3ef6a576-b80d-4dae-a046-692bbdc63880)
![Slide13](https://github.com/kharanpv/AI_DnD/assets/126278220/232d4666-1a53-47da-8ac3-ce39a962bafb)
![Slide14](https://github.com/kharanpv/AI_DnD/assets/126278220/96f49250-f411-4a9a-abe7-64a551a076b5)

## 6. Final Expo Poster
![AI_DnD_Poster](https://github.com/kharanpv/AI_DnD/assets/126278220/37b4132f-845a-4469-ad90-e30869d5d666)

## 7. Assessments
### 1. Initial Self-Assessments (Fall Sem)

#### Prateek Kharangate

My senior design project revolves around developing a Dungeons and Dragons video game or tools that could be used to make such a game (depending on time constraints) using generative AI. This project aims to empower an AI dungeon master to create unique worlds, characters, and storylines. It's a fusion of my interest in video games, artificial intelligence, and being at the bleeding-edge of technology. I'm undertaking this project in collaboration with Sam Weese, and together, we’re hopeful that our project will come to fruition.

Throughout my college life, I've been studious, although I never fully grasped the true value of subjects I was cramming for until a little over a year ago. It was then that I had an epiphany about its immense value. Since that moment, I've been relentlessly pursuing my passion for learning. This senior design project is a culmination of that journey, providing me with a golden opportunity to gain hands-on experience in a field I'm deeply passionate about. It's a chance to bridge the gap between theory and practice, allowing me to apply the knowledge I've acquired in a real-world context, and I couldn't be more enthusiastic about the prospects it holds.  While I believe that the Software Engineering course is the precursor to Senior Design (pardon me for not being able to recollect exact course numbers), I can’t say there is any one course or a couple of courses that have prepared me for this moment, but I would like to thank some of the professors I had the privilege of studying under, such as Dr. William Hawkins, Dr. John D. Gallagher, and Dr. Charles Zimmer, under whom I learned Programming Languages, Operating Systems, and Algorithms respectively.

My co-op experiences been diverse, spanning various industries and roles. I've assumed the role of a software engineer at a startup by the name of Payload, delved into web development with a logistics company called TCP, and engaged in research at the University of Cincinnati. While it's true that not all of the technical skills I've honed in these roles may be directly transferable to my senior design project, I firmly believe that the invaluable soft skills I've cultivated will undoubtedly prove instrumental. These experiences have endowed me with a robust work ethic, sharpened my decision-making abilities, and enhanced my communication skills. These soft skills, acquired through the diverse challenges of my co-op journey, will undoubtedly play a pivotal role in the success of our senior design project.

I am motivated about this project for a multitude of compelling reasons. Firstly, my confidence in my chosen partner, Sam Weese, for this endeavor is unwavering. I believe in his motivation and drive, and together, I believe we can bring this ambitious project to fruition. After all, it was he who approached me with the idea of this project. Secondly, I find myself captivated by the recent explosion of advancements in AI development, and I'm eager to contribute to this burgeoning field by creating a product that, although now feasible, remains unrealized. It's an opportunity to be on the cutting edge of innovation. Lastly, I am embarking on this project as a personal challenge, pushing myself beyond my perceived limits. I will need to deeply invest myself, and I'm determined to prove to myself that I have the capability and tenacity to see it through to success.

Our preliminary approach to this project involves developing the systems required for the project independently and then layering them on top of each other. My  initial focus is on world generation. Specifically, my aim is to create intricate and immersive worlds, complete with characters and items, that would seamlessly fit into the Dungeons and Dragons universe. This foundational work holds significant value not only for our current project but also as a valuable asset for any future Dungeons and Dragons-inspired video game. While I will be dedicating my efforts to developing the world generation aspect, my project partner, Sam Weese, will be taking the lead on crafting the language models crucial for the game's narrative and interactions. Our primary objective is to establish these individual systems, ensuring their seamless integration. If we successfully implement these components by the end of the Spring semester, we will consider advancing to the next stage: the actual video game development. However, if our progress halts at this juncture, we remain confident that the standalone systems we've created will already represent a substantial achievement. We hold out hope that, in the future, either ourselves or others may pick up the mantle and carry this ambitious project to its completion.

#### Sam Weese

The project I would like to complete is using a large language model (LLM) to
effectively generate Dungeons and Dragons content with visual components using stable
diffusion, which is informed and handled wholly by the LLM. This is quite an unbounded feat,
as the nature of LLM’s being new makes this project much much closer to research than
development. To nuance my goals a bit, I would like the final project to be able to generate
simple sprites as described by the LLM (simple meaning a common object, such as an apple or
tree, with a simple modifier, such as changing color). As this relates to what it means to me
academically, this is simply an excuse to work on a project I find interesting, and to be forced to
actually make headway on it due to the accountability provided in a teammate and class
structure. In relation to the field of academia, this project should be fairly new, as nowhere on the
open internet does anyone mention hooking up LLMs to stable diffusion for intuitive user
experience. If this project were to succeed, (which I suspect will be very hard in the short time
frame of the class), it would set the groundwork for LLM being able to display simple scenes and
ideas visually.
In regards to the usefulness of classes within UC in respect to this project, the most useful
course is Software Engineering (EECE 3093C). This course is extremely applicable, as it
covered the nature of managing a long term software project, and showed me the pitfalls of poor
project management. Another class which is applicable is Database Design and Development.
This class is an odd one in its applicability, but the general applicability comes from the mile
high view of multiple different databases. At its core, the stable diffusion LLM interface problem
is a storage problem, as being able to read from generated content and modify it. As a whole,
however, most of the classes I have taken have been largely in applicable, as the AI classes are
not covered until Senior Year, and useful LLMs (ChatGPT 3 and beyond) public accessibility is
less than a year old.
When it comes to COOPs, the only useful one will be my current one at Cryptic Vector.
While non-technical skill are always useful, especially in respect to human interaction, these I
have largely picked up in highschool, not college. The reason I find Cryptic Vector so useful is
my mentor there, Steve Kunath. Kunath has a PhD in linguistics and economics, and a Master’s
in computer science. The bulk of his work is in natural language processing, and the resources at
Stanford and connections to topics such as Resource Description Frameworks and Web Ontology
Languages have allowed myself to skip months worth of trial and error to simply know of a
resource which already exists, and is heavily applicable to my area of study. Additionally,
Cryptic Vector has a number of machine learning scientists, of whom I am in contact with and
learning on a weekly basis. While I would like to have the accessibility to Dr. Minai that other
students at UC do, I have that accessibility to AI researchers at Cryptic Vector on a daily basis, as
I am currently on COOP there.
My motivation for this project is three fold. First, I want to work with a project on a topic
I already know. I play Dungeons and Dragons on a weekly basis, and building and designing
maps is an extremely time intensive process. Being able to have an application which does this
for me would both make my life easier, and knowing where my pain points are in map design
and creation makes this project easier to jump into. Secondly, I want a project which is in a
cutting edge field, and able to eventually be converted to a product. As I have mentioned
previously, LLMs are relatively new to public consumption. This coupled with the popular
appeal of DnD (over 50k monthly subscribers to DnD Beyond, a character manager for players)
shows a fairly large market for the success of other projects. Finally, I want a project which is
extensible into another project. If we can get this project working, this opens up the possibility of
using LLMs to generate a fully unique, plot oriented world in video games. While character
dialogues in some video games are already in development (Convai), the wholistic creation of
both graphics to dialogue is unrealized at this current time.
My preliminary solution to creating sprites from LLM input is to simply have LLMs take
human input, and convert it to the commands entered in a stable diffusion model. Eventually, we
would like to include back propagation and some form of AI lens to be able to read the data back
to the LLM. This is much harder, however there are currently in development extensions and
models which accept image input to the AI. These, by themselves, are not sufficient, as
evaluating the image without context provided by the original generation creates a disconnect
between what the LLM evaluates and believes itself to generate. A solution to this is including
the prompt with the image for back propagation, and this is where the Resource Description
Framework (RDF) comes into play. The RDF allows us to carry both the image, text used to
generate the image, and the important points (such as a well in a generation of a castle, or
something similar). However, we (Prateek and myself) are starting smaller, and attempting to
build human and LLM usable tools, so that even if we do not get a solution to our satisfaction,
we can still have a human usable tool developed out of the experience.


### 2. Final Self-Assessments (Spring Sem)

#### Prateek Kharangate

**Part A**

Our project can broadly be divided into its backend and frontend. The backend is where most of the generative AI models employed operated. I was almost entirely responsible for the image generation pipeline and worked together with my project Partner, Sam, on the large language model-based dungeon master. I also had a few contributions to the frontend UI as well. I am confident that my understanding of AI and software engineering principles has improved since I undertook this project. My greatest experience working on this project stemmed from embarking on the challenge of running generative AI models on my computer natively. 

I was able to understand what different types of models exist and for what purpose, their underlying principles and the dependencies on which they operate. We did not train any models, but a lot of the requirements to run a model are very similar to training a model. I also learned how to interact with the hyperparameters for a model and understand their observed effects. This new knowledge came from my culminated effort to find the “right model” for the task as much of the quality indicators for our project depended on them. I would describe my success as being able to utilize Stable Diffusion to successfully and consistently generate the images expected of it. As for obstacles, I mainly faced issues with arriving at a coherent software architecture to build our project upon. As such, I experienced file path issues and threading issues that consumed more time than should have been required to patch.


**Part B**

We were successful in implementing a prototype version of the map-building component of our grander plan for AI Dungeons and Dragons. My main inference about group work that I learned was to pick your partner carefully. I consider myself fortunate to have Sam Weese as my project partner. While his interests and motivations are different from mine, we both maintained a high standard for responsibilities, deadlines, and willingness to learn. Furthermore, our understanding of what the project should be was very well defined and so conflicts on that did not arise down the line. 

The biggest challenges for the two us did not stem from a difference in opinion or attitude but from a difference in circumstances and resources. Our work environments for building the application differed greatly, and especially in the Fall Semester when we took Senior Design 1, our time schedules seldom aligned, if at all. I would like to believe, and I hope Sam thinks the same, that our contributions were fairly equal in magnitude with respect to each other. We had somewhat well-defined roles as to who was tasked with what, and these tasks were equally demanding. I believe we both deserve the same level of recognition for this project.

#### Sam Weese

**Part A**
For this project, I think I learned a lot. Unfortunately, a lot of it was learning how to do something the wrong way in software design than learning to do it the correct way. The project accomplished what we wanted to, which was to show a proof of concept MVP which allows us to build dungeons and dragons maps from plain text alone.  Before we go over my accomplishments, I should discuss the tech stack which we used. We use a python UI which displays images in a custom graph object, along with a text input box along the side. The text input box connects to a threading/subprocess handler which is in the primary secondary configuration (better known as master/slave for a lot of coding history) which spins up a new secondary thread for an input. That thread reaches out and connects to the chat-gpt api, which is passed a custom prompt set to create an image description. That text description is then passed to the image pipeline, which is spun up as another subprocess (due to some technical advantages for parallelization), which uses a custom stable diffusion model to generate an image. The thread returns, and the image is placed on the graph according to the text description given.  

I wrote the UI, the graph object, the API handling and prompt engineering, and the threading. Prateek (my only teammate, who was great to work with) wrote the stable diffusion sub processing and the custom image generation model.  I didn't get to build upon the AI correctness training I hoped to build upon, but instead mostly worked on threading and UI. I was rather disappointed with this, as the product we built was for the expo, not for what I wanted to do. I plan on continuing this project over the summer, but removing a lot of the work we did as it was made to produce fast, viewable work, not good solid behind the scenes analysis.  

**Part B**

I think the competency wise, nothing was new, but lessons I should have learned previously were relearned. I spent a large amount of time rewriting and having to bug fix the threading. I felt comfortable with threads prior to this project, and I still feel comfortable with them, but to a lesser degree when it interacts with code other people have written. I think I have learned to be more careful with how I write code which interacts with others. The threading issue was due to both Prateek and I working on the threading initially, and misconnecting the functions we both wrote. 

 I would say the largest lesson I learned about teamwork was to have good communication between team mates. I probably spent upwards of 20 hours debugging the threading, and it could have simply been avoided if only one of us had written the threading initially. I think the biggest non-technical realization I had related to the project was that the entire team can burn out. After midterms, neither Prateek nor myself had any motivation or desire to write code, as we both had simply had enough of school work at that time due to doing both midterms and senior design. It would have been better to simply pause and step back and put the project on hold, instead of pushing hard. I think Prateek should be recognized, both he and I contributed the same amount of work.
## 8. Summary of Hours and Justification

## 9. Summary of Expenses

## 10. Appendix

