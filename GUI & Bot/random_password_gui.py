'''Python program for generating random password'''

#Importing the modules
import tkinter as tk
from tkinter import ttk

import random
import string

#Data setting
lowercase = list(string.ascii_lowercase)
uppercase = list(string.ascii_uppercase)
digits = list(string.digits)
symbols = list(string.punctuation)


class Password:

    """Class for generating random strong passwords
    Attributes:
        length (int): Length of the password
        pwd (str): The password
    """

    def __init__(self, char, length):
        self.char = char
        self.length = length
        self.charset = []
        self.pwd = None

    def setchar(self):
        """Setting character set."""

        if 'l' in self.char: self.charset.extend(lowercase)
        if 'u' in self.char: self.charset.extend(uppercase)
        if 'd' in self.char: self.charset.extend(digits)
        if 's' in self.char: self.charset.extend(symbols)

    def password_gen(self):
        """Return the password

        Returns:
            str: The password
        """
        if len(self.char) == 0:
            self.charset.extend(lowercase)

        if len(self.length) == 0:
            self.length = 10 # By default, length is 10
        else:
            self.length = int(self.length)

        pwdlist = random.choices(self.charset, k=self.length)
        self.pwd = ''.join(pwdlist)
        return self.pwd


wind = tk.Tk()

def generate():
    global ch

    if u.get(): ch += 'u'
    if l.get(): ch += 'l'
    if d.get(): ch += 'd'
    if s.get(): ch += 's'

    password = Password(ch, len_entry.get())
    password.setchar()

    pwd.set(password.password_gen())
    ch = ''

# Initialise int variables
ch = ''
u = tk.IntVar()
d = tk.IntVar()
s = tk.IntVar()
l = tk.IntVar()
pwd = tk.StringVar()

# Main program
wind.title('Paasword Generator')
wind.geometry('400x300')
wind.resizable(0, 0)

head_label = ttk.Label(wind, text='Password Generator',
                       font=('Bodoni MT', 30, 'bold'))
head_label.grid(row=0, column=0, columnspan=2, pady=5)


len_label = ttk.Label(wind, text='Enter length', font=('Arial', 10))
len_label.grid(row=1, column=0, pady=10)

len_entry = ttk.Entry(wind, font=('Arial', 10, 'bold'))
len_entry.grid(row=1, column=1, pady=10)

upper_box = ttk.Checkbutton(wind, text='Uppercase', variable=u)
upper_box.grid(row=2, column=0)

lower_box = ttk.Checkbutton(wind, text='Lowercase', variable=l)
lower_box.grid(row=2, column=1)

digit_box = ttk.Checkbutton(wind, text='Digits', variable=d)
digit_box.grid(row=3, column=0)

symbol_box = ttk.Checkbutton(wind, text='Symbols', variable=s)
symbol_box.grid(row=3, column=1)

generate_button = ttk.Button(wind, text='Generate', command=generate)
generate_button.grid(row=4, column=0, columnspan=2, pady=10)

t_label = ttk.Label(wind, text=' Password :', font=('Arial', 10))
t_label.grid(row=5, column=0, pady=10)

password_disp = ttk.Entry(wind, font=('Arial', 10, 'bold'),
                          textvariable=pwd, width=30)
password_disp.grid(row=5, column=1, pady=10)

wind.mainloop()
