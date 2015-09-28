import os
from time import sleep
import Tkinter

__author__ = 'weixy6'


class DirList(object):
    def __init__(self, initdir=None):
        self.top = Tkinter.Tk()

        self.label = Tkinter.Label(self.top, text='Directory Lister v1.1')
        self.label.pack()

        self.cwd = Tkinter.StringVar(self.top)

        self.dir1 = Tkinter.Label(self.top, fg='blue', font=('Courier_New', 12, 'bold'))
        self.dir1.pack()

        self.dirfm = Tkinter.Frame(self.top)
        self.dirsb = Tkinter.Scrollbar(self.dirfm)
        self.dirsb.pack(side=Tkinter.RIGHT, fill=Tkinter.Y)
        self.dirs = Tkinter.Listbox(self.dirfm, height=15,
                                    width=50, yscrollcommand=self.dirsb.set)
        self.dirs.bind('<Double-1>', self.setDirAndGo)
        self.dirsb.config(command=self.dirs.yview)
        self.dirs.pack(side=Tkinter.LEFT, fill=Tkinter.BOTH)
        self.dirfm.pack()

        self.dirn = Tkinter.Entry(self.top, width=50, textvariable=self.cwd)
        self.dirn.bind('<Return>', self.doLS)
        self.dirn.pack()

        self.bfm = Tkinter.Frame(self.top)
        self.clr = Tkinter.Button(self.bfm, text='Clear', command=self.clrDir,
                                  activeforeground='white', activebackground='blue')
        self.ls = Tkinter.Button(self.bfm, text='List Directory', command=self.doLS,
                                 activeforeground='white', activebackground='green')
        self.quit = Tkinter.Button(self.bfm, text='Quit', command=self.top.quit,
                                   activeforeground='white', activebackground='red')
        self.clr.pack(side=Tkinter.LEFT)
        self.ls.pack(side=Tkinter.LEFT)
        self.quit.pack(side=Tkinter.LEFT)
        self.bfm.pack()

        if initdir:
            self.cwd.set(os.curdir)
            self.doLS()

    def clrDir(self, ev=None):
        self.cwd.set('')

    def setDirAndGo(self, ev=None):
        self.last = self.cwd.get()
        self.dirs.config(selectbackground='red')
        check = self.dirs.get(self.dirs.curselection())
        if not check:
            check = os.curdir
        self.cwd.set(check)
        self.doLS()

    def doLS(self, ev=None):
        error = ''
        tdir = self.cwd.get()
        if not tdir:
            tdir = os.curdir
        if not os.path.exists(tdir):
            error = tdir + ': no such file'
        elif not os.path.isdir(tdir):
            error = tdir + ': no such directory'

        if error:
            self.cwd.set(error)
            self.top.update()
            sleep(2)
            if not (hasattr(self, 'last') and self.last):
                self.last = os.curdir
            self.cwd.set(self.last)
            self.dirs.config(selectbackground='LightSkyBlue')
            self.top.update()
            return
        self.cwd.set('FETCHING DIRECTORY CONTENTS...')
        self.top.update()
        dirlist = os.listdir(tdir)
        dirlist.sort()
        os.chdir(tdir)
        self.dir1.config(text=os.getcwd())
        self.dirs.delete(0, Tkinter.END)
        self.dirs.insert(Tkinter.END, os.curdir)
        self.dirs.insert(Tkinter.END, os.pardir)
        for eachFile in dirlist:
            self.dirs.insert(Tkinter.END, eachFile)
        self.cwd.set(os.curdir)
        self.dirs.config(selectbackground='LightSkyBlue')


def main():
    d = DirList(os.curdir)
    Tkinter.mainloop()


if __name__ == '__main__':
    main()
