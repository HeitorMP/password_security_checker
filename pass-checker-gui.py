#!/usr/bin/env python3
import requests
import hashlib
import tkinter as tk
from tkinter import ttk


def request_api_data(query_char):
    url = 'https://api.pwnedpasswords.com/range/' + query_char
    res = requests.get(url)
    if res.status_code != 200:
        raise RuntimeError(
            f'Error fecthing: {res.status_code}, check the api and try again!')
    return res


def get_password_leaks_count(hashes, hash_to_check):
    hashes = (line.split(':') for line in hashes.text.splitlines())
    for h, count in hashes:
        if h == hash_to_check:
            return count
    return 0


def pwned_api_check(password):
    sha1password = hashlib.sha1(password.encode('utf-8')).hexdigest().upper()
    first5_char, tail = sha1password[:5], sha1password[5:]
    response = request_api_data(first5_char)
    return get_password_leaks_count(response, tail)


if __name__ == '__main__':
    pass_count = pwned_api_check('hello')

    root = tk.Tk()
    root.title("check password security")
    root.geometry('400x200')

    form_frame = ttk.Frame(root, padding=10)
    form_frame.grid()
    ttk.Label(form_frame, text="Password:").grid(column=0, row=0)

    def printInput():
        inp = inputtxt.get()
        count = pwned_api_check(inp)
        if count:
            result_label.config(
                text=f'Your password was found {count} times!\nYou should change your password!')
        else:
            result_label.config(
                text=f'Your password was found {count} times!\nAll good, carry on!')

    inputtxt = tk.Entry(form_frame, bd=5, width=46, show='*')
    inputtxt.grid(column=0, row=1)

    buttons_frame = ttk.Frame(root, padding=10)
    buttons_frame.grid()

    ttk.Button(buttons_frame, text="Check",
               command=printInput).grid(column=1, row=0)

    ttk.Button(buttons_frame, text="Quit",
               command=root.destroy).grid(column=2, row=0)

    result_frame = ttk.Frame(root, padding=10)
    result_frame.grid()
    result_label = ttk.Label(result_frame, text="aqui")
    result_label.grid(column=0, row=0)

    root.mainloop()
