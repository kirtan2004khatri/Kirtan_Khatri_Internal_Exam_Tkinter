import os 
os.system('cls')

from tkinter import *
from tkinter import ttk
from tkinter import messagebox

root=Tk()
root.geometry("800x500")
root.resizable(0,0)

# Billing values
billing_list=[]

# for theme
theme_var=StringVar()
theme_var.set("teal")


# frame widget----------------------
input_frame=Frame(root,highlightbackground="blue",highlightthickness=0,padx=10)
button_frame=Frame(root,highlightbackground="red",highlightthickness=0,bg=theme_var.get())
billing_frame=Frame(root,highlightbackground="green",highlightthickness=0)
gender_frame=Frame(input_frame)
lang_frame=Frame(input_frame)
address_frame=Frame(input_frame)

# scrollbar
scroll=Scrollbar(address_frame,orient=VERTICAL)
scroll.pack(side=RIGHT,fill=Y)

# label widget--------------
first_name=Label(input_frame,text="First Name : ")
last_name=Label(input_frame,text="Last Name : ")
gender=Label(input_frame,text="Gender : ")
languages=Label(input_frame,text="Languages : ")
email=Label(input_frame,text="Email : ")
address=Label(input_frame,text="Address : ")
state=Label(input_frame,text="State : ")
zip=Label(input_frame,text="Zip : ")
card=Label(input_frame,text="Credit Card Type : ")
billing=Label(billing_frame,text="Billing Records",font=("Arial",15))

# Entry widget
finput=Entry(input_frame)
linput=Entry(input_frame)   
einput=Entry(input_frame)   
zinput=Entry(input_frame)

# Text widget------------------------
ainput=Text(address_frame,width=20,height=5,font=("",10),yscrollcommand=scroll.set)
scroll.config(command=ainput.yview)
ainput.pack()

# Data for combobox------------------
state_list=["Gujarat","Mumbai","Delhi","Pune","Himachal","Chennai","Kerala","Rajasthan"]
card_list=["ICICI","BOB","BOI","AMCO","PNB"]

# Combox widget-----------------------
sinput=ttk.Combobox(input_frame,values=state_list)
cinput=ttk.Combobox(input_frame,values=card_list)

# Button Functions
def change_theme():
    if(theme_var.get()=="teal"):
        theme_var.set("navy blue")
        root.config(bg=theme_var.get())
        button_frame.config(bg=theme_var.get())
    else:
        theme_var.set("teal")
        root.config(bg=theme_var.get())
        button_frame.config(bg=theme_var.get())
def insert_func():
    fname=finput.get()
    lname=linput.get()
    email=einput.get()
    zipcode=zinput.get()
    add=ainput.get(1.0,END)
    numbers=["1","2","3","4","5","6","7","8","9","0"]
    checked=True
    if(fname!="" and lname!="" and email!="" and gen.get()!="" and tvar!=0 and evar!=0 and hvar!=0 and add!="" and sinput.get()!="" and cinput.get()!="" and zipcode!=""):
        for i in fname:
            if(i in numbers):
                checked=False
                messagebox.showerror("Validation Error","Name should contain alphabet's only")
                break
    
        for i in lname:
            if(i in numbers and checked):
                checked=False
                messagebox.showerror("Validation Error","Name should contain alphabet's only")
                break
            
        if("@" not in email and email!="" and checked):
            checked=False
            messagebox.showerror("Validation Error","Email should contain @ sign")

        for i in zipcode:
            if(i not in numbers and checked):
                checked=False
                messagebox.showerror("Validation Error","Zip code should contain alphabet only")

        if(checked):
            temp=fname+" "+lname+" "+sinput.get()+" "+cinput.get()
            billing_list.append(temp)
            messagebox.showinfo("Success","Data inserted Succesfully")
            billing_box.delete(0,END)
            for i in billing_list:
                billing_box.insert(END,i)
    else:
        messagebox.showerror("Error","Please fill out all fields")
    
def delete_func():
    temp=""
    for i in billing_box.curselection():
        temp=billing_box.get(i)
    if(temp in billing_list):
        billing_list.remove(temp)
        messagebox.showinfo("Success","Data deleted successfully...!")
        billing_box.delete(0,END)
        for i in billing_list:
            billing_box.insert(END,i)
    pass

# Buttons-----------------------------
insert=Button(button_frame,text="Insert",width=20,command=insert_func)
delete=Button(button_frame,text="Delete",width=20,command=delete_func)
theme=Button(button_frame,text="Theme",width=20,command=change_theme)

# setting buttons----------------------
insert.grid(row=0,column=0)
delete.grid(row=1,column=0,pady=50)
theme.grid(row=2,column=0)

# Listbox widget
billing_box=Listbox(billing_frame,height=24,width=40)

# Setting up the listbox
billing.pack()
billing_box.pack()

# Radiobox widget
gen=StringVar()
gen.set(" ")
male=Radiobutton(gender_frame,text="Male",variable=gen,value="Male")
female=Radiobutton(gender_frame,text="Female",variable=gen,value="Female")

# setting up the radiobutton
male.grid(row=0,column=0)
female.grid(row=0,column=1)

# Checkbutton Widget
tvar=IntVar()
evar=IntVar()
hvar=IntVar()

telugu=Checkbutton(lang_frame,text="Telugu",onvalue=1,offvalue=0,variable=tvar)
english=Checkbutton(lang_frame,text="English",onvalue=2,offvalue=0,variable=evar)
hindi=Checkbutton(lang_frame,text="Hindi",onvalue=3,offvalue=0,variable=hvar)

# Setting but the checbutton
telugu.grid(row=0,column=0)
english.grid(row=0,column=1)
hindi.grid(row=0,column=2)

# Setting fields in form---------------
first_name.grid(row=0,column=0,pady=10)
finput.grid(row=0,column=1)

last_name.grid(row=1,column=0,pady=10)
linput.grid(row=1,column=1)

gender.grid(row=2,column=0,pady=10)
gender_frame.grid(row=2,column=1)

languages.grid(row=3,column=0,pady=10)
lang_frame.grid(row=3,column=1)

email.grid(row=4,column=0,pady=10)
einput.grid(row=4,column=1)

address.grid(row=5,column=0,pady=10)
address_frame.grid(row=5,column=1)

state.grid(row=6,column=0,pady=10)
sinput.grid(row=6,column=1)

zip.grid(row=7,column=0,pady=10)
zinput.grid(row=7,column=1)

card.grid(row=8,column=0,pady=10)
cinput.grid(row=8,column=1)

# Setting the layout-------------
input_frame.grid(row=0,column=0,pady=40,padx=15)
button_frame.grid(row=0,column=1,padx=25)
billing_frame.grid(row=0,column=2)

# Setting the theme
root.config(bg=theme_var.get())

root.mainloop()