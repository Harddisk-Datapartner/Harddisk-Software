from pydoc import text
from tkinter import *
from unicodedata import category
import customtkinter

root = customtkinter.CTk()
root_width = 1440
root_height = 810

root_frame = customtkinter.CTkFrame(master=root, fg_color="cyan")
root_frame.pack(fill="both", expand=True)


class Category1():
    def __init__(self):
        category_frame_1 = customtkinter.CTkFrame(master=install_frame, fg_color=("#c4c3c2", "red"), corner_radius=15)
        category_frame_1.pack(pady=5, padx=5, fill="both", expand=True)
        category_label_1 =customtkinter.CTkLabel(master=category_frame_1, fg_color=("#c4c3c2", "blue"), text="Nettlesere", corner_radius=15)
        category_label_1.pack(fill="x", side="top")
        category_button_1 = customtkinter.CTkButton(master = category_frame_1, text="button1")
        category_button_1.pack()




class CategoryWindow:
    def __init__(self, root, text=text):
        self.root = root_frame
        self.frame = customtkinter.CTkFrame(root_frame, fg_color="red", text=self.text)
        self.frame.pack()
        self.label = customtkinter.CTkLabel(self.frame, fg_color="gray", text=self.text)
        self.label.pack()
        self.button = customtkinter.CTkButton(self.frame, fg_color="green", text="buttontest")
        self.button.pack()



def CreateCategory1():
    category1 = CategoryWindow(root_frame, text="halllllo")
def CreateCategory2():
    category1 = CategoryWindow(root_frame, "bæsj")






createcat1_btn = customtkinter.CTkButton(root_frame, text="Create category 1", command=CreateCategory1)
createcat2_btn = customtkinter.CTkButton(root_frame, text="Create category 2", command=CreateCategory2)
createcat1_btn.pack()
createcat2_btn.pack()


"""class Category1Frame:
    def __init__(self, master):
        categoryframe = customtkinter.CTkFrame(master, fg_color="red")
        categoryframe.pack()
        categorylabel = customtkinter.CTkLabel(categoryframe, fg_color="blue", text="Frame 1")
        categorylabel.pack()

class Category2Frame:
    def __init__(self, master):
        categoryframe = customtkinter.CTkFrame(master, fg_color="yellow")
        categoryframe.pack()
        categorylabel = customtkinter.CTkLabel(categoryframe, fg_color="green", text="Frame 2")
        categorylabel.pack()



def create_frame_1():
    e =Category1Frame(root_frame)
"""


"""button1 = customtkinter.CTkButton(master=root_frame, text="show1", command=create_frame_1)
button1.pack()
"""


root.mainloop()




"""        categoryframe.pack(fill="both", expand=True)

        self.classbutton = customtkinter.CTkButton(categoryframe, text="framebutton")
        self.classbutton.pack()

class Category2Frame:
    def __init__(self, master):
        categoryframe = customtkinter.CTkFrame(master, fg_color="blue")
        categoryframe.pack(fill="both", expand=True)

        self.classbutton = customtkinter.CTkButton(categoryframe, text="framebutton")
        self.classbutton.pack()

def showframe(args):
    if args == 1:
        e = Category1Frame(root)
    else:
        Category1Frame.packforget()


button1 = customtkinter.CTkButton(master=root, text="show1", command=lambda:showframe(1))
button2 = customtkinter.CTkButton(master=root, text="show2", command=lambda:showframe(2))
button1.pack()
button2.pack()

"""



"""class MyButton(Button):

    def __init__(self, text, *args, **kwargs):
        self.text = text



btn1 = MyButton(root, "heisann")
btn1.pack()

btn = tkinter.Button(master=root, text="Hallo")
btn.pack()

class Softwarebutton(customtkinter.CTkButton):
    def __init__(self, master, text, fg_color, image):
        super().__init__()
        self.master = master
        self.text = text
        self.fg_color = fg_color
        self.image = image



vlc_check = Softwarebutton(standardpakke_frame, "VLC", "red", vlc_image)
vlc_check.pack()"""