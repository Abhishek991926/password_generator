from tkinter import *
import random

num_choices = '0123456789'
lower_char_choices = 'abcdefghijklmnopqrstuvwxyz'
upper_char_choices = 'ABCDEFGHIJKLMNOPQRSTUVWXYZ'
special_char_choices = ''' !"#$%&'()*+,-./:;<=>?@[\]^_`{|}~'''


def generate_password(length=8, use_num=True, use_upper_char=True, use_lower_char=True, use_spacial_char=True):
    choices = ''
    password = ''

    if use_num:
        choices += num_choices

    if use_upper_char:
        choices += lower_char_choices

    if use_lower_char:
        choices += upper_char_choices

    if use_spacial_char:
        choices += special_char_choices

    if not choices:
        choices = num_choices+lower_char_choices + \
            upper_char_choices+special_char_choices

    for i in range(length):
        password += random.choice(choices)
    return password


# create root window
root = Tk()

# root window title and dimension
root.title("Password Generator Application")
# Set geometry (widthxheight)
root.geometry('360x250')


# all variables

pass_length = IntVar()
use_num = BooleanVar()
use_upper_char = BooleanVar()
use_lower_char = BooleanVar()
use_spacial_char = BooleanVar()
generated_password_var = StringVar()

# all widgets will be here

top_label = Label(text='Password Generator', anchor=CENTER, font=("Arial", 20))
top_label.grid(column=1, row=1, columnspan=2, padx=55)

use_num_check_btn = Checkbutton(
    root, text="Use number", variable=use_num, onvalue=True, offvalue=False, height=2)
use_num_check_btn.grid(column=1, row=2)

use_upper_char_check_btn = Checkbutton(
    root, text="Use upper character", variable=use_upper_char, onvalue=True, offvalue=False, height=2)
use_upper_char_check_btn.grid(column=2, row=2)

use_lower_char_check_btn = Checkbutton(
    root, text="Use lower character", variable=use_lower_char, onvalue=True, offvalue=False, height=2)
use_lower_char_check_btn.grid(column=1, row=3, padx=10)

use_spacial_check_btn = Checkbutton(
    root, text="Use spacial character", variable=use_spacial_char, onvalue=True, offvalue=False, height=2)
use_spacial_check_btn.grid(column=2, row=3)

pass_length_label = Label(text='Password length')
pass_length_label.grid(column=1, row=4)

pass_length_scale = Scale(variable=pass_length,
                          from_=1, to=20, orient=HORIZONTAL)
pass_length_scale.grid(column=2, row=4)

generated_password = ''


def print_pass():
    global generated_password
    generated_password = generate_password(length=pass_length.get(), use_num=use_num.get(
    ), use_lower_char=use_lower_char.get(), use_upper_char=use_upper_char.get(), use_spacial_char=use_spacial_char.get())
    print(generated_password)
    generated_password_var.set('Your Passoword: '+generated_password)


def copy_password():
    global generated_password
    root.clipboard_clear()
    root.clipboard_append(generated_password)
    root.update()


pass_gen_btn = Button(text='Generate password', command=print_pass)
pass_gen_btn.grid(column=1, row=5, pady=10)

pass_gen_btn = Button(text='Copy Password', command=copy_password)
pass_gen_btn.grid(column=2, row=5, pady=10)

pass_length_label = Label(
    textvariable=generated_password_var, font=("Arial", 12))
pass_length_label.grid(column=1, columnspan=2, row=6)

made_by_label = Label(text='Made by Abhishek Kumar Yadav')
made_by_label.grid(column=1, columnspan=2, row=7)

# Execute Tkinter
root.mainloop()
