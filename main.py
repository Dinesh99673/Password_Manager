import tkinter
from tkinter import messagebox

window = tkinter.Tk()
window.title("Password Manager")
window.config(padx=50,pady=50)
# ---------------------------- PASSWORD GENERATOR ------------------------------- #

def generate_buttom():
    print("clicked")
    password_entry.insert(0,"85693256")

# ---------------------------- SAVE PASSWORD ------------------------------- #
def save_data():
    website = website_entry.get()
    email = email_entry.get()
    password = password_entry.get()

    if len(website)==0 or len(password)==0:
        messagebox.showwarning(title="Wrong credentials",message="Dont't leave any field empty :(")
        return    
    is_ok = messagebox.askokcancel(title=website,message=f"This are the details entered : \n Email :- {email} \n Password :- {password} \n Is it ok to save ?")
    if is_ok:
        with open("data.txt", "a") as file:
            file.write(f"{website} | {email} | {password}\n")
            website_entry.delete(0,len(website))
            password_entry.delete(0,len(password))
            messagebox.showinfo(title="Success",message="Data saved successfully ")

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

#Entries
website_entry = tkinter.Entry(width=42)
website_entry.grid(row=1, column=1, columnspan=3)
website_entry.focus()

email_entry = tkinter.Entry(width=42)
email_entry.grid(row=2, column=1, columnspan=2)
email_entry.insert(0,"dineshchudhary123@gmail.com")

password_entry = tkinter.Entry(width=24)
password_entry.grid(column=1, row=3)

#Buttons
generate_password_button = tkinter.Button(text="Generate Password", command=generate_buttom)
generate_password_button.grid(column=2, row=3)

add_button = tkinter.Button(text="Add",width=36, command=save_data)
add_button.grid(row=4, column=1, columnspan=2)


window.mainloop()

