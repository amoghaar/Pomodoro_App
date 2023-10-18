import math
from tkinter import *

# ---------------------------- CONSTANTS ------------------------------- #

# Color codes for the interface
PINK = "#e2979c"
RED = "#e7305b"
GREEN = "#9bdeac"
YELLOW = "#f7f5dd"
FONT_NAME = "Courier"
CHECK = "✔"

# Time durations in minutes for work, short break, and long break
WORK_MIN = 25
SHORT_BREAK_MIN = 5
LONG_BREAK_MIN = 20

# Repetition counter and timer variable
rep = 0
timer = None


# ---------------------------- TIMER RESET ------------------------------- #

def reset_timer():
    """
    Reset the timer, labels, and repetition counter.
    """
    window.after_cancel(timer)  # Cancel any running timer
    label_title.config(text="Timer")  # Reset title label
    label_check.config(text="", background=YELLOW, fg=GREEN)  # Reset check label
    canvas.itemconfig(time_count, text="00:00")  # Reset timer display
    global rep
    rep = 0  # Reset repetition counter


# ---------------------------- TIMER MECHANISM ------------------------------- #

def start_timer():
    """
    Start the timer and alternate between work and break periods.
    """
    global rep
    rep += 1

    # Reset repetition counter after 8 intervals
    if rep == 9:
        rep = 1
        label_check.config(text="", background=YELLOW, fg=GREEN)
        label_title.config(text="Timer", fg=GREEN)

    # Work period
    if rep in [1, 3, 5, 7]:
        count_down(WORK_MIN * 60)
        label_title.config(text="Work", fg=GREEN)
        window.deiconify()

    # Short break
    elif rep in [2, 4, 6]:
        count_down(SHORT_BREAK_MIN * 60)
        label_title.config(text="Break", fg=PINK)
        window.deiconify()
        if rep == 2:
            label_check.config(text=CHECK)
        elif rep == 4:
            label_check.config(text=f"{CHECK}{CHECK}")
        else:
            label_check.config(text=f"{CHECK}{CHECK}{CHECK}")

    # Long break
    else:
        count_down(LONG_BREAK_MIN * 60)
        label_title.config(text="Break", fg=RED)
        label_check.config(text=CHECK, fg=RED)
        window.deiconify()


# ---------------------------- COUNTDOWN MECHANISM ------------------------------- #

def count_down(num):
    """
    Count down from a given number of seconds and update the display.
    """
    count_min = math.floor(num / 60)
    count_sec = num % 60
    if len(str(count_sec)) == 1:
        count_sec = f"0{count_sec}"
    canvas.itemconfig(time_count, text=f"{count_min}:{count_sec}")
    if num > 0:
        global timer
        timer = window.after(1000, count_down, num - 1)
    else:
        start_timer()


# ---------------------------- UI SETUP ------------------------------- #

# Create the main window
window = Tk()
window.title("Pomodoro App")
window.config(padx=100, pady=50, background=YELLOW)

# Title label
label_title = Label(text="Timer", font=(FONT_NAME, 30, "bold"), background=YELLOW, fg=GREEN)
label_title.grid(column=1, row=0)

# Canvas for displaying timer and tomato image
canvas = Canvas(width=200, height=224, background=YELLOW, highlightthickness=0)
image = PhotoImage(file="tomato.png")  # Image file assumed to be "tomato.png"
canvas.create_image(100, 112, image=image)
time_count = canvas.create_text(100, 130, text="00:00", font=(FONT_NAME, 30, "bold"), fill="white")
canvas.grid(column=1, row=1)

# Start button
button1 = Button(text="Start", command=start_timer)
button1.grid(column=0, row=2)

# Reset button
button2 = Button(text="Stop", command=reset_timer)
button2.grid(column=2, row=2)

# Checkmark label
label_check = Label(background=YELLOW, fg=GREEN)
label_check.grid(column=1, row=3)

# Run the application
window.mainloop()
