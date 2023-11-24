# Final Design Report
## Table of Contents

1. [Team Names](#team-names)
2. [Project Description](#project-description)
3. [User Stories](#user-stories)
4. [Design Diagrams](#design-diagrams)
5. [Project Tasks and Timeline](#project-tasks-and-timeline)
6. [ABET Concerns](#abet-concerns)
7. [Presentation](#presentation)
8. [Self Assessments](#self-assessments)
9. [Professional Biographies](#professional-biographies)
10. [Budget](#budget)
11. [Appendix](#appendix)

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
### TimeLine
### Effort Matrix
## ABET Concerns
uilding and deploying our vision for an AI-Powered Dungeons and Dragons project will be faced with many constraints, and the aim of this essay is to highlight all such constaints that we can imagine, and how they will come into play. From a our team discussion, we have come to a conclusion that we will face time, economic, and diversity/cultural constraints. It must also be noted that there can always be additional constraints that are unforseen or those that we may only uncover by working towards completing our project.

While time may be considered a universal constraint for any project, we believe the way it impacts our project is somewhat distinct from most. The issue is not that we do not or will not have enough time to complete the project; we have already anticipated what to do if in case we find ourselves short of time in way by dividing our project into two potential deliverables. We are constrained by time in the sense that we are working with technology that is seemingly on the "bleeding edge" and how we are able to fulfill our project depends greatly on what is available at that given time. Specifically, new AI models are released everyday, so our choice for what to pick may very well depend on what is available at the time we need to look for AI models for a specific use case. As they develop, so will our project, and as they development lags, our project will be limited as well.

Economic constraints will also play a role in influencing the choices we make for our project. Specifically, if we were to train our own AI models, then we would require computers with vast processing capabilities, and this would come at a "cost". As we are not able to afford such a cost, these economic constraints have compelled us to find other means of pursuing our idea. This means it is in our interest to repurpose pre-existing models to suit our needs. As of now, we don't have any funding, and we find it somewhat difficult to procure any funds for this semester. However, we are optimistic that we can get some funds in the Spring semester. We have eyed on the Innovation Challenge as a means for receiving funds, for example.

I argue that our project also faces diversity/cultural constraints because we feel that our game will still be heavily limited by aspects of the datasets in the AI models we employ. For example, we will probably only be able to offer our video game in the English language because there is some intricate play between the LLM and any image model we use, and we envision that we will probably only be able to engineer this in the english language because of our current understanding of the problem, knowledge of languages, and time. Moreover, the dataset can always be biased towards certain cultures over others. This means that our image models will generate biased imagery, and our LLM will respond is ways that can be considered culturally insenstive or ignorant. Since we previously established that training our own model is unlikely, these are some biases that we will have to live with.

It is important to note that it is not guaranteed nor certain that these are the constraints we will face. It is always likely that there are more of fewer, or misunderstood constraints. However, in any case, we do not want to label these constraints as limiting factors, but as challenges to work around. Our biggest obstacle of course, is picking up the right momentum to complete our project on time as we want it.

## Presentation
**Click to watch**
[Slides found here](https://mailuc-my.sharepoint.com/:p:/g/personal/weesesr_mail_uc_edu/EeqbQoT1fM1HujAF9S9ZvLgBVIXqP7yKphDvM2um7GsZSA?e=cjPz3g)

[![YouTube Video](https://img.youtube.com/vi/KZptVl2xiI8/0.jpg)](https://www.youtube.com/watch?v=KZptVl2xiI8)

## Self Assessments
### Prateek Kharangate
My senior design project revolves around developing a Dungeons and Dragons video game or tools that could be used to make such a game (depending on time constraints) using generative AI. This project aims to empower an AI dungeon master to create unique worlds, characters, and storylines. It's a fusion of my interest in video games, artificial intelligence, and being at the bleeding-edge of technology. I'm undertaking this project in collaboration with Sam Weese, and together, we’re hopeful that our project will come to fruition.

Throughout my college life, I've been studious, although I never fully grasped the true value of subjects I was cramming for until a little over a year ago. It was then that I had an epiphany about its immense value. Since that moment, I've been relentlessly pursuing my passion for learning. This senior design project is a culmination of that journey, providing me with a golden opportunity to gain hands-on experience in a field I'm deeply passionate about. It's a chance to bridge the gap between theory and practice, allowing me to apply the knowledge I've acquired in a real-world context, and I couldn't be more enthusiastic about the prospects it holds.  While I believe that the Software Engineering course is the precursor to Senior Design (pardon me for not being able to recollect exact course numbers), I can’t say there is any one course or a couple of courses that have prepared me for this moment, but I would like to thank some of the professors I had the privilege of studying under, such as Dr. William Hawkins, Dr. John D. Gallagher, and Dr. Charles Zimmer, under whom I learned Programming Languages, Operating Systems, and Algorithms respectively.

My co-op experiences been diverse, spanning various industries and roles. I've assumed the role of a software engineer at a startup by the name of Payload, delved into web development with a logistics company called TCP, and engaged in research at the University of Cincinnati. While it's true that not all of the technical skills I've honed in these roles may be directly transferable to my senior design project, I firmly believe that the invaluable soft skills I've cultivated will undoubtedly prove instrumental. These experiences have endowed me with a robust work ethic, sharpened my decision-making abilities, and enhanced my communication skills. These soft skills, acquired through the diverse challenges of my co-op journey, will undoubtedly play a pivotal role in the success of our senior design project.

I am motivated about this project for a multitude of compelling reasons. Firstly, my confidence in my chosen partner, Sam Weese, for this endeavor is unwavering. I believe in his motivation and drive, and together, I believe we can bring this ambitious project to fruition. After all, it was he who approached me with the idea of this project. Secondly, I find myself captivated by the recent explosion of advancements in AI development, and I'm eager to contribute to this burgeoning field by creating a product that, although now feasible, remains unrealized. It's an opportunity to be on the cutting edge of innovation. Lastly, I am embarking on this project as a personal challenge, pushing myself beyond my perceived limits. I will need to deeply invest myself, and I'm determined to prove to myself that I have the capability and tenacity to see it through to success.

Our preliminary approach to this project involves developing the systems required for the project independently and then layering them on top of each other. My  initial focus is on world generation. Specifically, my aim is to create intricate and immersive worlds, complete with characters and items, that would seamlessly fit into the Dungeons and Dragons universe. This foundational work holds significant value not only for our current project but also as a valuable asset for any future Dungeons and Dragons-inspired video game. While I will be dedicating my efforts to developing the world generation aspect, my project partner, Sam Weese, will be taking the lead on crafting the language models crucial for the game's narrative and interactions. Our primary objective is to establish these individual systems, ensuring their seamless integration. If we successfully implement these components by the end of the Spring semester, we will consider advancing to the next stage: the actual video game development. However, if our progress halts at this juncture, we remain confident that the standalone systems we've created will already represent a substantial achievement. We hold out hope that, in the future, either ourselves or others may pick up the mantle and carry this ambitious project to its completion.

## Professional Biographies
### Prateek Kharangate
#### Contact Information

- Email: kharanpv@mail.uc.edu
- Phone Number: (513)-850-7476

#### Work Experience

##### Skills
Python, C/C++, SQL, Linux, Google Cloud, HTML/CSS, JavaScript, PHP, Java, Adobe Premiere Pro, MATLAB

- **Undergraduate Research, University of Cincinnati, August 2023 - December 2023**
  - Works on providing application-level security against side-channel attacks by developing an application in Java to detect vulnerable C code.

- **Full-Stack Developer Intern, TrueChoicePack, January 2023 - April 2023**
  - Collaborated with NetSuite ERP consultants to deploy cutting-edge systems and automation solutions through
    scripting and workflows, resulting in a substantial boost in worker productivity and efficiency.
  - Implemented comprehensive SEO strategies on the company’s websites, leading to an improvement of 40% in its
    search engine scores.
  - Designed and developed a new subsidiary website from scratch, aligning it perfectly with the objectives of the
    executive board while maximizing user experience.

- **Software Engineering Intern, Payload, June 2022 - August 2022**
  - Worked with senior developers to optimize the Extract, Transform, Load (ETL) pipeline by implementing a highly
  efficient process that selectively synchronizes modified records.
  - Leveraged Python scripts and API requests to seamlessly integrate Payload's Google Cloud database with its CRM
  platform and website, streamlining data flow across the entire system.
  - Designed and implemented a robust solution to map JP Morgan Chase's transaction error codes to our system's error
  codes, facilitating accurate transaction processing while minimizing errors and discrepancies.

#### Project Sought
My main aim is to work on a project that hasn't been implemented prior in a capstone/senior-design setting. Ideally, it would implement bleeding-edge concepts. Moreover, the project must have some practical purpose that serves to be more than a proof-of-concept (i.e., something that can at least be expanded upon to create a deliverable project in the forseeable future). For this reason, I have chosen to work on a generative AI based project that incorporates Large Language Models (LLMs) with text-to-image models to create a Dungeons and Dragons video game; something that has not fully been realized before because of the limited abilities of previous machine learning models to create endless possibilites or scenarios to enact.

### Sam Weese
#### Contact Information

- Email: weesesr@mail.uc.edu
- Phone Number: (513)-886-4073

#### Work Experience

##### Skills
Python, C/C++, Linux, Ghidra, Bash
- **Cyber Security Research Coop, Cryptic Vector August 2023 - Current**
  - Worked on SMM research for arbitrary code execution during runtime using C and UEFI
- **Undergraduate Research, University of Cincinnati, April 2023 - Current**
  - Worked on VoMo vocal cord cancer tracking app
  - Wrote live signal analysis in C++, with UI connected in Swift
  - Wrote low pass filters and audio analysis for cancer deltas in vocal output
- **Software Contractor, Beechwood Capital Management February 2023 - June 2023**
  - Developed and implemented secure digitization methods and categorization system
  - Reduced overhead by streamlining company billing process using VBA, Python
- **Software Developer Intern, 3dB Labs December 2020 - August 2022**
  - Developed and implemented  CUI data storing software using OpenSSL
  - Designed API and RSS connectors, both server and client side (using Qt and CURL)
  - Created new timekeeping systems and software to be in accordance with DCAA Yellow Book standards
  - Researched and developed embedded device to Pine phone
- **Contributor, Red Team Games, May 2020 to Current**
  - Creator and maintainer of web frontend using CSS, HTML, Django
  - Creator and arbiter of the Cards and Castles competitive scene

#### Project Sought
  I am looking for a project which both is applicable and unsolved, specifically in the area of LLMs and AI. I would like to upskill in this area, and learn how to effectively use and sub divide them. I also enjoy Dungeons and Dragons, and I realize that the difficulty of creating Dungeons and dragons with AI is extremely extremely difficult. That is why I decided I wanted to work on the part to create a Dungeons and Dragons game with LLM support (chatgpt and alike), as the problem is both largely unexplored, largely applicable, and highly interesting to my hobbies. Prateek and I are skipping ahead a year to work on this project together, as we both are interested in using AI to tackle the problem of undefined and changing rulesets for generative content for Dungeons and Dragons. To scope the project a bit tighter, we are starting by attempting to generate dynamic buildings using stable diffusion for DnD. We intend to start here, as we can begin building tools for LLMs to use in later implementations. Eventually, assuming everything goes right, we intend to have a set of tools for dungeons and dragons, and a system to build worlds which plot linear, while still being generated instead of static.

## Budget

There have not been any expenses incurred for this project.

## Appendix
