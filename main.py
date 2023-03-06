from tkinter import *
from tkinter import ttk, messagebox
import sqlite3
import csv
from datetime import date, datetime
from signup import SignUp
from signup_admin import SignUpAdmin


class DrugStore:
    def __init__(self, root):
        self.root = root
        self.root.title("DrugStore")
        self.root.geometry("1350x800+0+0")
        self.root.resizable(False, False)
        lbtitle=Label(self.root, text="Drug Store Inventory",bd=3, relief=FLAT, bg='Black', fg="white", font=("MS UI Gothic", 30, "bold"), padx=2, pady=4)
        lbtitle.pack(side=TOP, fill=X)

        
        self.ref_variable = StringVar()
        self.addmed_variable = StringVar()
        self.companyname_var = StringVar()
        self.typemed_var = StringVar()
        self.medicine_var = StringVar()
        self.lotno_var = StringVar()
        self.price_var = StringVar()
        self.Costprice_var = StringVar()
        self.quantity_var = StringVar()
        self.expdt_var = StringVar()

        self.search_by = StringVar()
        self.search_txt = StringVar()
        self.searc_name= StringVar()



        topframe = Frame(self.root, bg='#A01505', bd=3, relief=SUNKEN, padx=20)
        topframe.place(x=0, y=62, width=1350, height=370)

        left_smallframe = LabelFrame(topframe, bg='#05171C', bd=10, relief=FLAT,
                                     padx=20, text="Medicine Information", font=("MS UI Gothic", 20, "bold") ,fg="white")
        left_smallframe.place(x=0, y=5, width=820, height=350)

        right_frame = LabelFrame(topframe, bg='#1f4f60', bd=10, relief=FLAT, padx=5,
                                 text="Admin Panel", font=("MS UI Gothic", 20, "bold"), fg="#36A3C3")
        right_frame.place(x=846, y=5, width=452, height=350)

        down_buttonframe = Frame(
            self.root, bg='#A80808', bd=10, relief=GROOVE, padx=20)
        down_buttonframe.place(x=0, y=432, width=1350, height=60)

        newframe = Frame(right_frame, bg='#049058', bd=5, relief=RIDGE)
        newframe.place(x=20, y=30, width=382, height=265)

        blank_label87 = Label(left_smallframe, text=".............", padx=2, pady=4, font=(
            "Ubuntu", 2, "bold"), bg="#051723", fg="#051723")
        blank_label87.grid(row=7, column=0, sticky=W)
        blank_label88 = Label(left_smallframe, text=".............", padx=2, pady=4, font=(
            "Ubuntu", 2, "bold"), bg="#051723", fg="#051723")
        blank_label88.grid(row=8, column=0, sticky=W)
        blank_label89 = Label(left_smallframe, text=".............", padx=2, pady=4, font=(
            "Ubuntu", 2, "bold"), bg="#051723", fg="#051723")
        blank_label89.grid(row=9, column=0)

        add_button = Button(newframe, text="Add Medicine", font=(
            "Lucida Sans", 14, "bold"), command=self.AddMed, width=30, fg="white", bg="black", bd=3, relief=RIDGE, activebackground="black", activeforeground="white")
        add_button.grid(row=3, column=0)

        update_button = Button(newframe, text="Update", font=(
            "Lucida Sans", 14, "bold"), width=30, command=self.update_new, fg="white", bg="black", bd=3, relief=RIDGE, activebackground="black", activeforeground="white")
        update_button.grid(row=4, column=0)

        delete_button = Button(newframe, text="Delete", font=("Lucida Sans", 14, "bold"), width=30,
                               fg="white", bg="black", bd=3, relief=RIDGE, activebackground="black", activeforeground="white", command=self.Delete_med)
        delete_button.grid(row=5, column=0)

        reset_button = Button(left_smallframe, text="Reset", command=self.clear_new , font=("Lucida Sans", 13, "bold"), width=12,
                              fg="white", bg="black", bd=3, relief=FLAT, activebackground="black", activeforeground="white")
        reset_button.grid(row=10, column=0)

        exit_button = Button(left_smallframe, command=self.root.quit, text="Exit", font=(
            "Lucida Sans", 13, "bold"), width=10, fg="white", bg="#E0270C", bd=3, relief=FLAT, activebackground="black", activeforeground="white")
        exit_button.grid(row=10, column=2)

        search_by = Label(down_buttonframe, text="Search By", font=(
            "arial", 15, "bold"), fg="white", bg="#A80808", bd=3, padx=3)
        search_by.grid(row=0, column=5, sticky=W)

        self.search_combo = ttk.Combobox(down_buttonframe, width=12, font=(
            "arial", 13, "bold"), state="readonly", textvariable=self.search_by)
        self.search_combo["values"] = ("Select Options", "Name ", "ID ")
        self.search_combo.grid(row=0, column=6)
        self.search_combo.current(0)

        blank_label4 = Label(down_buttonframe, text=".............", padx=2, pady=4, font=(
            "Ubuntu", 2, "bold"), bg="#A80808", fg="#A80808")
        blank_label4.grid(row=0, column=7, sticky=W)

        entry_button = Entry(down_buttonframe, font=("Monoton", 15, "bold"), fg="black",
                             bg="#FFECEC", bd=3, width=15, relief=RIDGE, textvariable=self.search_txt)
        entry_button.grid(row=0, column=8)

        blank_label5 = Label(down_buttonframe, text=".............", padx=2, pady=4, font=(
            "Ubuntu", 2, "bold"), bg="#A80808", fg="#A80808")
        blank_label5.grid(row=0, column=10, sticky=W)

        search_button = Button(down_buttonframe, command=self.search_data, text="Search by Id", font=("Monoton", 13, "bold"), width=14, fg="white", bg="black",
                               bd=3, relief=RIDGE, activebackground="black", activeforeground="white")
        search_button.grid(row=0, column=11)

        blank_label3 = Label(down_buttonframe, text=".............", padx=2, pady=4, font=(
            "Ubuntu", 2, "bold"), bg="#A80808", fg="#A80808")
        blank_label3.grid(row=0, column=12, sticky=W)

        search_button_name = Button(down_buttonframe, command=self.search_data_Name, text="Search by Name", font=("Monoton", 13, "bold"), width=15, fg="white", bg="black",
                               bd=3, relief=RIDGE, activebackground="black", activeforeground="white")
        search_button_name.grid(row=0, column=13)

        show_button = Button(left_smallframe, text="Show All", command=self.fetch_new, font=("Lucida Sans", 13, "bold"), fg="white", bg="#2C6006",
                             width=10, bd=3, relief=FLAT, activebackground="black", activeforeground="white")
        show_button.grid(row=10, column=1)

        company_label = Label(left_smallframe, text="Company Name", padx=2, pady=4, font=(
            "Ubuntu", 13, "bold"), bg="#051723", fg="white")
        company_label.grid(row=1, column=0, sticky=W)

        self.company_entry = Entry(left_smallframe, width=24, textvariable=self.companyname_var, font=(
            "Ubuntu", 13, "bold"), fg="black", bg="white")
        self.company_entry.grid(row=1, column=1)

        type_label = Label(left_smallframe, text="Medicine Type", padx=2, pady=4, font=(
            "Ubuntu", 13, "bold"), bg="#051723", fg="white")
        type_label.grid(row=2, column=0, sticky=W)

        exp_label = Label(left_smallframe, text="Expiry Date ", padx=2, pady=4, font=(
            "Ubuntu", 13, "bold"), bg="#051723", fg="white")
        exp_label.grid(row=6, column=0, sticky=W)

        self.exp_entry = Entry(left_smallframe, textvariable=self.expdt_var, width=24, font=(
            "Ubuntu", 13, "bold"), fg="black", bg="white")
        self.exp_entry.grid(row=6, column=1)

        Costprice_label = Label(left_smallframe, text="Cost Price ", padx=2, pady=4, font=(
            "Ubuntu", 13, "bold"), bg="#051723", fg="white")
        Costprice_label.grid(row=6, column=2, sticky=W)

        self.Costprice_entry = Entry(left_smallframe, textvariable=self.Costprice_var, width=28, font=(
            "Ubuntu", 13, "bold"), fg="black", bg="white")
        self.Costprice_entry.grid(row=6, column=3)

        self.type_combo = ttk.Combobox(left_smallframe, width=22, textvariable=self.typemed_var, font=(
            "Ubuntu", 13, "bold"), state="readonly")
        self.type_combo["values"] = (
            " Select  ", "Tablet", "Capsule", "Injection", "Syrups")
        self.type_combo.grid(row=2, column=1)
        self.type_combo.current(0)

        medname_label = Label(left_smallframe, text="Name of medicine", padx=2, pady=4, font=(
            "Ubuntu", 13, "bold"), bg="#051723", fg="white")
        medname_label.grid(row=3, column=0, sticky=W)
        self.med_entry = Entry(left_smallframe, width=24, font=(
            "Ubuntu", 13, "bold"),  textvariable=self.addmed_variable, fg="black", bg="white")
        self.med_entry.grid(row=3, column=1)


        lot_label = Label(left_smallframe, text="Product ID", padx=2, pady=4, font=(
            "Ubuntu", 13, "bold"), bg="#051723", fg="white")
        lot_label.grid(row=3, column=2, sticky=W)
        self.lot_entry = Entry(left_smallframe, width=28, textvariable=self.ref_variable, font=(
            "Khmer UI", 13, "bold"), fg="black", bg="white")
        self.lot_entry.grid(row=3, column=3)

        price_label = Label(left_smallframe, text="Price", padx=2, pady=4, font=(
            "Ubuntu", 13, "bold"), bg="#051723", fg="white")
        price_label.grid(row=1, column=2, sticky=W)
        self.price_entry = Entry(left_smallframe, width=28, textvariable=self.price_var, font=(
            "Ubuntu", 13, "bold"), fg="black", bg="white")
        self.price_entry.grid(row=1, column=3)

        qt_label = Label(left_smallframe, text="Quantity", padx=2, pady=4, font=(
            "Ubuntu", 13, "bold"), bg="#051723", fg="white")
        qt_label.grid(row=2, column=2, sticky=W)
        self.qt_entry = Entry(left_smallframe, width=28, textvariable=self.quantity_var, font=(
            "Ubuntu", 13, "bold"), fg="black", bg="white")
        self.qt_entry.grid(row=2, column=3)

        

        add_button = Button(newframe, text="Generate Report", command=self.loss_calc, font=("Ubuntu", 15, "bold"), width=30, fg="white", bg="black",
                            bd=3, relief=RIDGE, activebackground="black", activeforeground="white")
        add_button.grid(row=0, column=0)

        updatenew_button = Button(newframe, text="Add User", command=self.redirect_window, font=("Ubuntu", 15, "bold"), width=30, fg="white", bg="black",
                                  bd=3, relief=RIDGE, activebackground="black", activeforeground="white")
        updatenew_button.grid(row=1, column=0)

        delnew_button = Button(newframe, text="Add Admin", font=("Ubuntu", 15, "bold"), command=self.redirect_window2, width=30, fg="white", bg="black",
                               bd=3, relief=RIDGE, activebackground="black", activeforeground="white")
        delnew_button.grid(row=2, column=0)

        down_frame = Frame(self.root, bg='#D61818', bd=10, relief=GROOVE)
        down_frame.place(x=0, y=500, width=1350, height=232)

        scroll_frame = Frame(down_frame, bd=2, relief=RIDGE, bg="#D61818")
        scroll_frame.place(x=0, y=0, width=1330, height=215)

        scroll_x = ttk.Scrollbar(scroll_frame, orient=HORIZONTAL)
        scroll_y = ttk.Scrollbar(scroll_frame, orient=VERTICAL)
        self.info_table = ttk.Treeview(scroll_frame, column=("Product ID", "Medicine name", "Price", "Quantity", "Company name", "Type", "CostPrice", "Expiry"), xscrollcommand=scroll_x.set, yscrollcommand=scroll_y.set)

        scroll_x.pack(side=BOTTOM, fill=X)
        scroll_y.pack(side=RIGHT, fill=Y)

        scroll_x.config(command=self.info_table.xview)
        scroll_y.config(command=self.info_table.yview)

        self.info_table.heading("Product ID", text="Product ID")
        self.info_table.heading("Medicine name", text="Medicine Name")
        self.info_table.heading("Type", text="Type Of Medicine")
        self.info_table.heading("Company name", text="Company Name")
        self.info_table.heading("Price", text="Price")
        self.info_table.heading("Quantity", text="Quantity")
        self.info_table.heading("CostPrice", text="Cost Price")
        self.info_table.heading("Expiry", text="Expiry Date")
        

        self.info_table["show"] = "headings"
        self.info_table.pack(fill=BOTH, expand=1)

        self.info_table.column("Product ID", width=100)
        self.info_table.column("Medicine name", width=100)
        self.info_table.column("Type", width=100)
        self.info_table.column("Company name", width=100)
        self.info_table.column("Price", width=100)
        self.info_table.column("Quantity", width=100)
        self.info_table.column("CostPrice", width=100)
        self.info_table.column("Expiry", width=100)
        

        self.fetch_new()



        ##############
        # backend 
    def AddMed(self):

        if self.ref_variable.get() == "" or self.addmed_variable.get() == "":
            messagebox.showerror("Error", "All fields are required")

        else:
            conn = sqlite3.connect(database=r'C:\Users\usama\Desktop\DrugStores\drugs.db')
            my_cursor = conn.cursor()
            my_cursor.execute("Insert into Medicines(PROD_ID,Name,Price,Quantity,Company,Type,CostPrice,Expiry) values(?,?,?,?,?,?,?,?)", (
                int(self.ref_variable.get()),
                self.addmed_variable.get(),
                int(self.price_var.get()),
                int(self.quantity_var.get()),
                self.companyname_var.get(),
                self.typemed_var.get(),
                int(self.Costprice_var.get()),
                self.expdt_var.get()))

            conn.commit()
            self.fetch_new()
            conn.close()

            messagebox.showinfo("Success", "MEDICINE ADDED")

    def fetch_datamed(self):
        conn = sqlite3.connect(database=r'C:\Users\usama\Desktop\DrugStores\drugs.db')
        my_cursor = conn.cursor()
        my_cursor.execute("select * from Medicines")
        rows = my_cursor.fetchall()

        if len(rows) != 0:
            self.medicine_table.delete(*self.medicine_table.get_children())

            for i in rows:
                self.medicine_table.insert("", END, values=i)

            conn.commit()
            conn.close()

    def fetch_new(self):
        conn=sqlite3.connect(database=r'C:\Users\usama\Desktop\DrugStores\drugs.db')
        new_cursor=conn.cursor()
        new_cursor.execute("select * from Medicines")
        row=new_cursor.fetchall()


        if len(row)!=0:
            self.info_table.delete(*self.info_table.get_children())

            for i in row:
                self.info_table.insert("",END,values=i)

            conn.commit()
    def update_new(self):
        
        if self.typemed_var.get() == "":
            messagebox.showerror("Error","All fields are required")
        else:
            conn=sqlite3.connect(database=r'C:\Users\usama\Desktop\DrugStores\drugs.db')
            new_cursor=conn.cursor()
            new_cursor.execute("Update Medicines set Name=?,Price=?,Quantity=?,Company=?,Type=?,CostPrice=?,Expiry=? where PROD_ID=?",(
            self.addmed_variable.get(),                                                                              
            int(self.price_var.get()),
            int(self.quantity_var.get()),
            self.companyname_var.get(),
            self.typemed_var.get(),
            int(self.Costprice_var.get()),
            self.expdt_var.get(),
            int(self.ref_variable.get())
            ))
            conn.commit()
            self.fetch_new()
            messagebox.showinfo("Success","Successfully updated")

    def clear_new(self):
        self.ref_variable.set("")
        self.addmed_variable.set("")
        self.companyname_var.set("")
        self.typemed_var.set("Select")
        self.medicine_var.set("")
        self.lotno_var.set("")
        self.price_var.set("0")
        self.quantity_var.set("0")
        self.Costprice_var.set("0")
        self.expdt_var.set("")
        self.lotno_var.set("0")
    
    def search_data(self):
        conn=sqlite3.connect(database=r'C:\Users\usama\Desktop\DrugStores\drugs.db')
        new_cursor=conn.cursor()
        selected = self.search_by.get()
        if selected == "Select Options":
            messagebox.showerror("Error","You have to choose an option")
        else:
            new_cursor.execute("Select * from Medicines where PROD_ID=?",(int(self.search_txt.get()),))
            row=new_cursor.fetchall()
            

            if len(row)!=0:
                self.info_table.delete(*self.info_table.get_children())

                for i in row:
                    self.info_table.insert("",END,values=i)

                conn.commit()

    def search_data_Name(self):

        conn=sqlite3.connect(database=r'C:\Users\usama\Desktop\DrugStores\drugs.db')
        new_cursor=conn.cursor()
        selected = self.search_by.get()
        if selected == "Select Options":
            messagebox.showerror("Error","You have to choose an option")

        else:
            new_cursor.execute("Select * from Medicines where Name=?",(self.search_txt.get(),))
            row=new_cursor.fetchall()

            if len(row)!=0:
                self.info_table.delete(*self.info_table.get_children())

                for i in row:
                    self.info_table.insert("",END,values=i)

                conn.commit()

    def Delete_med(self):
        if self.ref_variable.get()=="":
            messagebox.showerror("Error","Ref no is required",parent=self.root)
        else:

            try:
                conn=sqlite3.connect(database=r'C:\Users\usama\Desktop\DrugStores\drugs.db')
                my_cursor=conn.cursor()
            
                my_cursor.execute("Delete from Medicines where PROD_ID=? ",(int(self.ref_variable.get()),))
                conn.commit()
                messagebox.showinfo("Delete","Successfully Deleted",parent=self.root)
                self.fetch_new()
            except Exception as e:
                messagebox.showerror("Error",f"Error due to:{str(e)}",parent=self.root)

    def loss_calc(self):

        conn=sqlite3.connect(database=r'C:\Users\usama\Desktop\DrugStores\drugs.db')
        new_cursor=conn.cursor()
        new_cursor.execute("select * from Medicines")
        row=new_cursor.fetchall()
        conn.commit()
        #conn.close()
        i=0
        while i<len(row):
            dt=row[i][7]
            quan=row[i][3]
            costt=row[i][6]
            idd=row[i][0]

            today = date.today()
            d1 = today.strftime("%d-%m-%Y")
            d3=datetime.strptime(d1, "%d-%m-%Y")
            dt2=datetime.strptime(dt, "%d-%m-%Y")
            diff=dt2-d3
            str_diff=str(diff)
            l= str_diff.split(" ", 2)
            int_l=int(l[0])
            if int_l<1:
                loss=quan*costt
                my_cursor = conn.cursor()
                my_cursor.execute("Insert into Loss(prod, exp, quan, cost, total) values(?, ?, ?, ?, ?)", (
                    idd,
                    dt,
                    quan,
                    costt,
                    loss
                ))

                conn.commit()
                #conn.close()
            i+=1
        cursor = conn.cursor()
        cursor.execute("select * from Sales;")
        with open("profit_report.csv", 'w',newline='') as csv_file: 
            csv_writer = csv.writer(csv_file)
            csv_writer.writerow([i[0] for i in cursor.description]) 
            csv_writer.writerows(cursor)
        cursor = conn.cursor()
        cursor.execute("select * from Loss;")
        with open("loss_report.csv", 'w',newline='') as csv_file: 
            csv_writer = csv.writer(csv_file)
            csv_writer.writerow([i[0] for i in cursor.description]) 
            csv_writer.writerows(cursor)
        conn.close()

        


    def redirect_window(self):
        self.root.destroy()
        root = Tk()
        obj2 = SignUp(root)
        root.mainloop()
    
    def redirect_window2(self):
        self.root.destroy()
        root = Tk()
        obj3 = SignUpAdmin(root)
        root.mainloop()

    
if __name__ == '__main__':

    root=Tk()
    obj=DrugStore(root)
    root.mainloop()
