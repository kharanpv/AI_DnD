# Final Design Report
## Table of Contents

1. [Team Names](#team-names)
2. [Project Description](#project-description)
3. [User Stories](#user-stories)
4. [Design Diagrams](#design-diagrams)
5. [Project Tasks and Timeline](#project-tasks-timeline)
6. [ABET Concerns](#abet-concerns)
7. [Presentation](#presentation)
8. [Self Assessments](#self-assessments)
9. [Professional Biographies](#professional-biographies)

## Team Names
**Team Name:** The Jaran Project

**Team Members:** 
1. Prateek Kharangate (@kharanpv)

2. Samuel Weese (@SamuelWeese)
                  
**Advisor**: Dr. Tianyu Jiang

### Project Abstract
The end-goal of this project is to have functional game of Dungeons and Dragons that operates purely based on player interactions with multiple AI systems that will be completely responsible for narration, story-building, and world generation. Since this is an ambitious project, we have divided the project into milestones, and we would be satisfied with whatever milestone we end up completing the project to, though we will ideally strive for a complete product.

The milestones are

    1. Developing the AI models necessary for world generation, asset generation, and story generation.
    2. Creating a model Dungeons and Dragons game that can be played with a human dungeon master.
    3. Creating a complete Dungeons and Dragons game that has an AI dungeon master.

## Project Description
**Project Topic Area:** Natural Language Processing & Deep Learning

This project seeks to use **Large Language Models (LLM)** to create narrative based battle maps, character sheets, and items for the table top role playing game, Dungeons and Dragons. The project will use a combination of **Static** and **Relational** memory to load details in and out of the LLM to infer important context for each task. The project also uses **Stable Diffusion** to create images which are used in the visual display of each piece of the project. The end goal is to develop these tools that a LLM can later use them to help players in automating Dungeons and Dragons world development.

## User Stories
### 1. Configuring the dungeon master's behavior

   Sara, ready for a new AI-driven D&D adventure, shapes the AI Dungeon Master's personality. She envisions a wise, enigmatic guide with a hint of whimsy, encouraging creativity and adaptability. The Dungeon master adds mystery, offering cryptic hints, fostering camaraderie, and making sessions memorable.
   
### 2. Generating characters for a new DnD game

   Carlos and friends gather for an AI-driven DnD game. Carlos sets the player count and opts for a Fantasy theme. Lacking character design skills, theyrely on the AI dungeon master. Each player submits       character stories, and the dungeon master uses these as prompts to generate stats fitting the Fantasy theme.

### 3. Generating a custom world from a custom theme

   Juan seeks a unique DnD experience, desiring a utopian French steampunk setting. The AI dungeon master assists by outlining a plot, guiding Juan's character and backstory choices, and instructing the       image generator AI to create the map and setting.

### 4. Interacting with the world

   Elena begins a new DnD game. The dungeon master describes the starting scene. Elena writes her next action, and the dungeon master responds, visually reflecting her choices in the game world.

### 5. Engaging in turn-based combat

   Alejandro's DnD party encounters a group of menacing creatures in the AI-driven DnD video game. As the party's warrior, he wishes to engage in a combat scenario. Alejandro communicates his intentions to    the AI dungeon master, describing his combat strategy and desired outcomes. The dungeon master processes his input, simulating the combat encounter, calculating dice rolls, and narrating the unfolding      battle. The image generator AI visually represents the combat, displaying character sprites, enemy creatures, and the evolving battlefield as the encounter intensifies.   

## Design Diagrams

### Level 0
![Design Diagram L0](https://github.com/kharanpv/AI_DnD/blob/main/Assignments/Assignment-10/DesignDiagram0.png)

### Level 1
![Design Diagram L1](https://github.com/kharanpv/AI_DnD/blob/main/Assignments/Assignment-10/Design_Diagram_D1.png)

### Level 2
![Design Diagram L2](https://github.com/kharanpv/AI_DnD/blob/main/Design_Diagrams/Design_Diagram_D2.png)

## Project Tasks and Timeline
### Task List
<table>
  <thead>
    <tr>
      <th>Task No.</th>
      <th>Team Member</th>
      <th>Task</th>
    </tr>
  </thead>
  <tbody>
    <tr>
      <td>1</td>
      <td rowspan="6">Prateek</td>
      <td>Develop UI for back propagation selection in stable diffusion.</td>
    </tr>
    <tr>
      <td>2</td>
      <td>Research stable diffusion models.</td>
    </tr>
    <tr>
      <td>3</td>
      <td>Research back propagation</td>
    </tr>
    <tr>
      <td>4</td>
      <td>Design back propagation UI</td>
    </tr>
    <tr>
      <td>5</td>
      <td>Research LLM to stable diffusion interfaces</td>
    </tr>
    <tr>
      <td> 6 </td>
      <td>Research map stitching methods</td>
    </tr>
    <tr>
      <td>7</td>
      <td rowspan="9">Sam</td>
      <td>Specify a proper result for map.</td>
    </tr>
    <tr>
      <td>8</td>
      <td>Investigate proper subsets for complex structures in a map.</td>
    </tr>
    <tr>
      <td>9</td>
      <td>Design back trace method for map comparison.</td>
    </tr>
    <tr>
      <td>10</td>
      <td>Research command interface LLM options.</td>
    </tr>
    <tr>
      <td>11</td>
      <td>Develop LLM command interface module.</td>
    </tr>
    <tr>
      <td>12</td>
      <td>Design map tool UI.</td>
    </tr>
    <tr>
      <td>13</td>
      <td>Develop map tool user interface.</td>
    </tr>
    <tr>
      <td>14</td>
      <td>Specify a constraint to map size.</td>
    </tr>
    <tr>
      <td>15</td>
      <td>Specify map stitching requirements.</td>
    </tr>
  </tbody>
</table>

## ABET Concerns
uilding and deploying our vision for an AI-Powered Dungeons and Dragons project will be faced with many constraints, and the aim of this essay is to highlight all such constaints that we can imagine, and how they will come into play. From a our team discussion, we have come to a conclusion that we will face time, economic, and diversity/cultural constraints. It must also be noted that there can always be additional constraints that are unforseen or those that we may only uncover by working towards completing our project.

While time may be considered a universal constraint for any project, we believe the way it impacts our project is somewhat distinct from most. The issue is not that we do not or will not have enough time to complete the project; we have already anticipated what to do if in case we find ourselves short of time in way by dividing our project into two potential deliverables. We are constrained by time in the sense that we are working with technology that is seemingly on the "bleeding edge" and how we are able to fulfill our project depends greatly on what is available at that given time. Specifically, new AI models are released everyday, so our choice for what to pick may very well depend on what is available at the time we need to look for AI models for a specific use case. As they develop, so will our project, and as they development lags, our project will be limited as well.

Economic constraints will also play a role in influencing the choices we make for our project. Specifically, if we were to train our own AI models, then we would require computers with vast processing capabilities, and this would come at a "cost". As we are not able to afford such a cost, these economic constraints have compelled us to find other means of pursuing our idea. This means it is in our interest to repurpose pre-existing models to suit our needs. As of now, we don't have any funding, and we find it somewhat difficult to procure any funds for this semester. However, we are optimistic that we can get some funds in the Spring semester. We have eyed on the Innovation Challenge as a means for receiving funds, for example.

I argue that our project also faces diversity/cultural constraints because we feel that our game will still be heavily limited by aspects of the datasets in the AI models we employ. For example, we will probably only be able to offer our video game in the English language because there is some intricate play between the LLM and any image model we use, and we envision that we will probably only be able to engineer this in the english language because of our current understanding of the problem, knowledge of languages, and time. Moreover, the dataset can always be biased towards certain cultures over others. This means that our image models will generate biased imagery, and our LLM will respond is ways that can be considered culturally insenstive or ignorant. Since we previously established that training our own model is unlikely, these are some biases that we will have to live with.

It is important to note that it is not guaranteed nor certain that these are the constraints we will face. It is always likely that there are more of fewer, or misunderstood constraints. However, in any case, we do not want to label these constraints as limiting factors, but as challenges to work around. Our biggest obstacle of course, is picking up the right momentum to complete our project on time as we want it.

## Presentation
<iframe width="560" height="315" src="https://www.youtube.com/embed/KZptVl2xiI8" frameborder="0" allowfullscreen></iframe>

## Self Assessments

## Professional Biographies
