import tkinter as tk
from tkinter import messagebox
import random
def generate_password():
    try:
        length = int(length_entry.get())
        if length < 4:
            messagebox.showwarning("Warning", "Password length should be at least 4 characters.")
            return
        char_pool="abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXY0123456789@#$%^&*"
        password=""
        # Generate a random password
        for _ in range(length):
           password += ''.join(random.choice(char_pool))
        
        # Display the generated password
        password_entry.delete(0, tk.END)
        password_entry.insert(0, password)
    except ValueError:
        messagebox.showerror("Error", "Please enter a valid number for the password length.")

root = tk.Tk()
root.title("Password Generator")
tk.Label(root, text="Enter the desired length of the pasword:").grid(row=0, column=0, pady=10)
length_entry = tk.Entry(root, width=10)
length_entry.grid(row=0, column=1, pady=10)

generate_button = tk.Button(root, text="Generate Password", command=generate_password)
generate_button.grid(row=1, column=0, columnspan=2, pady=10)

tk.Label(root, text="Generated Password:").grid(row=2, column=0, padx=10, pady=10)
password_entry = tk.Entry(root, width=30)
password_entry.grid(row=2, column=1, padx=10, pady=10)

root.mainloop()
