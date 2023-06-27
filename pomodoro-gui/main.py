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
timer = None
# ---------------------------- TIMER RESET ------------------------------- #

def reset():
    window.after_cancel(timer)
    label.config(text="Timer")
    canvas.itemconfig(timer_text, text="00:00")
    check.config(text="")
    global reps
    reps = 0


# ---------------------------- TIMER MECHANISM ------------------------------- # 

def start_timer():
    global reps
    work_secs = WORK_MIN * 60
    short_break = SHORT_BREAK_MIN * 60
    long_break = LONG_BREAK_MIN * 60
    reps += 1
    if reps % 2 != 0 and reps < 8:
        label.config(text="Timer", fg=GREEN, font=(FONT_NAME, 50), bg=YELLOW,)
        count_down(work_secs)
    elif reps % 2 == 0 and reps < 8:
        label.config(text="Short Break", fg=PINK, font=(FONT_NAME, 50), bg=YELLOW, )
        count_down(short_break)
    else:
        label.config(text="Long Break", fg=RED, font=(FONT_NAME, 50), bg=YELLOW, )
        reps = 0
        count_down(long_break)

# ---------------------------- COUNTDOWN MECHANISM ------------------------------- # 

def count_down(x):
    min = math.floor(x/60)
    secs = x % 60
    if secs < 10:
        secs = f"0{secs}"
    canvas.itemconfig(timer_text, text=f"{min}:{secs}")
    if x > 0:
        global timer
        timer = window.after(1000, count_down, x-1)
    else:
        start_timer()
        mark = ""
        sessions = math.floor(reps/2)
        for i in range(sessions):
            mark += "✓"
        check.config(text=mark)

# ---------------------------- UI SETUP ------------------------------- #

window = Tk()
window.title("Pomodoro")
window.config(padx=100, pady=50, bg=YELLOW)


canvas = Canvas(width=200, height=224, bg=YELLOW, highlightthickness=0)
photo = PhotoImage(file="tomato.png")
canvas.create_image(100, 112, image=photo)
timer_text = canvas.create_text(100, 130, text="00:00", fill="white", font=(FONT_NAME, 35, "bold"))
canvas.grid(column=1, row=1)


label = Label(text="Timer", fg=GREEN, font=(FONT_NAME, 50), bg=YELLOW,)
label.grid(column=1, row=0)

start_button = Button(text="Start", width=1, highlightthickness=0, command=start_timer)
start_button.grid(column=0, row=2)

reset_button = Button(text="Reset", width=1, highlightthickness=0, command=reset)
reset_button.grid(column=2, row=2)

check = Label(fg=GREEN, bg=YELLOW)
check.grid(column=1, row=3)


window.mainloop()