import tkinter as tk
from tkinter import messagebox
import getpass
import Password_manager as pm

root = tk.Tk()
root.title("Password Manager")
root.attributes("-type", "dialog")
root.geometry("400x300")
root.resizable(False, False)

# ------------------------------
# GUI FUNCTIONS
# ------------------------------

def gui_add_password():
    website = entry_website.get().strip()
    password = entry_password.get().strip()
    if not website or not password:
        messagebox.showwarning("Missing Info", "Please fill in both fields.")
        return
    pm.add_password(website, password)
    messagebox.showinfo("Success", f"Password saved for {website}!")
    entry_website.delete(0, tk.END)
    entry_password.delete(0, tk.END)


def gui_get_password():
    website = entry_website.get().strip()
    if not website:
        messagebox.showwarning("Missing Info", "Please enter a website name.")
        return
    result = pm.get_password(website)
    if result:
        messagebox.showinfo("Password Found", f"{website}: {result}")
    else:
        messagebox.showwarning("Not Found", f"No password found for {website}.")


def gui_view_websites():
    try:
        with open('passwords.json', 'r') as f:
            data = pm.json.load(f)
        websites = "\n".join(x['website'] for x in data)
        messagebox.showinfo("Saved Websites"
