# from sqlite_database import *
# from data import *
# from operations import *

from tkinter import *
from tkinter.ttk import *
import re

#initial popup window
window = Tk()
window.title("RUBi")
window.geometry('1300x800')
window.minsize(300, 300)

#welcome message
welcome = Label(window, text="Hello, welcome to RUBi. Please fill out the following information:", font=("Arial Bold", 20))
welcome.place(x=0, y=0)

window.mainloop()

