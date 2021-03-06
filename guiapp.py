import tkinter as tk
from tkinter import ttk
import os
import sys

sys.path.append(os.path.abspath("./frame"))

from startframe import StartFrame

import threading


class GUIAPP(tk.Tk):
    def __init__(self):
        tk.Tk.__init__(self)
        self.title("Crow Buster System")
        self.geometry("700x700")
        self.resizable(width = False,height = False)
        self.tk.call('tk','scaling',1.0)
        self.option_add("*TCombobox*Listbox.Font",("",13))
        self.s2 = ttk.Style()
        self.s2.theme_use('default')
        self.s2.configure("Release.TButton",font=("",13))
        self.s = ttk.Style()
        self.s.theme_use('default')
        self.style = ttk.Style()
        self.style.configure("Treeview",font=("",13))
        self.style.configure("Treeview.Heading",font=("",13))
        self.s.configure("Select.TButton",background='#87cefa',foreground='red',font=("",12,"bold"))
        self.start_frame = StartFrame(self)
        self.start_frame.pack()
    
    def GUIStart(self):
        self.mainloop()


if __name__ == "__main__":
    app = GUIAPP()
    app.GUIStart()
    