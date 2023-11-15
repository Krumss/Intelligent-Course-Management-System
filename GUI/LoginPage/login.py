import tkinter as tk
from tkinter import messagebox

class LoginPage(tk.Frame):
    def __init__(self, parent, controller):
        tk.Frame.__init__(self, parent)

        self.username_label = tk.Label(self, text="Username")
        self.username_entry = tk.Entry(self)
        self.username_label.pack()
        self.username_entry.pack()
        self.controller = controller

        self.password_label = tk.Label(self, text="Password")
        self.password_entry = tk.Entry(self, show="*")
        self.password_label.pack()
        self.password_entry.pack()

        login_button = tk.Button(self, text="Login", command=self.login)
        login_button.pack()


    def login(self):
        username = self.username_entry.get()
        password = self.password_entry.get()

        # Check if the username and password are correct
        # For the sake of simplicity, let's assume they are always correct
        if True:  # replace this with your own condition
            messagebox.showinfo("Login", "Login successful!")
            self.controller.show_frame("InfoPage")

