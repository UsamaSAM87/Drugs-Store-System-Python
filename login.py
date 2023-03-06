from tkinter import*
from tkinter import ttk, messagebox
from main import DrugStore
from User import Users
import os
import sqlite3

class login_page:
    def __init__(self, root):
        self.window = root
        self.window.title("Log In Drugs Portal")
        root.eval('tk::PlaceWindow . center')

        self.window.geometry("1200x700+70+0")
        self.window.config(bg = "white")

        self.username_entry = StringVar()
        self.password_entry = StringVar()

        self.frame1 = Frame(self.window, bg="#07092B")
        self.frame1.place(x=0, y=0, width=400, relheight = 1)

        label1 = Label(self.frame1, text= "Drugs", \
        font=("Lucida Sans", 30, "bold"), bg="#07092B", \
        fg="white").place(x=68,y=300)
        
        label2 = Label(self.frame1, text= "Store", \
        font=("Lucida Sans", 30, "bold"), bg="#07092B", \
        fg="white").place(x=204,y=300)
        
        label3 = Label(self.frame1, text= "Your Store Management Portal", \
        font=("Lucida Sans", 13, "bold"), bg="#07092B", \
        fg="white").place(x=68,y=360)

        self.frame2 = Frame(self.window, bg = "#520614")
        self.frame2.place(x=400,y=0,relwidth=1, relheight=1)

        self.frame3 = Frame(self.frame2, bg="white")
        self.frame3.place(x=140,y=150,width=400,height=450)

        self.email_label = Label(self.frame3,text="Username", \
        font=("Lucida Sans",20, "bold"),bg="white", \
        fg="black").place(x=50,y=40)
        
        self.email_entry = Entry(self.frame3,\
        textvariable=self.username_entry,\
        font=("Ubuntu",15),bg="white",fg="gray")
        self.email_entry.place(x=50, y=80, width=300)

        self.password_label = Label(self.frame3,text="Password", \
        font=("Lucida Sans",20,"bold"),bg="white", \
        fg="black").place(x=50,y=120)
        
        self.password_entry = Entry(self.frame3,\
        textvariable=self.password_entry,\
        font=("Ubuntu",15),bg="white",\
        fg="gray",show="*")
        
        self.password_entry.place(x=50, y=160, width=300)

        self.login_button = Button(self.frame3,text="Log In as User",\
        command=self.login,\
        font=("Lucida Sans",15, "bold"),\
        bd=0,cursor="hand2",bg="#06604F",\
        fg="white").place(x=50,y=200,width=300)

        self.login_button = Button(self.frame3,text="Log In as Admin",\
        command=self.login_admin,\
        font=("Lucida Sans",15, "bold"),\
        bd=0,cursor="hand2",bg="#D67A18",\
        fg="white").place(x=50,y=240,width=300)


    def redirect_window(self):
        self.window.destroy()
        root = Tk()
        obj = DrugStore(root)
        root.mainloop()

    def redirect_window3(self):
        self.window.destroy()
        root = Tk()
        obj76 = Users(root)
        root.mainloop()

    def login(self):
        conn=sqlite3.connect(database=r'C:\Users\usama\Desktop\DrugStores\drugs.db')
        c = conn.cursor()

        c.execute('SELECT * FROM User WHERE user = ? AND password = ?', (
            self.username_entry.get(), 
            self.password_entry.get()))
        user = c.fetchone()

        conn.close()

        if user:
            messagebox.showinfo("Success", "User Found")
            self.redirect_window3()
        else:
            messagebox.showinfo("Error", "User not Found")

    def login_admin(self):
        conn=sqlite3.connect(database=r'C:\Users\usama\Desktop\DrugStores\drugs.db')
        c = conn.cursor()

        c.execute('SELECT * FROM Admins WHERE user = ? AND password = ?', (
            self.username_entry.get(), 
            self.password_entry.get()))
        user = c.fetchone()

        conn.close()

        if user:
            messagebox.showinfo("Success", "User Found")
            self.redirect_window()
        else:
            messagebox.showinfo("Error", "User not Found")

if __name__ == "__main__":
    root = Tk()
    obj = login_page(root)
    root.mainloop()