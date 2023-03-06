# Importing libraries
import math
import tkinter as tk
from tkinter import *
from tkinter import ttk

# Define some colours
black = "#000000"
white = "#ffffff"
dark_blue = "#06042b"
green = "#077d21"
light_green = "#83e864"
gray = "#adadad"

# Creating the calculator window
window = Tk()
window.iconbitmap("pi_icon.ico")
window.title("Calculator")
window.geometry("360x602")
window.config(bg=black)

# Split window into display and buttons
display_window = Frame(window, width=360, height=105, bg=dark_blue)
display_window.grid(row=0, column=0)

body_window = Frame(window, width=360, height=497)
body_window.grid(row=1, column=0)

# Creating buttons
b_C = Button(body_window, text="C", width=37, height=3, bg=green, font="Roboto 8 bold", relief=RAISED, overrelief=RIDGE)
b_C.place(x=2, y=142)
b_0 = Button(body_window, text="0", width=24, height=3, font="Roboto 8 bold", relief=RAISED, overrelief=RIDGE)
b_0.place(x=2, y=426)
b_1 = Button(body_window, text="1", width=11, height=3, font="Roboto 8 bold", relief=RAISED, overrelief=RIDGE)
b_1.place(x=2, y=355)
b_2 = Button(body_window, text="2", width=11, height=3, font="Roboto 8 bold", relief=RAISED, overrelief=RIDGE)
b_2.place(x=92, y=355)
b_3 = Button(body_window, text="3", width=11, height=3, font="Roboto 8 bold", relief=RAISED, overrelief=RIDGE)
b_3.place(x=182, y=355)
b_4 = Button(body_window, text="4", width=11, height=3, font="Roboto 8 bold", relief=RAISED, overrelief=RIDGE)
b_4.place(x=2, y=284)
b_5 = Button(body_window, text="5", width=11, height=3, font="Roboto 8 bold", relief=RAISED, overrelief=RIDGE)
b_5.place(x=92, y=284)
b_6 = Button(body_window, text="6", width=11, height=3, font="Roboto 8 bold", relief=RAISED, overrelief=RIDGE)
b_6.place(x=182, y=284)
b_7 = Button(body_window, text="7", width=11, height=3, font="Roboto 8 bold", relief=RAISED, overrelief=RIDGE)
b_7.place(x=2, y=213)
b_8 = Button(body_window, text="8", width=11, height=3, font="Roboto 8 bold", relief=RAISED, overrelief=RIDGE)
b_8.place(x=92, y=213)
b_9 = Button(body_window, text="9", width=11, height=3, font="Roboto 8 bold", relief=RAISED, overrelief=RIDGE)
b_9.place(x=182, y=213)
b_dot = Button(body_window, text=".", width=11, height=3, font="Roboto 8 bold", relief=RAISED, overrelief=RIDGE)
b_dot.place(x=182, y=426)
b_equals = Button(body_window, text="=", width=11, height=3, bg=light_green, font="Roboto 8 bold", relief=RAISED, overrelief=RIDGE)
b_equals.place(x=272, y=426)
b_plus = Button(body_window, text="+", width=11, height=3, bg=light_green, font="Roboto 8 bold", relief=RAISED, overrelief=RIDGE)
b_plus.place(x=272, y=355)
b_minus = Button(body_window, text="-", width=11, height=3, bg=light_green, font="Roboto 8 bold", relief=RAISED, overrelief=RIDGE)
b_minus.place(x=272, y=284)
b_times = Button(body_window, text="*", width=11, height=3, bg=light_green, font="Roboto 8 bold", relief=RAISED, overrelief=RIDGE)
b_times.place(x=272, y=213)
b_divide = Button(body_window, text="/", width=11, height=3, bg=light_green, font="Roboto 8 bold", relief=RAISED, overrelief=RIDGE)
b_divide.place(x=272, y=142)
b_pi = Button(body_window, text="pi", width=11, height=3, bg=gray, font="Roboto 8 bold", relief=RAISED, overrelief=RIDGE)
b_pi.place(x=2, y=71)
b_e = Button(body_window, text="e", width=11, height=3, bg=gray, font="Roboto 8 bold", relief=RAISED, overrelief=RIDGE)
b_e.place(x=92, y=71)
b_sqr = Button(body_window, text="x^2", width=11, height=3, bg=gray, font="Roboto 8 bold", relief=RAISED, overrelief=RIDGE)
b_sqr.place(x=182, y=71)
b_raise = Button(body_window, text="x^y", width=11, height=3, bg=gray, font="Roboto 8 bold", relief=RAISED, overrelief=RIDGE)
b_raise.place(x=272, y=71)
b_sin = Button(body_window, text="sin", width=11, height=3, bg=gray, font="Roboto 8 bold", relief=RAISED, overrelief=RIDGE)
b_sin.place(x=2, y=0)
b_cos = Button(body_window, text="cos", width=11, height=3, bg=gray, font="Roboto 8 bold", relief=RAISED, overrelief=RIDGE)
b_cos.place(x=92, y=0)
b_tan = Button(body_window, text="tan", width=11, height=3, bg=gray, font="Roboto 8 bold", relief=RAISED, overrelief=RIDGE)
b_tan.place(x=182, y=0)
b_mod = Button(body_window, text="mod", width=11, height=3, bg=gray, font="Roboto 8 bold", relief=RAISED, overrelief=RIDGE)
b_mod.place(x=272, y=0)



window.mainloop()