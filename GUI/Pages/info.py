import tkinter as tk

class InfoPage(tk.Frame):
    def __init__(self, parent, controller, args):
        tk.Frame.__init__(self, parent)

        course_info_label = tk.Label(self, text="Course Information: COMP3278")
        course_info_label.pack()

        classroom_name_label = tk.Label(self, text="Classroom Name: MB221")
        classroom_name_label.pack()

        teacher_message_label = tk.Label(self, text="Teacher's Message: Hi, I am Kevin.")
        teacher_message_label.pack()

        zoom_link_label = tk.Label(self, text="Zoom Link: null")
        zoom_link_label.pack()