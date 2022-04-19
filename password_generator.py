import random

num_choices='0123456789'
lower_char_choices='abcdefghijklmnopqrstuvwxyz'
upper_char_choices='ABCDEFGHIJKLMNOPQRSTUVWXYZ'
special_char_choices=''' !"#$%&'()*+,-./:;<=>?@[\]^_`{|}~'''

def generate_password(length=8,use_num=True ,use_upper_char=True, use_lower_char=True, use_spacial_char=True):
    choices=''
    password=''

    if use_num:
        choices+=num_choices
    
    if use_upper_char:
        choices+=lower_char_choices
    
    if use_lower_char:
        choices+=upper_char_choices
    
    if use_spacial_char:
        choices+=special_char_choices
    
    if not choices:
        choices=num_choices+lower_char_choices+upper_char_choices+special_char_choices

    for i in range(length):
        password+=random.choice(choices)
    return password

# Import Module
from tkinter import *
 
# create root window
root = Tk()
 
# root window title and dimension
root.title("Password Generator Application")
# Set geometry (widthxheight)
root.geometry('350x350')
 
# all widgets will be here
#adding a label to the root window
# lbl = Label(root, text = "Choose Options To Generate Your Password", font=50)
# lbl.grid(column=1, row=1)

pass_length = IntVar()
use_num = BooleanVar()
use_upper_char = BooleanVar()
use_lower_char = BooleanVar()
use_spacial_char = BooleanVar()

use_num_check_btn = Checkbutton(root, text = "Use number", variable = use_num, onvalue = True, offvalue = False, height = 2)
use_num_check_btn.grid(column=1, row=2)

use_upper_char_check_btn = Checkbutton(root, text = "Use upper character", variable = use_upper_char, onvalue = True, offvalue = False, height = 2)
use_upper_char_check_btn.grid(column=2, row=2)

use_lower_char_check_btn = Checkbutton(root, text = "Use lower character", variable = use_lower_char, onvalue = True, offvalue = False, height = 2)
use_lower_char_check_btn.grid(column=1, row=3)

use_spacial_check_btn = Checkbutton(root, text = "Use spacial character", variable = use_spacial_char, onvalue = True, offvalue = False, height = 2)
use_spacial_check_btn.grid(column=2, row=3)

pass_length_label=Label(text='Password length')
pass_length_label.grid(column=1, row=4)


pass_length_scale = Scale( root, variable = pass_length, from_ = 1, to = 100, orient = HORIZONTAL) 
pass_length_scale.grid(column=2, row=4)


def print_pass():
    print(generate_password(length=pass_length.get(), use_num=use_num.get(), use_lower_char=use_lower_char.get(), use_upper_char=use_upper_char.get(), use_spacial_char=use_spacial_char.get()), end='\n\n')

pass_gen_btn = Button(text = 'Generate password', bd = '5', command = print_pass)
pass_gen_btn.grid(column=1, row=5)

# Execute Tkinter
root.mainloop()




# print('Password 1 - ',generate_password())
# print('Password 2 - ',generate_password(10))
# print('Password 3 - ',generate_password(8,False))
# print('Password 4 - ',generate_password(8, False, False))
# print('Password 5 - ',generate_password(8, False, False, False))
# print('Password 6 - ',generate_password(8, False, False, False, False))