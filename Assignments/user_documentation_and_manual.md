# User Documentation and User Manual

The purpose of this document is to assist users of the application AI DnD to install, navigate, and run the application. It will also highlight some troubleshooting that a user can do and provide a guide on the intended use of this application. Note that this document will not cover the technical aspects and details concerning the functionality of the application.

## Index
1. [What is AI DnD?](#what-is-ai-dnd)
2. [User Manual](#user-manual)
   - [How to install AI DnD](#how-to-install-ai-dnd)
   - [Running AI DnD for the first time](#running-ai-dnd-for-the-first-time)
   - [Playing AI DnD](#playing-ai-dnd)
3. [User Documentation](#user-documentation)

## What is AI DnD?

AI DnD, short for Artificial Intelligence Dungeons and Dragons, is a rendition of the classic game of Dungeons and Dragons that uses machine-learning based tools such as image models and Large Language Models (LLMs) to simulate a typical game of Dungeons and Dragons. As such, this project can be considered a video game that uses AI tools.

## User Manual

The purpose of the user manual is to provide instructions on how to run this application, and how to interact with it within its intended use. As such, this section of the documents will primarily consist of how-to's for different components/aspects of the applications.

### How to install AI DnD

In order to install AI DnD, one must first clone the repository found here on GitHub. [To learn more about how to clone repositories on GitHub here](https://docs.github.com/en/repositories/creating-and-managing-repositories/cloning-a-repository). Next, you must download the `Models` folder [found on Onedrive here](https://mailuc-my.sharepoint.com/:f:/g/personal/kharanpv_mail_uc_edu/EmVYlTuEC3FAi6xZJqB-GHkB6rmDqU_5euftu4KqU--LSw?e=L2svGm).

After the necessary files and folders have been cloned and downloaded, the next step is to install the application. For this, a simple `install.bat` file can be found. Execute the `.bat` file and it will ensure that all the requirements are properly set up for the application to run. At this point, the application is ready to run.

### Running AI DnD for the first time

To run AI DnD, you must double click and execute `main.exe` found within the outermost folder of the GitHub project. This will begin the execution of the application. In order to maximize performance, please ensure that you have an active, ready to use, and configured GPU (preferably Nvidia) enabled as well.

After a while, a UI will show up with three buttons, which confirms that the application is running successfully. This is what we will refer to as the _main menu_. You will notice that there are 3 options available -- _load game_, _new game_, and _quit_. The purpose of each of these options is as follows:
1. New Game - In order to start a new game of AI DnD, click this option. Upon clicking, it will bring up a dialog box confirming that this is your choice. If you choose to continue by clicking _yes_, it will overwrite any previous game session that you had started and start a new game. If you choose _no_, it will simply take you back to the main menu.
2. Load Game - This will load the previous game session again from the previous section. For information on how to save a game, please continue reading down below for _Save Game_.
3. Quit - This simply shuts down the application.

Once you enter a game session, you will see two windows. One is a larger window to the right called the "World" window and a smaller window to the left called the "Chat" window.
- Chat Window: The chat window is where you will interact with the (LLM-powered) Dungeon Master (DM). This is also the only way you can interact with the game. At the bottom of this window you will see a text-box with a button to the right of it saying _Send_. The prompt you want to pose to the DM will be entered into this text box, that we will call the prompt box. Once you are ready with the prompt in the box, you must click _Send_ to send it through. The prompt you put in will be displayed just above the text box. The DM will process this prompt and then above the text box and below your prompt displayed. Older conversations will be pushed upwards as the conversation progresses. There is a scroll-bar to the right to access older parts of the conversation that may have left the screen.
  
- World Window: The world window reflects the consequences/output generated from the reaction of the AI models running behind the scenes in the form of images that stitch themselves together to create a cohesive world/map of the immediate surrounding. You will be able to zoom in and zoom out (using the mouse scroll wheel) and drag around the map to view all different parts of it (using the mouse left and right buttons). It only reacts after you put in a prompt, and until then, the world remains stationary. At the top-right of the world window is a button with 3 horizontal bars. This is the _pause menu_ button, which can also be reached at any time by hitting _escape_ on your keyboard.

The _pause menu_ button leads to the _pause menu_, which looks similar the _main menu_, except for a few key differences. Of the similarities, you will notice the _New Game_ and _Quit_ buttons. However, there is no _Load Game_ button. Instead, you will now see
1. Save Game - Pressing this button saves the current session in its current state, and can be accessed again at any other time using the _Load Game_ button.
2. Save and Quit Game - This combines the effects of the _Save Game_ and _Quit_ buttons in succession, i.e., it first saves the game in its current state and then quits the application.

### Playing AI DnD

To play the game, you must first either choose _New Game_ or _Load Game_ (if you are resuming another game) from the _main menu_. This will bring up the game session with the two windows - the _world window_, and the _chat window_. The game functions identically to Dungeons and Dragons. If you are unfamiliar with Dungeons and Dragons, please refer to [a guide found here](https://dnd.wizards.com/how-to-play).

#### Dungeon Master Interaction
In this game, the dungeon Master (DM) is operated by a Large Language Model (LLM), which means it is run by AI. No human input is needed to asssume the role of the DM. In the text box at the bottom of the _chat window_, you will interact with the DM, and above, in the chat history, the DM will respond. Simultaneously, AI-generated images will populate the _world window_ reflecting any changes that occured since your prompt was entered.

#### World Map Interaction
The world map of the Dungeons and Dragons game will be displayed on the _world view_ window. Aside from the controls described in the [Running AI DnD for the firt time](#running-ai-dnd-for-the-first-time) section, you will be able to drag AI-generated sprites spawned in. This feature is intended to be used if the AI-determined placement is incorrect, but it is not limited to such uses.

If the DM deems that the scene needs to change, you will receive a pop-up box confirming the change of scene. If you either requested a change of scene, or you believe the plot requires a change of scene, then click the _yes_ button found on the pop-up and a new scene will be generated. If not, then click _no_ and the scene will resume.

## User Documentation




