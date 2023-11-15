import tkinter as tk

from LoginPage.login import LoginPage
from info import InfoPage

class tkinterApp(tk.Tk):
    def __init__(self, *args, **kwargs):
        tk.Tk.__init__(self, *args, **kwargs)

        container = tk.Frame(self)
        container.pack(side = "top", fill = "both", expand = True)

        self.frames = {"LoginPage": [LoginPage, None], "InfoPage": [InfoPage, None]}
        self.curr = "LoginPage"

        for key, value in self.frames.items():
            F = value[0]
            self.frames[key] = [F, F(container, self)]
        print(self.frames)
        self.show_frame("LoginPage")

    def show_frame(self, cont):
        old = self.frames[self.curr][1]
        old.pack_forget()
        frame = self.frames[cont][1]
        frame.pack()
        self.curr = cont


app = tkinterApp()
app.mainloop()