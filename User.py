from tkinter import *
from tkinter import ttk, messagebox
import os
import sqlite3
from middleware import Middleware

class Users:
    def __init__(self, root):
        self.window = root
        self.window.title("User")
        self.window.geometry("1350x800+0+0")
        self.window.config(bg = "white")
        root.resizable(False, False)
        lbtitle=Label(text="Drug Store Purchase",bd=3, relief=FLAT, bg='Black', fg="white", font=("MS UI Gothic", 30, "bold"), padx=2, pady=4)
        lbtitle.pack(side=TOP, fill=X)



        self.ref_variable = StringVar()
        self.addmed_variable = StringVar()
        self.companyname_var = StringVar()
        self.typemed_var = StringVar()
        self.medicine_var = StringVar()
        self.lotno_var = StringVar()
        self.price_var = StringVar()
        self.quantity_var = StringVar()
        self.Costprice_var = StringVar()

        self.search_by = StringVar()
        self.search_txt = StringVar()
        self.searc_name = StringVar()
        self.total_bill = StringVar()

        self.total_price = 0
        self.count = 0
        self.profit = 0
        self.sold_quant = 0

        topframe = Frame(bg='#A01505', bd=3, relief=SUNKEN, padx=20)
        topframe.place(x=0, y=62, width=1350, height=370)

        left_smallframe = LabelFrame(topframe, bg='#05171C', bd=10, relief=FLAT,
                                     padx=20, text="Medicine Information", font=("MS UI Gothic", 20, "bold") ,fg="white")
        left_smallframe.place(x=0, y=5, width=820, height=350)


        right_frame = LabelFrame(topframe, bg='#1f4f60', bd=10, relief=FLAT, padx=5,
                                 text="Billing", font=("MS UI Gothic", 20, "bold"), fg="#36A3C3")
        right_frame.place(x=846, y=5, width=452, height=350)

        down_buttonframe = Frame(
            bg='#05171C', bd=10, relief=RIDGE, padx=20)
        down_buttonframe.place(x=0, y=432, width=1350, height=60)

        search_by = Label(down_buttonframe, text="Search By", font=(
            "arial", 15, "bold"), fg="white", bg="#05171C", bd=3, padx=3, pady=2)
        search_by.grid(row=0, column=5, sticky=W)

        self.search_combo = ttk.Combobox(down_buttonframe, width=12, font=(
            "arial", 13, "bold"), state="readonly", textvariable=self.search_by)
        self.search_combo["values"] = ("Select Options", "Name ", "ID ")
        self.search_combo.grid(row=0, column=6)
        self.search_combo.current(0)

        blank_label4 = Label(down_buttonframe, text=".............", padx=2, pady=4, font=(
            "Ubuntu", 2, "bold"), bg="#05171C", fg="#05171C")
        blank_label4.grid(row=0, column=7, sticky=W)

        entry_button = Entry(down_buttonframe, font=("Monoton", 15, "bold"), fg="black",
                             bg="#FFECEC", bd=3, width=15, relief=RIDGE, textvariable=self.search_txt)
        entry_button.grid(row=0, column=8)

        blank_label5 = Label(down_buttonframe, text=".............", padx=2, pady=4, font=(
            "Ubuntu", 2, "bold"), bg="#05171C", fg="#05171C")
        blank_label5.grid(row=0, column=10, sticky=W)

        search_button = Button(down_buttonframe, command=self.search_data, text="Search by Id", font=("Monoton", 13, "bold"), width=14, fg="white", bg="black",
                               bd=3, relief=RIDGE, activebackground="black", activeforeground="white")
        search_button.grid(row=0, column=11)

        blank_label3 = Label(down_buttonframe, text=".............", padx=2, pady=4, font=(
            "Ubuntu", 2, "bold"), bg="#05171C", fg="#05171C")
        blank_label3.grid(row=0, column=12, sticky=W)

        search_button_name = Button(down_buttonframe, command=self.search_data_Name, text="Search by Name", font=("Monoton", 13, "bold"), width=15, fg="white", bg="black",
                               bd=3, relief=RIDGE, activebackground="black", activeforeground="white")
        search_button_name.grid(row=0, column=13)





        medname_label = Label(left_smallframe, text="Name of medicine", padx=2, pady=4, font=(
            "Ubuntu", 13, "bold"), bg="#051723", fg="white")
        medname_label.grid(row=3, column=0, sticky=W)
        self.med_entry = Entry(left_smallframe, width=24, font=(
            "Ubuntu", 13, "bold"),  textvariable=self.addmed_variable, fg="black", bg="white")
        self.med_entry.grid(row=3, column=1)


        lot_label = Label(left_smallframe, text="Product ID", padx=2, pady=4, font=(
            "Ubuntu", 13, "bold"), bg="#051723", fg="white")
        lot_label.grid(row=3, column=2, sticky=W)
        self.lot_entry = Entry(left_smallframe, width=24, textvariable=self.ref_variable, font=(
            "Khmer UI", 13, "bold"), fg="black", bg="white")
        self.lot_entry.grid(row=3, column=3)



        add_button = Button(left_smallframe, text="Show medicines", font=(
            "Lucida Sans", 12, "bold"), command=self.fetch_new, width=14, fg="white", bg="black", bd=3, relief=FLAT, activebackground="black", activeforeground="white")
        add_button.grid(row=5, column=0)

        blank_label2 = Label(left_smallframe, text=".............", padx=2, pady=4, font=(
            "Ubuntu", 20, "bold"), bg="#05171C", fg="#05171C")
        blank_label2.grid(row=6, column=0, sticky=W)

        update_button = Button(left_smallframe, text="Click to Buy(1 per click)", font=(
            "Lucida Sans", 13, "bold"), width=20, command=self.buy, fg="white", bg="black", bd=3, relief=FLAT, activebackground="black", activeforeground="white")
        update_button.grid(row=7, column=0)

        blank_label2 = Label(left_smallframe, text=".............", padx=2, pady=4, font=(
            "Ubuntu", 20, "bold"), bg="#05171C", fg="#05171C")
        blank_label2.grid(row=8, column=0, sticky=W)

        exit_button = Button(left_smallframe, command=self.logout, text="Log Out", font=(
            "Lucida Sans", 13, "bold"), width=10, fg="white", bg="#E0270C", bd=3, relief=FLAT, activebackground="black", activeforeground="white")
        exit_button.grid(row=9, column=0)

        total_label = Label(right_frame, text="Total Bill in PKR", padx=2, pady=4, font=(
            "Ubuntu", 13, "bold"), bg="#051723", fg="white")
        total_label.grid(row=1, column=0, sticky=W)

        blank_label7 = Label(right_frame, text="...", padx=2, pady=4, font=(
            "Ubuntu", 20, "bold"), bg="#1f4f60", fg="#1f4f60")
        blank_label7.grid(row=1, column=1, sticky=W)

        self.total_entry = Entry(right_frame, width=24, textvariable=self.total_bill, font=(
            "Ubuntu", 13, "bold"), fg="black", bg="white")
        self.total_entry.grid(row=1, column=2)

        blank_label6 = Label(right_frame, text=".............", padx=2, pady=4, font=(
            "Ubuntu", 20, "bold"), bg="#1f4f60", fg="#1f4f60")
        blank_label6.grid(row=2, column=0, sticky=W)

        finalBill_button = Button(right_frame, text="Finalise Bill", command=self.finalise ,font=(
            "Lucida Sans", 13, "bold"), width=10, fg="white", bg="violet", bd=3, relief=FLAT, activebackground="black", activeforeground="white")
        finalBill_button.grid(row=3, column=0)


        down_frame = Frame(bg='#D61818', bd=10, relief=GROOVE)
        down_frame.place(x=0, y=500, width=1350, height=232)

        scroll_frame = Frame(down_frame, bd=2, relief=RIDGE, bg="#D61818")
        scroll_frame.place(x=0, y=0, width=1330, height=215)

        scroll_x = ttk.Scrollbar(scroll_frame, orient=HORIZONTAL)
        scroll_y = ttk.Scrollbar(scroll_frame, orient=VERTICAL)
        self.info_table = ttk.Treeview(scroll_frame, column=("Product ID", "Medicine name", "Price", "Quantity", "Company name", "Type"), xscrollcommand=scroll_x.set, yscrollcommand=scroll_y.set)

        scroll_x.pack(side=BOTTOM, fill=X)
        scroll_y.pack(side=RIGHT, fill=Y)

        scroll_x.config(command=self.info_table.xview)
        scroll_y.config(command=self.info_table.yview)

        self.info_table.heading("Product ID", text="Product ID")
        self.info_table.heading("Company name", text="Company Name")
        self.info_table.heading("Type", text="Type Of Medicine")
        self.info_table.heading("Medicine name", text="Medicine Name")
        self.info_table.heading("Price", text="Price")
        self.info_table.heading("Quantity", text="Quantity")

        self.info_table["show"] = "headings"
        self.info_table.pack(fill=BOTH, expand=1)

        self.info_table.column("Product ID", width=100)
        self.info_table.column("Company name", width=100)
        self.info_table.column("Type", width=100)
        self.info_table.column("Medicine name", width=100)
        self.info_table.column("Price", width=100)
        self.info_table.column("Quantity", width=100)

    def Get_billID(self):
        conn = sqlite3.connect(database=r'C:\Users\usama\Desktop\DrugStores\drugs.db')
        new_cursor = conn.cursor()
        new_cursor.execute("Select * from Bill")
        row=new_cursor.fetchall()
        billID=row[0][0]
        conn.close()
        return billID
    
    def get_profit(self):
        print(int(self.price_var.get()))
        print(int(self.quantity_var.get()))
        print(int(self.Costprice_var.get()))
        print(self.profit)
        
        self.profit=(int(self.price_var.get())*int(self.quantity_var.get()))-(int(self.Costprice_var.get())*int(self.quantity_var.get()))+int(self.profit)

    def Billing(self):
        conn = sqlite3.connect(database=r'C:\Users\usama\Desktop\DrugStores\drugs.db')
        my_cursor = conn.cursor()
        #self.get_profit()
        my_cursor.execute("Insert into Bill(Price, Prod) values(?, ?)", (
            int(self.total_price),
            int(self.ref_variable.get())))

        conn.commit()
        conn.close()
        


    def buy(self):
        conn=sqlite3.connect(database=r'C:\Users\usama\Desktop\DrugStores\drugs.db')
        new_cursor=conn.cursor()
        new_cursor.execute("Select * from Medicines where PROD_ID=?",(int(self.ref_variable.get()),))
        row=new_cursor.fetchall()
        conn.commit()
        price1 = row[0][2]
        quant= row[0][3]
        cost= row[0][6]
        if quant>1:
            newquant=quant-1
            new_cursor=conn.cursor()
            new_cursor.execute("Update Medicines set Quantity=? where PROD_ID=?",(
            newquant,
            int(self.ref_variable.get())))
            self.total_price=self.total_price+price1
            self.total_bill.set(self.total_price)
            self.sold_quant+=1
        
            self.profit=(price1-cost)+int(self.profit)

            conn.commit()
            self.count+=1
            self.Billing()
        else:
            messagebox.showinfo("Error","Not in stock")   


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

    def finalise(self):
        print()
        conn = sqlite3.connect(database=r'C:\Users\usama\Desktop\DrugStores\drugs.db')
        
        #print('with get ', self.ref_variable.get())
        new_cursor=conn.cursor()
        new_cursor.execute("Select * from Medicines where PROD_ID=?",(int(self.ref_variable.get()),))
        row=new_cursor.fetchall()
        conn.commit()
        price1 = row[0][2]
        quant= row[0][3]
        cost= row[0][6]
        my_cursor = conn.cursor()
        my_cursor.execute("Insert into Sales(prod, price, quantity, total, profit) values(?, ?, ?, ?, ?)", (
            int(self.ref_variable.get()),
            price1,
            int(self.sold_quant),
            int(self.total_price),
            int(self.profit)
            ))

        conn.commit()
        conn.close()
    
    def logout(self):
        self.window.quit()

if __name__ == "__main__":
    root=Tk()
    obj=Users(root)
    root.mainloop()