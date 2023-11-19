import tkinter as tk
from tkinter import messagebox

class PasswordPage(tk.Frame):
    def __init__(self, parent, controller, args):
        tk.Frame.__init__(self, parent)
        self.label = tk.Label(self, text="Enter your password")
        self.label.pack()
        self.password = tk.Entry(self)
        self.password.pack()
        self.login_button = tk.Button(self, text="Login", command=self.login)
        self.login_button.pack()
        self.face_button = tk.Button(self, text="Use Face Recognition", command=self.change_to_face_page)
        self.face_button.pack()

        self.controller = controller
        self.username_text = args["username"]
        self.password_text = ""


    def login(self):
        # Check if the username and password are correct
        # For the sake of simplicity, let's assume they are always correct
        if self.checkPassword():  # replace this with your own condition
            messagebox.showinfo("Login", "Login successful!")
            self.controller.show_frame("InfoPage")
        else:
            messagebox.showinfo("Login", "Wrong password!")

    def checkPassword(self):
        self.password_text = self.controller.sql.get_password(self.username_text)
        return self.password_text == self.password.get()
    
    def change_to_face_page(self):
        self.controller.show_frame("FacePage")
        return
