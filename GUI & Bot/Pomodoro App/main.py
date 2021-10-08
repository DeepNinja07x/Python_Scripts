from tkinter import *
import math
# ---------------------------- CONSTANTS ------------------------------- #
PINK = "#e2979c"
RED = "#e7305b"
GREEN = "#9bdeac"
YELLOW = "#f7f5dd"
FONT_NAME = "Courier"
WORK_MIN = 25
SHORT_BREAK_MIN = 5
LONG_BREAK_MIN = 20
reps = 0
timer = NONE
# ---------------------------- TIMER RESET ------------------------------- # 

def reset():
    window.after_cancel(timer)
    canvas.itemconfig(timer_text, text="00:00")
    label_1.config(text="Timer")
    label_tick.config(text="")
    global reps
    reps = 0

# ---------------------------- TIMER MECHANISM ------------------------------- # 

def start_timer():
    global reps
    reps += 1
    work_sec = WORK_MIN * 60
    short_break_sec = SHORT_BREAK_MIN * 60
    long_break_sec = LONG_BREAK_MIN * 60
    
    if reps%8 == 0:
        label_1.config(text="Long Break", fg=RED)
        countdown(long_break_sec)
    elif reps%2 == 0:
        label_1.config(text="Short Break", fg=PINK)
        countdown(short_break_sec)
    else:
        label_1.config(text="Work time!!", fg=GREEN)
        countdown(work_sec)
    
# ---------------------------- COUNTDOWN MECHANISM ------------------------------- # 

def countdown(count):
    
    count_min = math.floor(count / 60)
    count_sec = count % 60
    if count_sec < 10:
        count_sec = f"0{count_sec}"
    
    canvas.itemconfig(timer_text, text=f"{count_min}:{count_sec}")
    if count > 0:
        global timer
        timer = window.after(1000, countdown, count - 1)
    else:
        start_timer()
        marks = ""
        work_session = math.floor(0, reps/2)
        for _ in range(work_session):
            marks += "✓" 
        label_tick.config(text=marks)

# ---------------------------- UI SETUP ------------------------------- #

window = Tk()
window.title("Pomodoro App")
window.config(padx=100, pady=50, bg=YELLOW)

canvas = Canvas(width=200, height=224, bg=YELLOW, highlightthickness=0)
tomato_pic = PhotoImage(file="tomato.png")
canvas.create_image(100, 112, image=tomato_pic)
timer_text = canvas.create_text(100, 130, text="00:00", font=(FONT_NAME, 38, 'bold'), fill="white")
canvas.grid(column=1, row=1)

label_1 = Label(text="Timer",fg= GREEN, bg=YELLOW, highlightthickness=0, font=("B612 Mono", 28, "bold"))
label_1.grid(column=1, row=0)

button_start = Button(text="Start", bg=YELLOW, font=("B612 Mono", 12, "normal"), borderwidth=0, command=start_timer)
button_start.grid(column=0, row=2)

button_reset = Button(text="Reset", bg=YELLOW, font=("B612 Mono", 12, "normal"), borderwidth=0, command=reset)
button_reset.grid(column=2, row=2)

label_tick = Label(fg= GREEN, bg=YELLOW)
label_tick.grid(column=1, row=3)

window.mainloop()
