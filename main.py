import random
import tkinter
from tkinter import messagebox
import pyperclip
import json

window = tkinter.Tk()
window.title("Password Manager")
window.config(padx=50,pady=50)

# ---------------------------- PASSWORD GENERATOR ------------------------------- #

def generate_password():
    letters = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z', 'A', 'B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'K', 'L', 'M', 'N', 'O', 'P', 'Q', 'R', 'S', 'T', 'U', 'V', 'W', 'X', 'Y', 'Z']
    numbers = ['0', '1', '2', '3', '4', '5', '6', '7', '8', '9']
    symbols = ['!', '#', '$', '%', '&', '(', ')', '*', '+']

    password_list = []

    [password_list.append(random.choice(letters)) for char in range(random.randint(8, 10))]

    [password_list.append(random.choice(symbols)) for char in range(random.randint(2, 4))]

    [password_list.append(random.choice(numbers)) for char in range(random.randint(2, 4))]

    random.shuffle(password_list)

    password = "".join(password_list)

    print(f"Your password is: {password}")
    password_entry.delete(0,len(password_entry.get()))
    password_entry.insert(0,password)
    pyperclip.copy(password)

# ---------------------------- SAVE PASSWORD ------------------------------- #

def save_data():
    website = website_entry.get()
    email = email_entry.get()
    password = password_entry.get()
    new_data = {website:{
        "email":email,
        "password":password
    }}

    if len(website)==0 or len(password)==0:
        messagebox.showwarning(title="Ooops",message="Please dont't leave any fields empty :(")
        return    
    is_ok = messagebox.askokcancel(title=website,message=f"This are the details entered : \n Email :- {email} \n Password :- {password} \n Is it ok to save ?")
    if is_ok:
        try:
            with open("data.json", "r") as file:
                #Reading old data
                data = json.load(file)
                #Updating old data
                data.update(new_data)
        except:
            data = new_data
        with open("data.json","w") as file:
            #saving the new data
            json.dump(data,file, indent=4) # Dictionary data is saved in JSON format automatically
        website_entry.delete(0,len(website))
        password_entry.delete(0,len(password))
        messagebox.showinfo(title="Success",message="Data saved successfully ")

# ---------------------------- Searching ------------------------------- #

def search():
    print("In search")
    website = website_entry.get()
    try:
        with open("data.json","r") as file:
            data = json.load(file)
    except:
        messagebox.showwarning(title="Data not found", message="Something went Wrong, Data not found !!")
    try:
        found_data = data[website]
        email = found_data["email"]
        password = found_data["password"]
        messagebox.showinfo(title="Found",message=f"Email : {email}\nPassword : {password}\n")
    except:
        messagebox.showinfo(title="Not Found",message=f"No data found for entered {website} website/doman name")
    finally:
        website_entry.delete(0,len(website))

# ---------------------------- UI SETUP ------------------------------- #

canvas = tkinter.Canvas(width=200,height=200, highlightthickness=0)
logo = tkinter.PhotoImage(file="logo.png")
canvas.create_image(100,100, image=logo)
canvas.grid(column=1,row=0)


#Labels
website_label = tkinter.Label(text="Website :")
website_label.grid(column=0, row=1)

email_label = tkinter.Label(text="Email/Username :")
email_label.grid(column=0, row=2)

password_label = tkinter.Label(text="Password :")
password_label.grid(column=0, row=3)

#Entries/Input Boxs
website_entry = tkinter.Entry(width=36)
website_entry.grid(row=1, column=1, columnspan=3)
website_entry.focus()

email_entry = tkinter.Entry(width=42)
email_entry.grid(row=2, column=1, columnspan=2)
email_entry.insert(0,"userEmail@gmail.com") #default emal can ne inserted prior

password_entry = tkinter.Entry(width=24)
password_entry.grid(column=1, row=3)

#Buttons
generate_password_button = tkinter.Button(text="Generate Password", command=generate_password)
generate_password_button.grid(column=2, row=3)

search_button = tkinter.Button(text="Searh", command=search, width=10)
search_button.grid(column=2, row=1)

add_button = tkinter.Button(text="Add",width=36, command=save_data)
add_button.grid(row=4, column=1, columnspan=2)

window.mainloop()

