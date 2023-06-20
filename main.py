from tkinter import *
import pandas as pd
from random import choice

from tkinter import messagebox


BACKGROUND_COLOR = "#B1DDC6"
WIDTH, HEIGHT = (800, 526)
FONT_NAME = "Arial"
TITLE_POS = (400, 150)
WORD_POS = (400, 263)

data_words = pd.read_csv("data/french_words.csv")
data_words = data_words.to_dict(orient="records")

after_id = None
# ---------------------------- DISPLAY WORDS------------------------------- #
def flip_card(card):
    image_back = PhotoImage(file="./images/card_back.png")
    canvas.itemconfig(card_side, image = image_back)
    canvas.itemconfig(title_displayed, text = "English", fill = "white")
    canvas.itemconfig(word_displayed, text = card["English"], fill = "white")


def display_words():
    #global title_displayed, word_displayed
    global after_id

    canvas.itemconfig(card_side, image=image_front)

    if after_id:
        window.after_cancel(after_id) # to cancel the effect of after, in case we hit a button several times

    langage = list(data_words[0])[0]
    new_card = choice(data_words)

    canvas.itemconfig(title_displayed, text = langage, fill = "black")
    canvas.itemconfig(word_displayed, text = new_card[langage], fill = "black")

    #flip the card after 3 seconds
    after_id = window.after(3000, lambda: flip_card(new_card))


# ---------------------------- GUI WINDOW ------------------------------- #
window = Tk()
window.title("Flashy")
window.config(bg=BACKGROUND_COLOR)
window.config(padx=50, pady=50)

# CANVAS
canvas = Canvas(width=WIDTH, height=HEIGHT, highlightthickness=0, bg=BACKGROUND_COLOR)
image_front = PhotoImage(file="./images/card_front.png")
card_side = canvas.create_image((WIDTH) / 2, (HEIGHT) / 2, image=image_front)

title_displayed = canvas.create_text(TITLE_POS, text="Title", font=(FONT_NAME, 40, 'italic'))
word_displayed  = canvas.create_text(WORD_POS, text="Word", font=(FONT_NAME, 60, 'bold'))
canvas.grid(column=0, row=0, columnspan=2)

display_words() # in order to start with a french word

#BUTTONS
image_wrong = PhotoImage(file="./images/wrong.png")
button_wrong = Button(image=image_wrong, bg=BACKGROUND_COLOR, highlightthickness=0, command=display_words)
button_wrong.grid(column=0, row=1, columnspan=1)

image_right = PhotoImage(file="./images/right.png")
button_right = Button(image=image_right, bg=BACKGROUND_COLOR, command=display_words)
button_right.grid(column=1, row=1, columnspan=1)



window.mainloop()

