from tkinter import *
from sys import *

def submit():
    input = text.get('1.0',END)
    print(input)
root = Tk()
text = Text(root)
text.pack()
with open('test.txt') as file:
    text.insert('1.0',file)
button = Button(root,text='SAVE',command=submit)
button.pack()
root.mainloop()