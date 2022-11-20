import tkinter
from tkinter import *
from tkinter import messagebox
import random
def password_gen():
    upper = "QWERTYUIOPASFKLZXCVBNM"
    lower = "qwertyuiopasdfghjklzxcvbnm"
    spec ="<>}{(*&^%#@$!~}"
    num ="1234567890"
    alllen = upper + lower+ spec+num
    length = 9
    pass_word = ''.join(random.sample(alllen,length)) #sample is use to find sample in range
    #print("the password you entered is:",pass_word)
    password_entry.insert(0,pass_word)
def save():
    website= website_entry.get()
    email = email_entry.get()
    password= password_entry.get()
    if len(website)==0 or len(password)==0:
        messagebox.showinfo(title="oops",message="please make sure you have not any field blanks")
    else:
        is_ok = messagebox.askokcancel(title=website, message=f"there are the detaailed:\n{email}\npassword:{password}")
        if is_ok:
            with open("data.txt","a")as data_file:
                data_file.write(f"website_name: {website} | Username:{email} | Password:{password}\n")
                website_entry.delete(0,END)
                password_entry.delete(0,END)
                email_entry.delete(0,END)
                messagebox.showinfo(message="Password Saved")
window = tkinter.Tk()
window.title("Password Managers")
window.iconbitmap("iconnn.ico")
#window.configure(bg="pink")
window.maxsize(width=500,height=400)
window.minsize(width=500,height=400)
window.config(padx=20, pady=20)
canvas = Canvas(height=200, width=220)
logo_img = PhotoImage(file="logo2.png")
canvas.create_image(130,120,image=logo_img)
#canvas.configure(bg="pink")
canvas.grid(row=0,column=1)
#label
website_label=Label(text="Website   :")
website_label.configure(bg="red")
website_label.grid(row=1,column=0)
email_label=Label(text="Username:")
email_label.configure(bg="red")
email_label.grid(row=2,column=0)
password_label=Label(text="Password:")
password_label.configure(bg="red")
password_label.grid(row=3,column=0)
#entry
website_entry=Entry(width=50)
website_entry.configure(bg="yellow")
website_entry.focus()
website_entry.grid(row=1,column=1,columnspan=3)
email_entry=Entry(width=50)
email_entry.configure(bg="yellow")
email_entry.grid(row=2,column=1,columnspan=3)
password_entry=Entry(width=32)
password_entry.configure(bg="yellow")
password_entry.grid(row=3,column=1)
#button

generate_password_button= Button(text="Generate Password",width=17,command=password_gen)
generate_password_button.configure(bg="red")
generate_password_button.grid(row=3,column=2)
add_button=Button(text="Add",width=50,command=save)
add_button.configure(bg="red")
add_button.grid(row=4,column=1,columnspan=2)
window.mainloop()
