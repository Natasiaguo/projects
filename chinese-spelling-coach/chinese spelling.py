# Chinese Spelling Coach
from gtts import gTTS
import random
import os
import time
def speak(word):
    if os.path.exists("word.mp3"):
        os.remove("word.mp3")
    tts = gTTS(text=word, lang="zh-cn")
    tts.save("word.mp3")
    if os.name == "nt":
        os.system("start word.mp3")
    else:
        os.system("afplay word.mp3")    

def clear_screen():
    os.system("cls" if os.name == "nt" else "clear")
words_dict = {}
count = 1
# Let user to provide the spelling words line by line
while True:
    words = input("请写下来你的听写字。如果写完了，请安‘1’: ")
    if words == "1":
        break
    words_dict[count] = words
    count += 1
print("Press Enter to start the 听写：")

# another input
input()
clear_screen()
time.sleep(0.1)
keys = list(words_dict.keys())
random.shuffle(keys)
for i, key in enumerate(keys, start=1):
    print(f"Word {i}/{len(keys)}")
    speak(words_dict[key])
    while True:
        action = input("按 Enter 播放词语，或输入‘2’进入下一个词语： ").strip()
        clear_screen()
        if action == "2":
            break
        else:
            speak(words_dict[key])
clear_screen()
speak("听写完成！谢谢！")
speak("以下是所有词语的总结")
print("听写总结：")
for i, key in enumerate(keys, start=1):
    print(f"{i}. {words_dict[key]}")   