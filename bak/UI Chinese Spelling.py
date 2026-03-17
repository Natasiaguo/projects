import customtkinter as ctk
from gtts import gTTS
import random
import os
import time
import tkinter.messagebox as mb
import subprocess
import json

# ---------------- GLOBAL STATE ----------------
words = []             # All words added by user
practice_words = []    # Shuffled copy for spelling
spoken_words = []      # Words already spoken
current_word = None
word_index = 0
current_number = 1
audio_process = None
audio_playing = False
callback = None

# ---------------- FUNCTIONS ----------------
def speak(word, callback=None):
    global audio_process, audio_playing

    audio_playing = True
    repeat_button.configure(state="disabled")
    next_button.configure(state="disabled")
    start_button.configure(state="disabled")
    if os.path.exists("word.mp3"):
        os.remove("word.mp3")
    tts = gTTS(text=word, lang="zh-cn")
    tts.save("word.mp3")
    if audio_process and audio_process.poll() is None: # if audio is still playing, stop it safely before starting new one
        audio_process.terminate()
    
    # Play audio without blocking
    if os.name == "nt":  # Windows
        audio_process = subprocess.Popen(["start", "word.mp3"], shell=True)
    else:  # Mac / Linux
        audio_process = subprocess.Popen(["afplay", "word.mp3"])

    check_audio_finished(callback)

def check_audio_finished(callback=None):
    global audio_process, audio_playing
    if audio_process.poll() is None:
        # still playing -> check again in 200ms
        root.after(200, lambda: check_audio_finished(callback))
    else:
        audio_playing = False
        if callback:
            callback()
        else:    
            repeat_button.configure(state="normal")
            next_button.configure(state="normal")
            start_button.configure(state="normal")

def speak_numbered(word, number):
    # Say number first, then the word
    def speak_word():
        speak(word)
    speak(f"第{number}", callback=lambda: speak_word())

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
    listbox.delete("1.0", "end")
    listbox.configure(state="disabled")  # disable editing during practice
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
    if mb.askyesno("确认", "确定要结束测试吗？"):
        global current_word, word_index
        current_word = None
        word_index = 0
        status_label.configure(text="测试已中止！")
        
        summary_textbox.configure(state="normal")
        summary_textbox.delete("1.0", "end")    # Clear summary
        summary_textbox.configure(state="disabled")
        
        start_button.configure(state="normal") 
        repeat_button.configure(state="disabled")
        next_button.configure(state="disabled")
    else:
        pass    
    initialize_listbox()

def save_progress():
    if not practice_words:
        status_label.configure(text="没有词语可保存！")
        return
    listbox_text = listbox.get("1.0", "end").strip()
    data = {
        "practice_words": practice_words,
        "word_index": word_index,
        "spoken_words": spoken_words,
        "listbox_text": listbox_text
    }
    with open("test_progress.json", "w", encoding="utf-8") as f:
        json.dump(data, f, ensure_ascii=False)
    status_label.configure(text="词语已保存！")

def load_progress():
    global practice_words, spoken_words, word_index, words, current_word

    try:
        with open("test_progress.json", "r", encoding="utf-8") as f:
            data = json.load(f)

        practice_words = data["practice_words"]
        spoken_words = data["spoken_words"]
        word_index = data["word_index"]
        words[:] = practice_words

        listbox.configure(state="normal") 
        listbox.delete("1.0", "end")
        listbox.insert("1.0", data.get("listbox_text", ""))   
        listbox.see("end")

        if word_index < len(practice_words):
            current_word = words[word_index]
            status_label.configure(text=f"已加载测试进度！下一个词语: {word_index + 1}/{len(practice_words)}")
        else:
            current_word = None
            status_label.configure(text="听写已完成！")

        start_button.configure(state="disabled")
        repeat_button.configure(state="normal")
        next_button.configure(state="normal")

    except FileNotFoundError:
        status_label.configure(text="没有找到保存的进度！")     

## ---------------- USER INTERFACE ----------------
ctk.set_appearance_mode("light")

root = ctk.CTk()
root.attributes("-fullscreen", True)
root.title("听写练习")
root.configure(fg_color="#CFE3F8")

main_frame = ctk.CTkFrame(root, fg_color="#CFE3F8")
main_frame.pack(expand=True, fill="both")

# title
title_label = ctk.CTkLabel(main_frame, text="听写练习", font=ctk.CTkFont(family="Arial", weight="bold", size=30))
title_label.pack(anchor="n", pady=(20,10), padx=50)

# instructions
word_label = ctk.CTkLabel(main_frame, text="请在下方输入词语，每行一个词语，按Enter自动编号：", font=ctk.CTkFont(family="Arial", size=18), justify="left", anchor="w")
word_label.pack(anchor="w", pady=(10, 10), padx=50)

#input section
input_section_label = ctk.CTkLabel(main_frame, text="词语输入", font=ctk.CTkFont(size=22, weight="bold"))
input_section_label.pack(anchor="w", pady=(0,10),padx=50)

listbox = ctk.CTkTextbox(main_frame, width=400, height=120, font=ctk.CTkFont(size=16))
listbox.pack(fill="both", expand=True, padx=50, pady=(0,10))
listbox.bind("<Return>", add_number)
initialize_listbox()

listbox.see("end")  # make sure it's visible

# buttons
button_frame = ctk.CTkFrame(main_frame, fg_color="#CFE3F8")
button_frame.pack(padx=50, pady=(10,5), fill="x")

start_button = ctk.CTkButton(button_frame, text="开始", fg_color="#1FAD5A", hover_color="#3E9647", width=120, height=50, font=ctk.CTkFont(size=16), command=start_practice)
start_button.pack(side="left", padx=5)

repeat_button = ctk.CTkButton(button_frame, text="重复播放", width=120, height=50, font=ctk.CTkFont(size=16), command=repeat_word)
repeat_button.pack(side="left", padx=5)

next_button = ctk.CTkButton(button_frame, text="下一个", fg_color="#74571E", hover_color="#57461D", width=120, height=50,font=ctk.CTkFont(size=16),command=next_word)
next_button.pack(side="left", padx=5)

abort_button = ctk.CTkButton(button_frame, text="结束测试", fg_color="#F40C0C", hover_color="#C40202", width=120, height=50, font=ctk.CTkFont(size=16),command=abort_test)
abort_button.pack(side="left", padx=5)

repeat_button.configure(state="normal")
next_button.configure(state="normal")

# status
status_label = ctk.CTkLabel(main_frame, text="", font=ctk.CTkFont(family="Arial", size=18))
status_label.pack(anchor="w", padx=(15, 5))

# summary section
summary_frame = ctk.CTkFrame(main_frame, fg_color="#CFE3F8")
summary_frame.pack(fill="both", expand=True, padx=50, pady=(10,10))

summary_section_label = ctk.CTkLabel(summary_frame, text="听写总结", font=ctk.CTkFont(size=22, weight="bold"))
summary_section_label.pack(anchor="w", pady=(0,5))

summary_textbox = ctk.CTkTextbox(summary_frame, font=ctk.CTkFont(size=16))
summary_textbox.pack(fill="both", expand=True)
summary_textbox.configure(state="disabled")

# save/load buttons
progress_frame = ctk.CTkFrame(main_frame, fg_color="#CFE3F8")
progress_frame.pack(padx=50, pady=(5,20), fill="x")

save_button = ctk.CTkButton(progress_frame, text="保存词语", width=120, height=50, font=ctk.CTkFont(size=16),command=save_progress)
save_button.pack(side="left", padx=5)

load_button = ctk.CTkButton(progress_frame, text="加载词语", width=120, height=50, font=ctk.CTkFont(size=16), command=load_progress)
load_button.pack(side="left", padx=5)

# ---------------- MAIN LOOP ----------------
root.mainloop()