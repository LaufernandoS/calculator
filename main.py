# Importing libraries
import math
from tkinter import *
from tkinter import ttk

# Define some colours
black, white, dark_blue, green, light_green, gray = "#000000", "#ffffff", "#06042b", "#077d21", "#83e864", "#adadad"

# Creating the calculator window
window = Tk()
window.iconbitmap("pi_icon.ico")
window.title("Calculator")
window.geometry("360x602")
window.config(bg=black)

# Split window into display and buttons
display_window = Frame(window, width=360, height=105, bg=dark_blue)
display_window.grid(row=0, column=0)

body_window = Frame(window, width=360, height=492)
body_window.grid(row=1, column=0)

# Variable to store all input values
all_values = ""
# Functions for the operations
def inputValues(event):
    # Keeping the changes at all_values
    global all_values
    # Storing the event
    all_values = all_values + str(event)
    result = eval("1")
    # Value to the display
    text_value.set(all_values)

# Creating label
text_value = StringVar()
app_label = Label(display_window, textvariable=text_value, width=16, height=2,
                  padx=7, relief=FLAT, anchor="e", justify=RIGHT,
                  font="calibri 30 bold", bg=dark_blue, fg=white)
app_label.place(x=0, y=0)

# Creating buttons
b_C = Button(body_window, text="C", width=34, height=3, bg=green, font="bitter 10 bold", relief=RAISED, overrelief=RIDGE)
b_C.place(x=0, y=142)
b_0 = Button(body_window, text="0", width=22, height=3, font="bitter 10 bold", relief=RAISED, overrelief=RIDGE)
b_0.place(x=0, y=426)
b_1 = Button(body_window, text="1", width=10, height=3, font="bitter 10 bold", relief=RAISED, overrelief=RIDGE)
b_1.place(x=0, y=355)
b_2 = Button(body_window, text="2", width=10, height=3, font="bitter 10 bold", relief=RAISED, overrelief=RIDGE)
b_2.place(x=90, y=355)
b_3 = Button(body_window, text="3", width=10, height=3, font="bitter 10 bold", relief=RAISED, overrelief=RIDGE)
b_3.place(x=180, y=355)
b_4 = Button(body_window, text="4", width=10, height=3, font="bitter 10 bold", relief=RAISED, overrelief=RIDGE)
b_4.place(x=0, y=284)
b_5 = Button(body_window, text="5", width=10, height=3, font="bitter 10 bold", relief=RAISED, overrelief=RIDGE)
b_5.place(x=90, y=284)
b_6 = Button(body_window, text="6", width=10, height=3, font="bitter 10 bold", relief=RAISED, overrelief=RIDGE)
b_6.place(x=180, y=284)
b_7 = Button(body_window, text="7", width=10, height=3, font="bitter 10 bold", relief=RAISED, overrelief=RIDGE)
b_7.place(x=0, y=213)
b_8 = Button(body_window, text="8", width=10, height=3, font="bitter 10 bold", relief=RAISED, overrelief=RIDGE)
b_8.place(x=90, y=213)
b_9 = Button(body_window, text="9", width=10, height=3, font="bitter 10 bold", relief=RAISED, overrelief=RIDGE)
b_9.place(x=180, y=213)
b_dot = Button(body_window, text=".", width=10, height=3, font="bitter 10 bold", relief=RAISED, overrelief=RIDGE)
b_dot.place(x=180, y=426)
b_equals = Button(body_window, text="=", width=10, height=3, bg=light_green, font="bitter 10 bold", relief=RAISED, overrelief=RIDGE)
b_equals.place(x=270, y=426)
b_plus = Button(body_window, text="+", width=10, height=3, bg=light_green, font="bitter 10 bold", relief=RAISED, overrelief=RIDGE)
b_plus.place(x=270, y=355)
b_minus = Button(body_window, text="-", width=10, height=3, bg=light_green, font="bitter 10 bold", relief=RAISED, overrelief=RIDGE)
b_minus.place(x=270, y=284)
b_times = Button(body_window, text="*", width=10, height=3, bg=light_green, font="bitter 10 bold", relief=RAISED, overrelief=RIDGE)
b_times.place(x=270, y=213)
b_divide = Button(body_window, text="/", width=10, height=3, bg=light_green, font="bitter 10 bold", relief=RAISED, overrelief=RIDGE)
b_divide.place(x=270, y=142)
b_pi = Button(body_window, text="pi", width=10, height=3, bg=gray, font="bitter 10 bold", relief=RAISED, overrelief=RIDGE)
b_pi.place(x=0, y=71)
b_e = Button(body_window, text="e", width=10, height=3, bg=gray, font="bitter 10 bold", relief=RAISED, overrelief=RIDGE)
b_e.place(x=90, y=71)
b_sqr = Button(body_window, text="x^2", width=10, height=3, bg=gray, font="bitter 10 bold", relief=RAISED, overrelief=RIDGE)
b_sqr.place(x=180, y=71)
b_raise = Button(body_window, text="x^y", width=10, height=3, bg=gray, font="bitter 10 bold", relief=RAISED, overrelief=RIDGE)
b_raise.place(x=270, y=71)
b_sin = Button(body_window, text="sin", width=10, height=3, bg=gray, font="bitter 10 bold", relief=RAISED, overrelief=RIDGE)
b_sin.place(x=0, y=0)
b_cos = Button(body_window, text="cos", width=10, height=3, bg=gray, font="bitter 10 bold", relief=RAISED, overrelief=RIDGE)
b_cos.place(x=90, y=0)
b_tan = Button(body_window, text="tan", width=10, height=3, bg=gray, font="bitter 10 bold", relief=RAISED, overrelief=RIDGE)
b_tan.place(x=180, y=0)
b_mod = Button(body_window, command=lambda: inputValues("%"), text="mod", width=10, height=3, bg=gray, font="bitter 10 bold", relief=RAISED, overrelief=RIDGE)
b_mod.place(x=270, y=0)



window.mainloop()