import os
import tkinter as tk
from dotenv import load_dotenv

from LoginPage.login import LoginPage
from info import InfoPage
from dbConn.mysql_connection import SqlConnection

frames = {"LoginPage": LoginPage, "InfoPage": InfoPage}

class tkinterApp(tk.Tk):
    def __init__(self, *args, **kwargs):
        tk.Tk.__init__(self, *args, **kwargs)

        self.container = tk.Frame(self)
        self.container.pack(side = "top", fill = "both", expand = True)

        self.curr = frames["LoginPage"](self.container, self, {})
        self.curr.pack()

        load_dotenv()
        self.sql = SqlConnection(os.getenv("HOST"), os.getenv("USER"), os.getenv("PASSWORD"), os.getenv("DATABASE"))
        self.sql.connect()

    def show_frame(self, cont, args={}):
        old = self.curr
        old.pack_forget()
        frame = frames[cont](self.container, self, args)
        frame.pack()
        self.curr = frame


app = tkinterApp()
app.mainloop()