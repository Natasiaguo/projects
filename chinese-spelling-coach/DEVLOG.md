# Development Log – Chinese Spelling Coach
## Purpose
This document serves as a longer reflection on the development process of the Chinese Spelling Coach. It outlines what I learned, the problems encountered, and how I resolved them and grew through the project.

For a concise overview of the project and its features, please refer to "README.md".

## Project Motivation
I created this Chinese spelling coach to help my brother, who regularly has Chinese spelling tests, practise independently without requiring my father to read out the words for him.

As a busy person with many responsibilities, my father often had to take time out of his schedule to help with spelling practice, which was inconvenient and limited how often my brother could practise.

---
# Version 1: Terminal
## Initial Approach
The first version of the program was very simple:
- The user typed spelling words separated by commas
- The program split the input using commas
- The words were stored and shuffled
- The program printed the words one by one

This approach worked for basic word lists.

---

## Problems Encountered
I later realised that spelling tests could also include full sentences, which may contain commas. This made comma-based splitting unreliable.

The initial version also lacked important features such as:
- Repeating a word on command
- Hiding previously entered words to prevent cheating

---

## Improvements Made
To address these issues, I:
- Changed input to line-by-line entry instead of comma-separated input using a loop
- Added controls to repeat words or move to the next one
- Cleared the screen to prevent users from seeing previously entered words
- Used Google Text-to-Speech (gTTS) to read words aloud

---

## Key Lessons Learned
- Always design from the user’s point of view
- Anticipate real-world use cases early
- Iterative development leads to better solutions

---

## Reflection on Version Control
After completing the project, I realised that I had not implemented version control from the start. This would have made it difficult to track progress or show how the project evolved.

After researching solutions, I discovered GitHub and learned the importance of versioning. For future projects, I plan to use version control from the beginning.

# Version 2: User Interface
During testing, my brother found the terminal-based model inconvenient to use. When he requested the model to repeat a word, delays caused him to press the repeat command multiple times, resulting in the word being repeated repeatedly without a way to skip to the next word. This forced him to quit the program entirely, leading to frustration and him refusing to re-enter all the words.

## Solutions to the problems:
- Terminal-based interface was inconvenient: created a user-friendly GUI with buttons instead of relying on keyboard-triggered commands
- Words repeated without a way to skip: added a “Next Word” button that allows users to skip to the next word immediately, without waiting for audio playback to finish
- Having to re-enter words for continued practice: implemented a save/load progress feature so users can resume practice without retyping word