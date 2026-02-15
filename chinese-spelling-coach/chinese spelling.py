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
while True:
    words = input("请写下来你的听写字。如果写完了，请安‘1’: ")
    if words == "1":
        break
    words_dict[count] = words
    count += 1
print("Press Enter to start the 听写：")
input()
clear_screen()
time.sleep(0.1)
keys = list(words_dict.keys())
random.shuffle(keys)
for i, key in enumerate(keys, start=1):
    print(f"Word {i}/{len(keys)}")
    speak(words_dict[key])
    
    while True:
        print("按下‘Enter’键跳过，或等待重复播放。")
        
        start = time.time()
        while time.time() - start < 5:  # 等待5秒钟
            if os.name == "posix":
                pass
            time.sleep(0.1)

        speak(words_dict[key])

        action = input("按下‘Enter’ 跳过，或按下‘q’退出：")
        if action == "":
            break
        elif action.lower() == "q":
            print("退出听写。")
            exit()    
clear_screen()
speak("听写完成！谢谢！")
speak("以下是所有词语的总结")
print("听写总结：")
for i, key in enumerate(keys, start=1):
    print(f"{i}. {words_dict[key]}")  
