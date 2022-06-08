from tkinter import *
import customtkinter

root = customtkinter.CTk()
root_width = 1440
root_height = 810

root_frame = customtkinter.CTkFrame(master=root, fg_color="cyan")
root_frame.pack(fill="both", expand=True)



class Category1Frame:
    def __init__(self, master):
        categoryframe = customtkinter.CTkFrame(master, fg_color="red")
        categorylabel = customtkinter.CTkLabel(master, fg_color="blue")

def showframe(args, Category1Frame):
    if args == 1:
        categoryframe.pack()
        categorylabel.pack()



button1 = customtkinter.CTkButton(master=root, text="show1", command=lambda:showframe(1))


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