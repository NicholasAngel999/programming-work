import tkinter as tk
from tkinter import messagebox
import getpass

import Password_manager as pm

root = tk.Tk()
root.title("Password Manager")
root.attributes("-type", "dialog")
root.geometry("400x300")
root.resizable(False, False)
root.mainloop()
# ------------------------------
# GUI

def gui_add_password():
    website = entry_website.get().strip()
    password = entry_password.get().strip()
    if not website or not password:
        messagebox.showwarning("missing Info, Please fill in both fields.")
        return
    pm.add_password(website, password)
    messagebox.showinfo("Success", f"Password saved for {website}!")
    entry_website.delete(0, tk.EMD)
    entry_password.delete(0, tk.END)

    

