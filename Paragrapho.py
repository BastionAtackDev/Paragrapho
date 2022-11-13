from tkinter import *
from tkinter import filedialog
import keyboard

#from sys import *

def submit():
    file = filedialog.asksaveasfile(defaultextension='.txt',
                                    filetypes=[
                                        ("All files",".*")
                                    ])
    input = text.get('1.0',END)
    file.write(input)
    file.close()

def getFile():
    path = filedialog.askopenfilename()
    file = open(path,'rt')
    text.insert('1.0',file.read())
    file.close()
root = Tk()
root.geometry('400x400')
root.title("Paragrapho")
img=PhotoImage(file="D:\\Sebastian\\Programare\\Cpp,Python,C#\Python\\TextEditor-main\\TextEditor-main\\Paragrapho.png")
root.iconphoto(False,img)
save = Button(root,text='Save',command=submit)
save.place(x=0,y=0)
openbutton = Button(root,text="Open",command=getFile)
openbutton.place(x=40,y=0)
text = Text(root)
text.place(x=0,y=25)
#with open('test.txt') as file:
#    text.insert('1.0',file)

root.mainloop()
