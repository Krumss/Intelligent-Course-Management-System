import tkinter as tk
from tkinter import messagebox


class LoginPage(tk.Frame):
    def __init__(self, parent, controller, args):
        tk.Frame.__init__(self, parent)
        self.label = tk.Label(self, text="Enter your username")
        self.label.pack()
        self.username = tk.Entry(self)
        self.username.pack()
        self.login_button = tk.Button(self, text="Next", command=self.login)
        self.login_button.pack()

        self.controller = controller
        self.username_text = ""


    def login(self):
        # Check if the username and password are correct
        # For the sake of simplicity, let's assume they are always correct
        if self.checkUserName():  # replace this with your own condition
            self.controller.show_frame("PasswordPage", {"username": self.username_text})
        else:
            messagebox.showinfo("Login", "No this username!")

    def checkUserName(self):
        self.username_text = self.controller.sql.get_username(self.username.get())
        return not self.username_text == None
        








