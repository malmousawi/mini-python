from tkinter import *
from tkinter import messagebox
import random
import pyperclip
import json


# ---------------------------- PASSWORD GENERATOR ------------------------------- #

def generate():
    letters = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u',
               'v', 'w', 'x', 'y', 'z', 'A', 'B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'K', 'L', 'M', 'N', 'O', 'P',
               'Q', 'R', 'S', 'T', 'U', 'V', 'W', 'X', 'Y', 'Z']
    numbers = ['0', '1', '2', '3', '4', '5', '6', '7', '8', '9']
    symbols = ['!', '#', '$', '%', '&', '(', ')', '*', '+']

    nr_letters = random.randint(8, 10)
    nr_symbols = random.randint(2, 4)
    nr_numbers = random.randint(2, 4)

    password_list = []

    pass_letters = [random.choice(letters) for i in range(nr_letters)]
    pass_symbols = [random.choice(symbols) for i in range(nr_symbols)]
    pass_numbers = [random.choice(numbers) for i in range(nr_numbers)]

    password_list = pass_letters + pass_symbols + pass_numbers

    random.shuffle(password_list)

    password = ""
    for char in password_list:
        password += char

    pass_input.insert(0, password)
    pyperclip.copy(password)


# ---------------------------- SAVE PASSWORD ------------------------------- #


def save():
    new_data = {
        website_input.get(): {
            "email": email_input.get(),
            "password": pass_input.get(),
        }
    }
    is_ok = messagebox.askokcancel(title=website_input.get(), message="Is it ok to save?")
    if is_ok:
        try:
            with open("data.json", "r") as f:
                data = json.load(f)
        except FileNotFoundError:
            with open("data.json", "w") as f:
                json.dump(new_data, f, indent=4)
        else:
            data.update(new_data)
            with open("data.json", "w") as f:
                json.dump(data, f, indent=4)
        finally:
            website_input.delete(0, END)
            pass_input.delete(0, END)


def find_password():
    website = website_input.get()
    try:
        with open("data.json") as f:
            data = json.load(f)
    except FileNotFoundError:
        messagebox.showinfo(message="Data not found")
    else:
        if website in data:
            email = data[website]["email"]
            password = data[website]["password"]
            messagebox.showinfo(message=f"Email: {email}\nPassword: {password}")
        else:
            messagebox.showinfo(message="Data not found")
        website_input.delete(0, END)


def check():
    if website_input.get() == "" or email_input.get() == "" or pass_input.get() == "":
        messagebox.showinfo(message="You have left fields empty!")
    else:
        save()


# ---------------------------- UI SETUP ------------------------------- #


window = Tk()
window.title("Password Manager")
window.config(padx=50, pady=50)

canvas = Canvas(width=200, height=200)
img = PhotoImage(file="logo.png")
canvas.create_image(100, 100, image=img)
canvas.grid(column=1, row=0)

website_label = Label(text="Website: ", font=("Arial", 15))
website_label.grid(column=0, row=1)

website_input = Entry(width=18)
website_input.grid(column=1,  row=1)

email_label = Label(text="Email/Username: ", font=("Arial", 15))
email_label.grid(column=0, row=2)

email_input = Entry(width=35)
email_input.grid(column=1, columnspan=2, row=2)
email_input.insert(0, "mohammadalmousawi74@gmail.com")

pass_label = Label(text="Password: ", font=("Arial", 15))
pass_label.grid(column=0, row=3)

pass_input = Entry(width=35)
pass_input.grid(column=1, row=3, columnspan=2)

add_button = Button(text="Add", width=36, command=check)
add_button.grid(column=1, columnspan=2, row=4)

pass_button = Button(text="Generate Password", command=generate)
pass_button.grid(column=2, row=3)

search_button = Button(text="Search", command=find_password, width=13)
search_button.grid(column=2, row=1)

window.mainloop()
