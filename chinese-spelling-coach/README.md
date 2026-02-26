# Chinese Spelling Coach
A Python-based Chinese spelling practice tool that allows students to practise independently using text-to-speech.

## Why This Project
I built this project to help my brother practise Chinese spelling on his own, without needing a parent to read the words aloud each time.

## Problem
Traditional spelling practice requires another person to read out words, which can be inconvenient for busy parents and limits how often students can practise.

## Solution
This program allows users to:
- Input Chinese spelling words or sentences line by line
- Start a mock spelling test
- Hear shuffled words read aloud using Google Text-to-Speech (gTTS)
- Repeat a word or move to the next one
- View all words at the end for marking

# Version 1: Terminal
## Technologies I learnt to use
- Python
- Google Text-to-Speech (gTTS)

## What I Learned
- Designing software from the user’s perspective
- Using text-to-speech libraries in Python
- Improving program functionality through iteration

## Future Improvements
- Add a graphical user interface
- Apply version control from the start

# Version 2(User Interface)
## What I learnt:
- Creating and linking buttons to functions
- Enabling and disabling buttons
- Customising frame colours for better UI design
- Implementing version control
- Saving and loading user progress
- Adding indexed word tracking in a Listbox

## Improvements made:
- Replaced keyboard-triggered commands with buttons for improved usability
- Implemented conditional button activation to prevent invalid actions
- Enhanced UI aesthetics through improved colour schemes
- Added automatic word indexing to track vocabulary count
- Enabled users to save and reload progress, without the need to keep re-entering words
- Allowed users to skip or quit at any time without waiting for audio playback to finish

## Technologies I learnt to use:
- customtkinter (for User Interface)

## Future Improvements:
- Implement adjustable speech speed control for personalised learning
- Develop a web-based version to increase accessibility and reach more users
- Integrate cloud-based progress saving to enable cross-device access and long-term tracking