from tkinter import *
from tkinter import messagebox
import random


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


# ---------------------------- SAVE PASSWORD ------------------------------- #


def save():
    is_ok = messagebox.askokcancel(title=website_input.get(), message="Is it ok to save?")
    if is_ok:
        with open("data.txt", "a") as f:
            f.write(website_input.get() + " | " + email_input.get() + " | " + pass_input.get())
            f.write("\n")
        website_input.delete(0, END)
        pass_input.delete(0, END)


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

website_input = Entry(width=35)
website_input.grid(column=1, columnspan=2, row=1)

email_label = Label(text="Email/Username: ", font=("Arial", 15))
email_label.grid(column=0, row=2)

email_input = Entry(width=35)
email_input.grid(column=1, columnspan=2, row=2)
email_input.insert(0, "mohammadalmousawi74@gmail.com")

pass_label = Label(text="Password: ", font=("Arial", 15))
pass_label.grid(column=0, row=3)

pass_input = Entry(width=21)
pass_input.grid(column=1, row=3)

add_button = Button(text="Add", width=36, command=check)
add_button.grid(column=1, columnspan=2, row=4)

pass_button = Button(text="Generate Password", command=generate)
pass_button.grid(column=2, row=3)

window.mainloop()
