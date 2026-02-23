import customtkinter as ctk
from gtts import gTTS
import random
import os
import time

# ---------------- GLOBAL STATE ----------------
words = []             # All words added by user
practice_words = []    # Shuffled copy for spelling
spoken_words = []      # Words already spoken
current_word = None
word_index = 0
current_number = 1

# ---------------- FUNCTIONS ----------------
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

def speak_numbered(word, number):
    # Say number first, then the word
    speak(f"第{number}")
    time.sleep(0.5)
    speak(word)

def add_number(event):
    # Add new number on Enter press
    global current_number
    current_number += 1
    listbox.insert("end", f"\n{current_number}. ")
    listbox.see("end")
    return "break"  # prevent default newline

def start_practice():
    global practice_words, spoken_words, word_index, words
    start_button.configure(state="disabled")
    
    listbox_text = listbox.get("1.0", "end").strip()
    
    if not listbox_text:
        status_label.configure(text="请先添加词语！")
        start_button.configure(state="normal")
        return

    status_label.configure(text="")

    lines = listbox_text.split("\n")
    words = [line.split(".", 1)[1].strip() if ". " in line else line for line in lines if line.strip()]
    
    practice_words = words.copy()
    random.shuffle(practice_words)
    words[:] = practice_words
    spoken_words.clear()
    word_index = 0
    next_word()

def next_word():
    global current_word, word_index
    if word_index < len(words):
        next_button.configure(state="disabled")
        current_word = words[word_index]
        spoken_words.append(current_word)
        word_index += 1
        status_label.configure(text=f"正在播放词语 ({word_index}/{len(practice_words)})")
        speak_numbered(current_word, word_index)
        next_button.configure(state="normal")
    else:
        current_word = None
        status_label.configure(text="听写完成！")
        speak("听写完成！以下是所有词语的总结：")
        show_summary()

def repeat_word():
    if current_word:
        speak(current_word)

def show_summary():
    summary_textbox.configure(state="normal")
    summary_textbox.delete("1.0", "end")
    for i, word in enumerate(spoken_words, start=1):
        summary_textbox.insert("end", f"{i}. {word}\n")
    summary_textbox.configure(state="disabled")

def initialize_listbox():
    global current_number
    listbox.configure(state="normal")
    listbox.delete("1.0", "end")
    current_number = 1
    listbox.insert("end", f"{current_number}. ")

def abort_test():
    global current_word, word_index
    current_word = None
    word_index = 0
    status_label.configure(text="测试已中止！")
    
    summary_textbox.configure(state="normal")
    summary_textbox.delete("1.0", "end")    # Clear summary
    summary_textbox.configure(state="disabled")
    
    start_button.configure(state="normal")  # Allow restarting
    repeat_button.configure(state="disabled")
    next_button.configure(state="disabled")
    initialize_listbox()

# ---------------- USER INTERFACE ----------------
root = ctk.CTk()
root.geometry("700x650")
root.title("听写练习")

main_frame = ctk.CTkFrame(root)
main_frame.pack(anchor="w", padx=30, pady=30)

title_label = ctk.CTkLabel(main_frame, text="听写练习", font=ctk.CTkFont(family="Arial", weight="bold", size=28))
title_label.pack(anchor="w", pady=10)

word_label = ctk.CTkLabel(main_frame, text="请在下方输入词语，每行一个词语，按Enter自动编号：", font=ctk.CTkFont(family="Arial", size=16), justify="left", anchor="w")
word_label.pack(anchor="w", pady=(10, 10))

listbox = ctk.CTkTextbox(main_frame, width=400, height=120, font=ctk.CTkFont(size=14))
listbox.pack(anchor="w", pady=(0, 20))
listbox.bind("<Return>", add_number)
initialize_listbox()

listbox.see("end")  # make sure it's visible

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

abort_button = ctk.CTkButton(button_frame, text="结束测试", command=abort_test)
abort_button.pack(side="left", padx=5)

# ---------------- MAIN LOOP ----------------
root.mainloop()