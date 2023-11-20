import tkinter as tk
from tkinter import messagebox
import cv2
import pickle
from PIL import Image, ImageTk


# Define camera and detect face
face_cascade = cv2.CascadeClassifier('haarcascade/haarcascade_frontalface_default.xml')
cap = cv2.VideoCapture(0)
#2 Load recognize and read label from model
recognizer = cv2.face.LBPHFaceRecognizer_create()
recognizer.read("train.yml")

labels = {"person_name": 1}
with open("labels.pickle", "rb") as f:
    labels = pickle.load(f)
    labels = {v: k for k, v in labels.items()}

class FacePage(tk.Frame):
    def __init__(self, parent, controller, args):
        tk.Frame.__init__(self, parent)
        self.login_button = tk.Button(self, text="Back to password", command=self.login)
        self.login_button.pack()

        self.controller = controller

        # Create a label and display it on app 
        self.panel = tk.Label(self) 
        self.panel.pack()


        self.username_text = args["username"]
        self.face_name_text = ""
        self.timer = 40
        self.check_face()



    def login(self):
        self.controller.show_frame("InfoPage", {"username": self.username_text})

    def checkUserName(self):
        self.username_text = self.controller.sql.get_username(self.username.get())
        return not self.username_text == None
    
    def update_image(self): 
        ret, frame = cap.read()
        frame = cv2.cvtColor(frame, cv2.COLOR_BGR2RGBA)
        img = Image.fromarray(frame)
        photo = ImageTk.PhotoImage(image=img)
        self.panel.photo = photo
        self.panel.configure(image=photo) 
        self.after(1, self.update_image)

    def check_face(self):
        ret, frame = cap.read()
        gray = cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY)
        video = cv2.cvtColor(frame, cv2.COLOR_BGR2RGBA)
        faces = face_cascade.detectMultiScale(gray, scaleFactor=1.5, minNeighbors=5)
        for (x, y, w, h) in faces:
            #print(x, w, y, h)
            roi_gray = gray[y:y + h, x:x + w]
            #roi_color = video[y:y + h, x:x + w]
            # predict the id and confidence for faces
            id_, conf = recognizer.predict(roi_gray)
            if conf >= 50:
                font = cv2.QT_FONT_NORMAL
                name = labels[id_]
                color = (255, 0, 0)
                stroke = 2
                cv2.putText(video, name, (x, y), font, 1, color, stroke, cv2.LINE_AA)
                cv2.rectangle(video, (x, y), (x + w, y + h), (255, 0, 0), (2))
                self.face_name_text = name
                self.timer -= 1
            else:
                color = (255, 0, 0)
                stroke = 2
                font = cv2.QT_FONT_NORMAL
                cv2.putText(video, "UNKNOWN", (x, y), font, 1, color, stroke, cv2.LINE_AA)
                cv2.rectangle(video, (x, y), (x + w, y + h), (255, 0, 0), (2))
        img = Image.fromarray(video)
        photo = ImageTk.PhotoImage(image=img)
        self.panel.photo = photo
        self.panel.configure(image=photo)
        print(self.face_name_text, self.username_text)
        if (self.face_name_text == self.username_text and self.timer <= 0):
            self.controller.show_frame("InfoPage")
            return
        self.after(1, self.check_face)