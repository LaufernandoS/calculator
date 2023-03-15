# Importing libraries
import math
from tkinter import *

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
def input_values(event):
    # Keeping the changes at all_values
    global all_values
    # Storing the event
    all_values = all_values + str(event)
    # Values to the display
    if "^" in all_values:
        all_values.replace("**", "^")
        text_value.set(all_values)
    else:
        text_value.set(all_values)


# Function to calculate
def calculate():
    try:
        global all_values
        result = eval(all_values)
        text_value.set(result)
    except ZeroDivisionError:
        text_value.set("Error")


# Function to clear the display
def clean_display():
    global all_values
    all_values = ""
    text_value.set("")


# Trigonometric functions
def sin():
    global all_values
    value = math.sin(float(all_values))
    all_values = str(value)
    text_value.set(all_values)


def cos():
    global all_values
    value = math.cos(float(all_values))
    all_values = str(value)
    text_value.set(all_values)


def tan():
    global all_values
    value = math.tan(float(all_values))
    all_values = str(value)
    text_value.set(all_values)


# Creating label
text_value = StringVar()
app_label = Label(display_window, textvariable=text_value, width=16, height=2,
                  padx=7, relief=FLAT, anchor="e", justify=RIGHT,
                  font="calibri 30 bold", bg=dark_blue, fg=white)
app_label.place(x=0, y=0)

# Creating buttons
b_C = Button(body_window, command=clean_display, text="C", width=34, height=3, bg=green,
             font="bitter 10 bold", relief=RAISED, overrelief=RIDGE)
b_C.place(x=0, y=142)
b_0 = Button(body_window, command=lambda: input_values("0"), text="0", width=22, height=3,
             font="bitter 10 bold", relief=RAISED, overrelief=RIDGE)
b_0.place(x=0, y=426)
b_1 = Button(body_window, command=lambda: input_values("1"), text="1", width=10, height=3,
             font="bitter 10 bold", relief=RAISED, overrelief=RIDGE)
b_1.place(x=0, y=355)
b_2 = Button(body_window, command=lambda: input_values("2"), text="2", width=10, height=3,
             font="bitter 10 bold", relief=RAISED, overrelief=RIDGE)
b_2.place(x=90, y=355)
b_3 = Button(body_window, command=lambda: input_values("3"), text="3", width=10, height=3,
             font="bitter 10 bold", relief=RAISED, overrelief=RIDGE)
b_3.place(x=180, y=355)
b_4 = Button(body_window, command=lambda: input_values("4"), text="4", width=10, height=3,
             font="bitter 10 bold", relief=RAISED, overrelief=RIDGE)
b_4.place(x=0, y=284)
b_5 = Button(body_window, command=lambda: input_values("5"), text="5", width=10, height=3,
             font="bitter 10 bold", relief=RAISED, overrelief=RIDGE)
b_5.place(x=90, y=284)
b_6 = Button(body_window, command=lambda: input_values("6"), text="6", width=10, height=3,
             font="bitter 10 bold", relief=RAISED, overrelief=RIDGE)
b_6.place(x=180, y=284)
b_7 = Button(body_window, command=lambda: input_values("7"), text="7", width=10, height=3,
             font="bitter 10 bold", relief=RAISED, overrelief=RIDGE)
b_7.place(x=0, y=213)
b_8 = Button(body_window, command=lambda: input_values("8"), text="8", width=10, height=3,
             font="bitter 10 bold", relief=RAISED, overrelief=RIDGE)
b_8.place(x=90, y=213)
b_9 = Button(body_window, command=lambda: input_values("9"), text="9", width=10, height=3,
             font="bitter 10 bold", relief=RAISED, overrelief=RIDGE)
b_9.place(x=180, y=213)
b_dot = Button(body_window, command=lambda: input_values("."), text=".", width=10, height=3,
               font="bitter 10 bold", relief=RAISED, overrelief=RIDGE)
b_dot.place(x=180, y=426)
b_equals = Button(body_window, command=calculate, text="=", width=10, height=3, bg=light_green,
                  font="bitter 10 bold", relief=RAISED, overrelief=RIDGE)
b_equals.place(x=270, y=426)
b_plus = Button(body_window, command=lambda: input_values("+"), text="+", width=10, height=3, bg=light_green,
                font="bitter 10 bold", relief=RAISED, overrelief=RIDGE)
b_plus.place(x=270, y=355)
b_minus = Button(body_window, command=lambda: input_values("-"), text="-", width=10, height=3, bg=light_green,
                 font="bitter 10 bold", relief=RAISED, overrelief=RIDGE)
b_minus.place(x=270, y=284)
b_times = Button(body_window, command=lambda: input_values("*"), text="*", width=10, height=3, bg=light_green,
                 font="bitter 10 bold", relief=RAISED, overrelief=RIDGE)
b_times.place(x=270, y=213)
b_divide = Button(body_window, command=lambda: input_values("/"), text="/", width=10, height=3, bg=light_green,
                  font="bitter 10 bold", relief=RAISED, overrelief=RIDGE)
b_divide.place(x=270, y=142)
b_pi = Button(body_window, command=lambda: input_values("{}".format(str(format(math.pi, ".6f")))), text="pi", width=10,
              height=3, bg=gray,
              font="bitter 10 bold", relief=RAISED, overrelief=RIDGE)
b_pi.place(x=0, y=71)
b_e = Button(body_window, command=lambda: input_values("e"), text="e", width=10, height=3, bg=gray,
             font="bitter 10 bold", relief=RAISED, overrelief=RIDGE)
b_e.place(x=90, y=71)
b_sqr = Button(body_window, command=lambda: input_values("**2"), text="x^2", width=10, height=3, bg=gray,
               font="bitter 10 bold", relief=RAISED, overrelief=RIDGE)
b_sqr.place(x=180, y=71)
b_raise = Button(body_window, command=lambda: input_values("^"), text="x^y", width=10, height=3, bg=gray,
                 font="bitter 10 bold", relief=RAISED, overrelief=RIDGE)
b_raise.place(x=270, y=71)
b_sin = Button(body_window, command=sin, text="sin", width=10, height=3, bg=gray,
               font="bitter 10 bold", relief=RAISED, overrelief=RIDGE)
b_sin.place(x=0, y=0)
b_cos = Button(body_window, command=cos, text="cos", width=10, height=3, bg=gray,
               font="bitter 10 bold", relief=RAISED, overrelief=RIDGE)
b_cos.place(x=90, y=0)
b_tan = Button(body_window, command=tan, text="tan", width=10, height=3, bg=gray,
               font="bitter 10 bold", relief=RAISED, overrelief=RIDGE)
b_tan.place(x=180, y=0)
b_mod = Button(body_window, command=lambda: input_values("%"), text="mod", width=10, height=3, bg=gray,
               font="bitter 10 bold", relief=RAISED, overrelief=RIDGE)
b_mod.place(x=270, y=0)

window.mainloop()