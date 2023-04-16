# -*- coding: utf-8 -*-
"""
Created on Sat May  7 21:21:36 2022

@author: 91965
"""

from tkinter import *
from tkinter import ttk
from ttkthemes import ThemedTk

wind =  ThemedTk(theme = 'plastik')
wind.geometry("800x600")
style = ttk.Style(wind)
style.configure('Tentry', foreground = 'Red')

num1 = IntVar()
num2 = IntVar()
sumnums = StringVar()
sumnum = StringVar()
from operator import mul

def sum_of_num():
    sumnum = int(num1.get()) + int(num2.get())
    sumnums.set(sumnum)
    
def difference_of_num():
    sumnum = int(num1.get()) - int(num2.get())
    sumnums.set(sumnum)
    
def multi_of_num():
    sumnum = (int(num1.get())) * (int(num2.get()))
    print(sumnum)
    sumnums.set(sumnum)
    
def division_of_num():
    sumnum = (int(num1.get())) / (int(num2.get()))
    sumnums.set(sumnum)
    
def comparison():
    if (int(num1.get())) < (int(num2.get())):
        # comparison = str((int(num1.get())) < (int(num2.get())))
        sumnums.set("2nd number is greater")
    elif (int(num1.get())) > (int(num2.get())):
        # comparison = str((int(num1.get())) > (int(num2.get())))
        sumnums.set("First number is greater")
    else:
        # comparison = str((int(num1.get())) = (int(num2.get())))
        sumnums.set("both numbers are equal")
        
def exit_the_window():
    wind.destroy()
    
label1 = Label(wind, text = "Enter the 1st number")
label1.place(x = 10, y = 45)
label1 = Entry(wind, width = 30, textvariable = num1)
label1.place(x = 150, y = 45)

label2 = Label(wind, text = "Enter the 2nd number")
label2.place(x = 10, y = 90)
label2 = Entry(wind, width = 30, textvariable = num2)
label2.place(x = 150, y = 90)

Button1 = Button(wind, text = "Sum", command = sum_of_num)
Button1.place(x = 350, y = 45)
Button2 = Button(wind, text = "Difference", command = difference_of_num)
Button2.place(x = 450, y = 45)

Button3 = Button(wind, text = "Multiply", command = multi_of_num)
Button3.place(x = 350, y = 90)
Button4 = Button(wind, text = "Divide", command = division_of_num)
Button4.place(x = 450, y = 90)

Button4 = Button(wind, text = "Comparator", command = comparison)
Button4.place(x = 550, y = 45)

label3 = Label(wind, text = "Result")
label3.place(x = 10, y = 135)
label3 = Entry(wind, width = 30, textvariable  = sumnums)
label3.place(x = 150, y = 135)

Button4 = Button(wind, text = "Exit", command = exit_the_window)
Button4.place(x = 350, y = 135)

wind.mainloop()
