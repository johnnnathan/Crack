# Reverse-Engineering Challenge Write-ups

This repository contains write-ups and solutions for various challenges from the [crackmes.one](https://crackmes.one/) and [crackmy.app](https://crackmy.app/) websites. Each folder corresponds to a specific challenge and is organized by the challenge name and its author.

## Repository Structure

- **Folder Name**: Each folder is named after the challenge and the author, e.g., `challenge_name_author` or `challenge_name` depending on if the name is unique enough.
  - **solution.txt**: This file contains a high-level overview of the steps taken to solve the challenge, explaining the thought process and techniques used.
  - **keygen.py** (if applicable): A keygen script that generates valid user/password combinations for the challenge, where feasible.
  - **decompilation.c/.cpp** (if applicable): Sometimes I write decompilations for the challenges. Don't treat them as source code, they are not since I just replicate the high-level operations.

## How to Use

To explore a solution, navigate to the corresponding folder, read the `solution.txt` file for guidance, and run `keygen.py` if you’d like to generate keys for testing. Decompilations, inside the `decompilation.c/.cpp` file, can be compiled with the compiler of your choice and run without much thought. I develop them on linux, so windows users might face issues(I try to keep them as cross-platform as I can).

## Plans 
- I will try to solve at least one difficult crackme a week and multiple easier ones, adding the write-ups to this repository. I am currently in Uni so I don't have infinite time but can usually spend an hour a day on it. 

- I have started developing a GUI app called Harpocrates, which can be found on my github profile. I will try to keep it updated and add features semi-regularly. More information can be found there.

## Contributions

Feel free to suggest improvements to existing solutions or request solutions to challenges. I usually compose the write-ups while I'm tired so if there are any mistakes in the phrasing or if you want something to be explained in more detail, let me know. 


## Notes
I am still a student of this craft and thus many of my solutions may be sub-optimal or may use bad habits. Make sure to study other people's solutions too. 
