import Tkinter

__author__ = 'weixy6'

top = Tkinter.Tk()

lab = Tkinter.Label(top, text='Hello World!')
lab.pack()

quitapp = Tkinter.Button(top, text='QUIT', command=top.quit, bg='red', fg='white')
quitapp.pack(fill=Tkinter.X, expand=1)

Tkinter.mainloop()
