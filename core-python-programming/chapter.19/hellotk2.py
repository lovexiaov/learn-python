from Tkinter import *

__author__ = 'weixy6'

def resize(ev=None):
    label.config(font='Courier_New -%d bold' % scale.get())
    pass

top = Tk()
# widthxheight+x+y
top.geometry('450x350+300+300')

label = Label(top, text='Hello World!', font='Courier_New')
label.pack(fill=Y, expand=1)

scale = Scale(top, from_=10, to=40, orient=HORIZONTAL, command=resize)
scale.set(12)
scale.pack(fill=X, expand=5)

quitapp = Button(top, text='QUIT', command=top.quit, activeforeground='white', activebackground='red')
quitapp.pack()

mainloop()

