import tkinter as tk
from tkinter import messagebox
import cv2
from PIL import Image, ImageTk


class FacePage(tk.Frame):
    def __init__(self, parent, controller, args):
        tk.Frame.__init__(self, parent)
        self.login_button = tk.Button(self, text="Next", command=self.login)
        self.login_button.pack()

        self.controller = controller

        # Create a label and display it on app 
        self.label_widget = tk.Label(self) 
        self.label_widget.pack()

        
        self.cap = cv2.VideoCapture(0)
        self.cap.set(cv2.CAP_PROP_FRAME_WIDTH, 300) 
        self.cap.set(cv2.CAP_PROP_FRAME_HEIGHT, 300) 

        self.canvas = tk.Canvas(self, width = 300, height = 300, bg="#ffffff")
        self.update_image()
        self.canvas.pack()



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
    
    def update_image(self): 
        ret, frame = self.cap.read()
        cv2.imshow('frame', frame)
        frame = cv2.cvtColor(frame, cv2.COLOR_BGR2RGB)
        img = Image.fromarray(frame)
        photo = ImageTk.PhotoImage(img)
        self.canvas.create_image(0, 0, image = photo, anchor = tk.NW)
        self.canvas.after(10, self.update_image)