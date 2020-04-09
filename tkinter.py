# -*- coding: utf-8 -*-
"""
Created on Thu Dec 26 23:49:27 2019

@author: Bagavathi Priya
"""

import tkinter as tk

win=tk.Tk()
def clicked():
    label.configure(text="Button was clicked")
    
def entry():
    res="The text entered was"+txt.get()
    label.configure(text=res)
    
label=tk.Label(win,text="Hello Priya",font=("Arial Bold",25))
label.grid(column=4,row=1)
txt=tk.Entry(win,width=10)
txt.grid(column=4,row=3)

'''from tkinter.ttk import *
win=tk.Tk()
combo = Combobox(win)
combo['values']= (1, 2, 3, 4, 5, "Text")
combo.current(3)
combo.grid(column=0, row=0)
'''



bt=tk.Button(win,text="Click me",bg="black",fg="white",command=entry)
bt.grid(column=4,row=4)
win.mainloop()



