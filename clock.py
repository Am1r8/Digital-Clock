from tkinter import *
from tkinter.ttk import *
from time import strftime

root = Tk()
root.title("Digital Clock")

label = Label(root, font=("ds-digital", 70), background = "black", foreground = "lightgreen")
label.pack(anchor = 'center')

def time():
  string = strftime('%H:%M:%S %p')
  label.config(text=string)
  label.after(1000, time)
  
time()
mainloop()