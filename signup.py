from tkinter import *
from tkinter import ttk, messagebox
import sqlite3
#import middleware

class SignUp:
    def __init__(self, root):
        self.window = root
        self.window.title("Sign Up")
        self.window.geometry("600x450+320+150")
        self.window.config(bg = "#02041E")
        

        self.user_var = StringVar()
        self.user_pass = StringVar()

        frame = Frame(self.window, bg="white")
        frame.place(x=50,y=60,width=500,height=350)

        title1 = Label(frame, text="Create user account", \
        font=("Lucida Sans",25,"bold"),bg="white")
        title1.place(x=10, y=10)

        email = Label(frame, text="UserName", font=("Lucida Sans",15,"bold"),\
        bg="white")
        email.place(x=20, y=70)

        self.email_txt = Entry(frame,font=("Ubuntu"), textvariable=self.user_var, fg="gray")
        self.email_txt.place(x=20, y=110, width=420)

        password =  Label(frame, text="Password", \
        font=("Lucida Sans",15,"bold"),bg="white").place(x=20, y=170)

        self.password_txt = Entry(frame,font=("Ubuntu"), textvariable=self.user_pass, fg="gray", show="*")
        self.password_txt.place(x=20, y=210, width=420)

        
        self.signup = Button(frame,text="Sign Up",\
        command=self.AddUser,\
        font=("Lucida Sans",18, "bold"),bd=0,cursor="hand2",bg="#2C6006",\
        fg="white").place(x=120,y=260,width=250)
    
    def AddUser(self):

        if self.user_var.get() == "" or self.user_pass.get() == "":
            messagebox.showerror("Error", "All fields are required")

        else:
            conn = sqlite3.connect(database=r'C:\Users\usama\Desktop\DrugStores\drugs.db')
            my_cursor = conn.cursor()
        
            my_cursor.execute("Insert into User(user, password) values(?,?)", (
                self.user_var.get(),
                self.user_pass.get()))

            conn.commit()
            conn.close()
            messagebox.showinfo("Success", "User ADDED")


    def redirect_middle(self):
        self.window.destroy()
        root = Tk()
        #obj3 = middleware.Middleware(root)
        root.mainloop()


if __name__ == "__main__":
    root = Tk()
    obj3 = SignUp(root)
    root.mainloop()