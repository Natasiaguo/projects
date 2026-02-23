import customtkinter as ctk 
from gtts import gTTS
import random
import os
import time

root = ctk.CTk()
root.geometry("700x650")
root.title("听写练习")

words = []
practice_words = []
current_word = None
spoken_words = []
word_index = 0

def speak(word):
    repeat_button.configure(state="disabled")  
    if os.path.exists("word.mp3"):    
        os.remove("word.mp3")
    tts = gTTS(text=word, lang="zh-cn")
    tts.save("word.mp3")

    if os.name == "nt":
        os.system("start /wait word.mp3")
    else:
        os.system("afplay word.mp3")
    repeat_button.configure(state="normal")

def add_word():
    word = entry.get()
    if word:
        words.append(word)
        listbox.configure(state="normal")  # Enable to insert
        listbox.insert("end", word + "\n")
        entry.delete(0, "end")

def start_practice():
    global practice_words, spoken_words, word_index
    start_button.configure(state="disabled")  # Disable start button during practice
    if status_label.cget("text") == "请先添加词语！":
        status_label.configure(text="")
    entry.delete(0, "end")
    listbox.configure(state="normal")            # Enable to clear
    listbox.delete("1.0", "end")                 # Clear previous words
    listbox.configure(state="disabled")          # Disable again
        
    if not words:
        status_label.configure(text="请先添加词语！")
        start_button.configure(state="normal")  # Re-enable start button
        return
    else:
        practice_words = words.copy()
        random.shuffle(practice_words)
        words[:] = practice_words  # Update the global words list to the shuffled version
        spoken_words.clear()
        word_index = 0
        next_word()

def speak_numbered(word, number):
    # Say the number first
    speak(f"第{number}")  # "第1个", "第2个" etc.
    time.sleep(0.5)            # wait 1 second before saying the word
    speak(word)              # then speak the actual word

def next_word():
    global current_word, word_index
    if word_index < len(words):   # If words remain
        next_button.configure(state="disabled")  # Disable next button until current word is spoken
        current_word = words[word_index]  # Get word
        spoken_words.append(current_word) # Save it
        word_index += 1 # Move index forward
        status_label.configure(text=f"正在播放词语 ({word_index}/{len(practice_words)})")
        speak_numbered(current_word, word_index) # Speak word
        next_button.configure(state="normal")  # Re-enable next button
        
    else:
        current_word = None
        status_label.configure(text="听写完成！")
        speak("听写完成！以下是所有词语的总结：")
        show_summary()

def repeat_word():
        if current_word:
            speak(current_word)

def show_summary():
    summary_textbox.configure(state="normal") # Enable to show summary
    summary_textbox.delete("1.0", "end") # delete everything from start(1.0) to end
    
    for i, word in enumerate(spoken_words, start=1):
        summary_textbox.insert("end", f"{i}. {word}\n") # show summary, \n means next line
    summary_textbox.configure(state="disabled") # Disable again

# --------------- USER INTERFACE ---------------
main_frame = ctk.CTkFrame(root)
main_frame.pack(anchor="w", padx=30, pady=30)

title_label = ctk.CTkLabel(main_frame, text="听写练习", font=ctk.CTkFont(family="Arial", weight="bold", size=28))
title_label.pack(anchor="w", pady=10)

word_label = ctk.CTkLabel(main_frame, text=f"请写下听写字,\n点击‘开始’按钮开始听写练习：", font=ctk.CTkFont(family="Arial", size=16), justify="left", anchor="w")
word_label.pack(anchor="w", pady=(10, 10))

entry = ctk.CTkEntry(main_frame, width=400, height=45, font=ctk.CTkFont(family="Arial", size=16))
entry.pack(anchor="w", pady=(5, 15))

add_button = ctk.CTkButton(main_frame, text="添加词语", width=150, height=40, command=add_word)
add_button.pack(anchor="w", pady=(0, 20))

listbox = ctk.CTkTextbox(main_frame, width=400, height=120, font=ctk.CTkFont(size=14))
listbox.pack(anchor="w", pady=(0, 20))
listbox.configure(state="disabled")  # Make it read-only

button_frame = ctk.CTkFrame(main_frame)
button_frame.pack(anchor="w")

start_button = ctk.CTkButton(button_frame, text="开始", command=start_practice)
start_button.pack(side="left", padx=5)

repeat_button = ctk.CTkButton(button_frame, text="重复播放", command=repeat_word)
repeat_button.pack(side="left", padx=5)

next_button = ctk.CTkButton(button_frame, text="下一个", command=next_word)
next_button.pack(side="left", padx=5)

status_label = ctk.CTkLabel(main_frame, text="", font=ctk.CTkFont(family="Arial", size=14))
status_label.pack(anchor="w", padx=(15, 5))

summary_textbox = ctk.CTkTextbox(main_frame, width=400, height=150, font=ctk.CTkFont(size=14))
summary_textbox.pack(anchor="w", pady=(10, 0))
summary_textbox.configure(state="disabled")  

root.mainloop()