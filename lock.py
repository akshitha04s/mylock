from tkinter import *
from tkinter import messagebox
import random as r
import json
window=Tk()
window.title("My Lock")
window.config(padx=20,pady=20)
def adddata():
    currweb=websiteentry.get()
    curremail=emailentry.get()
    currpass=passwordentry.get()
    if(len(currweb)==0 or len(curremail)==0 or len(currpass)==0):
        messagebox.showerror(title="ERROR",message="One or more boxes are empty.please fill  them")
        return
    currdata=f"Website name: {currweb}\nEmail/username : {curremail}\nPassword : {currpass}\n\n\n"
    jsondata = {currweb: {"email/username": curremail, "Password": currpass}}
    try:
        with open("data.json", "r") as df:
            data = json.load(df)
    except FileNotFoundError:
        data = {}

    # Check if the website already exists
    if currweb in data:
        confirm_update = messagebox.askyesno(title="WEBSITE EXISTS", message=f"Data for '{currweb}' already exists. Do you want to update it with the new details?")
        if not confirm_update:
            return  # Exit without saving if user clicks 'No'
    else:
        # Standard confirmation message for brand-new items
        confirm = messagebox.askokcancel(title="CONFIRMATION", message=f"{currdata}\nPress OK to continue")
        if not confirm:
            return

    # Update data dictionary and completely overwrite file cleanly with 'w'
    data.update(jsondata)
    with open("data.json", "w") as df:
        json.dump(data, df, indent=4)
        
    websiteentry.delete(0, END)
    passwordentry.delete(0, END)    
def genpass():
    passlist=['Q','W','E','R','T','Y','U','I','O','P','A','S','D','F','G','H','J','K','L','Z','X','C','V','B','N','M','q','w','e','r','t','y','u','i','o','p','a','s','d','f','g','h','j','k','l','z','x','c','v','b','n','m','1','2','3','4','5','6','7','8','9','0','!','@','#','$','%','^','&','*','?']
    generatedpasslist=r.choices(passlist,k=10)
    generatedpass = "".join(generatedpasslist)
    passwordentry.delete(0, END)
    passwordentry.insert(0, generatedpass)
def search_data():
    currweb = websiteentry.get()
    if len(currweb) == 0:
        messagebox.showerror(title="ERROR", message="Please enter a website name to search.")
        return
    try:
        with open("data.json", "r") as df:
            data = json.load(df)
    except FileNotFoundError:
        messagebox.showerror(title="ERROR", message="No data file found yet. Add some entries first!")
        return
    if currweb in data:
        email = data[currweb]["email/username"]
        password = data[currweb]["Password"]
        messagebox.showinfo(title=currweb, message=f"Email/Username: {email}\nPassword: {password}")
    else:
        messagebox.showerror(title="NOT FOUND", message="No details found")
logo=PhotoImage(file="images.png")
canvas=Canvas(height=400,width=400)
canvas.create_image(200,200,image=logo)
canvas.grid(row=0,column=1)
websitelabel=Label(text="Website:")
websitelabel.grid(row=1,column=0)
websiteentry=Entry(width=100)
websiteentry.grid(row=1,column=1,columnspan=2)
websiteentry.focus()
emaillabel=Label(text="Email/Username:")
emaillabel.grid(row=2,column=0)
emailentry=Entry(width=100)
emailentry.grid(row=2,column=1,columnspan=2)
emailentry.insert(0,"surakantiakshithareddy04@gmail.com")
passwordlabel=Label(text="Password")
passwordlabel.grid(row=3,column=0)
passwordentry=Entry(width=75)
passwordentry.grid(row=3,column=1,columnspan=2)
genpassbutton=Button(text="Generate password",command=genpass)
genpassbutton.grid(row=3,column=4)
addbutton=Button(text="Add",command=adddata)
addbutton.grid(row=4,column=1)
searchbutton=Button(text="Search",command=search_data)
searchbutton.grid(row=4,column=2)
window.mainloop()