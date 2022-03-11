from tkinter import *
from PIL import ImageTk, Image
import random
import math

# ---------------------------- CONSTANTS ------------------------------- #
PINK = "#e2979c"
RED = "#e7305b"
GREEN = "#9bdeac"
YELLOW = "#f7f5dd"
FONT_NAME = "Courier"
WORK_MIN = 1
SHORT_BREAK_MIN = 5
LONG_BREAK_MIN = 20
reps = 0
timer = None
# ---------------------------- Mechanism ------------------------------- #

letters = ['There can never be too many cherries on an ice cream sundae.', 'We have young kids who often walk into our '
                                                                           'room at night for various reasons '
                                                                           'including clowns in the closet.',
           'Lets all be unique together until we realise we are all the same.', 'Trash covered the landscape like '
                                                                                'sprinkles do a birthday cake.',
           'When confronted with a rotary dial phone the teenager was perplexed.']
random_words = random.choice(letters)


# ---------------------------- TIMER MECHANISM ------------------------------- #

def start_timer():
    work_sec = WORK_MIN * 60
    count_down(work_sec)
    title_label.config(text="Typing", fg='white')


# ---------------------------- COUNTDOWN MECHANISM ------------------------------- #
def count_down(count):
    count_min = math.floor(count / 60)
    count_sec = count % 60
    if count_sec < 10:
        count_sec = f"0{count_sec}"

    canvas.itemconfig(timer_text, text=f"{count_min}:{count_sec}")
    if count > 0:
        global timer
        timer = window.after(1000, count_down, count - 1)
    return count


def reset_timer():
    window.after_cancel(timer)
    canvas.itemconfig(timer_text, text="00:00")
    title_label.config(text="Timer")
    print(timer)


# ---------------------------- functions ------------------------------- #
def get_words():
    typing_entry = typing.get()
    print(typing_entry)
    reset_timer()


# ---------------------------- UI SETUP ------------------------------- #
window = Tk()
window.title("Typing speed")
window.config(padx=100, pady=50, )
title_label = Label(text="TypeSpeed", font=(FONT_NAME, 50))
title_label.grid(column=1, row=0)

canvas = Canvas(width=200, height=200, bg=YELLOW, highlightthickness=0)
tomato_img = ImageTk.PhotoImage(Image.open("typing.jpg"))
canvas.create_image(100, 112, image=tomato_img)
timer_text = canvas.create_text(100, 130, text="00:00", fill="white", font=(FONT_NAME, 35, "bold"))
canvas.grid(column=1, row=1)

text = Text(height=5, width=30)
# Puts cursor in textbox.

# Adds some text to begin with.
text.insert(END, f"{random_words}")
text.grid(row=2, column=1, columnspan=2)

typing = Entry(width=30)
# Puts cursor in textbox.
typing.focus()
# Adds some text to begin with.
typing.grid(row=3, column=1, columnspan=2)

# BUTTONS
start = Button(text="start", command=start_timer)
start.grid(row=4, column=1)
finish = Button(text="finish", command=get_words)
finish.grid(row=4, column=2)

window.mainloop()
