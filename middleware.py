from tkinter import *
from tkinter import ttk, messagebox
import os
#from login import login_page
#from User import Users

class Middleware:
    def __init__(self, root):
        self.window = root
        self.window.title("Redirecting...")
        self.window.geometry("1280x800+0+0")
        self.window.config(bg = "white")

        #self.window.destroy()
        #root = Tk()
        #obj = Users(root)
        #root.mainloop()

if __name__ == "__main__":
    root = Tk()
    obj = Middleware(root)
    root.mainloop()