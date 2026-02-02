import customtkinter as ctk
import time

# Open window
app = ctk.CTk()
app.geometry("600x500")
app.title("Study Reward Tracker")

start_time = None
# Timer display
timer_label = ctk.CTkLabel(app, text="Time Studied: 00:00", font=("Arial", 24))
timer_label.pack(pady=20)

# Reward display
reward_label = ctk.CTkLabel(app, text="", font=("Arial", 18))
reward_label.pack(pady=20)

def start_timer():
    global start_time
    start_time = time.time()
    timer_label.configure(text="Time Studied: 00:00")
    reward_label.configure(text="")
    update_timer()
    stop_button.pack(pady=20)
    reset_button.pack_forget()

def update_timer():
    if start_time is not None:
        elapsed_time = time.time() - start_time
        minutes, seconds = divmod(int(elapsed_time), 60)
        timer_label.configure(text=f"Time Studied: {minutes:02}:{seconds:02}")
        app.after(1000, update_timer) 

def stop_timer():
    global start_time
    if start_time is not None:
        elapsed_time = time.time() - start_time
        minutes, seconds = divmod(int(elapsed_time), 60)
        reward_label.configure(text=f"Great job! You studied for {minutes} minutes and {seconds} seconds.")
        start_time = None
        stop_button.pack_forget()
        reset_button.pack(pady=20)

def reset_timer():
    global start_time
    start_time = None
    timer_label.configure(text="Time Studied: 00:00")
    reward_label.configure(text="")
    reset_button.pack_forget()

start_button = ctk.CTkButton(app, text="Start Studying", command=start_timer)
start_button.pack(pady=20)

stop_button = ctk.CTkButton(app, text="Stop Studying", command=stop_timer)
stop_button.pack_forget()

reset_button = ctk.CTkButton(app, text="Reset Timer", command=reset_timer)
reset_button.pack_forget()

app.mainloop()