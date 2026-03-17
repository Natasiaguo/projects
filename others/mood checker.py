def prompt_mood():
    user_input = input('How are you feeling today? ').lower()
    moods = {
        "happy": ["happy", "promoted", "amazing", "great", "glad", "excited", "awesome", "good"],
        "sad": ["sad", "disappointed", "upset", "unhappy", "devastated", "depressed", "down", "miserable", "heartbroken"],
        "angry": ["frustrated", "angry", "mad", "irritated", "pissed", "furious"],
        "anxious": ["nervous", "exam", "anxious", "panic", "panicky", "panicked", "worried", "scared", "overthinking", "can't stop thinking","racing thoughts", "spiralling", "what if", "worried about", "heart racing", "tight chest", "short of breath", "shaking", "sweaty", "restless", "stressed", "pressure", "on edge", "uneasy", "tense"]
        }
    responses = {
        "happy": "I'm so happy to hear that!",
        "sad": "I'm so sorry to hear that, but don't worry, there will always be better days:)",
        "angry": "I TOTALLY UNDERSTAND HOW YOU ARE FEELING -- haizz life can be like that sometimes...",
        "anxious": "Try to take deep breaths! Breath in for 4 seconds, hold for 4 seconds, and breathe out for 4 seconds, releasing all your stress with you<3"
        } 
    scores = {
        "happy": 0,
        "sad": 0,
        "angry": 0,
        "anxious": 0
        }
    
    for mood, keywords in moods.items():
        for word in keywords:
            if word in user_input:
                scores[mood] += 1
                print("my mood ", mood, "score", scores[mood])
                detected_mood = max(scores, key=scores.get) 
                print("scores.get: ", max(scores, key=scores.get))
    
    # Determine the mood if any score > 0
    if max(scores.values()) > 0:
        detected_mood = max(scores, key=scores.get)
        print("scores.get:", detected_mood)
        print("hello")            
        print(responses[detected_mood])
    else:
        print("hello")
        print("Thanks for sharing!")

while True:
    prompt_mood()
    restart = input("Would you like to continue chatting? y/n")
    if restart == "n":
        break