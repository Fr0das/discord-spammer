from pynput.keyboard import Key, Controller
import time
import clipboard

from tkinter import *
# Packages
gui = Tk()


gui.geometry("800x300")
gui.resizable(width=False, height=False)
gui.title('Discord Spammer')
# GUI

def getTextInput():
    result = text_box.get("1.0","end")
    clipboard.copy(result)
# Text Input Value Command

def startSpamming():
    time.sleep(4)
    for _ in range(15):
        keyboard = Controller()
        with keyboard.pressed(Key.ctrl):
            keyboard.press('v')
            keyboard.release('v')
        keyboard.press(Key.enter)
        keyboard.release(Key.enter)
        time.sleep(0.5)

# Main Spamming Command


btn = Button(gui, text = 'Copy Text', bg = 'gray', width = 20, height = 3, command = getTextInput)
btn.pack()
btn.place(x=340, y=130)
# Copies a text

btn = Button(gui, text = 'Start Spam', bg = 'green', width = 40, height = 5, command = startSpamming)
btn.pack()
btn.place(x=270, y=200)
# Start Spam Button

text_box = Text(
    gui,
    height=2,
    width=100,
    font=("Arial", 32
))

text_box.pack()
# Text Box

gui.mainloop()

# Project by Fr0das
# Project by Fr0das
# Project by Fr0das