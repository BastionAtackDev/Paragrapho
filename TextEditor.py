from tkinter import *
from tkinter import filedialog

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
root.title("Text Editor")
save = Button(root,text='SAVE',command=submit)
save.pack(side="top")
openbutton = Button(root,text="Open",command=getFile)
openbutton.pack()
text = Text(root)
text.pack()
#with open('test.txt') as file:
#    text.insert('1.0',file)
root.mainloop()