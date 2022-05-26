from doctest import master
from select import select
from sre_parse import State
import tkinter
from turtle import left, mode
import customtkinter
from PIL import Image, ImageTk

customtkinter.set_appearance_mode("dark")  # Modes: "System" (standard), "Dark", "Light"
"""customtkinter.set_default_color_theme("blue")  # Themes: "blue" (standard), "green", "dark-blue"""

# Harddisk colors. Blue = "#0B57C2" Orange = "#F5681C"

root = customtkinter.CTk()  # create CTk window like you do with the Tk window
root.title("Harddisk Datapartner")
root.iconbitmap(default="Logos\HDDLOGO.ico")

"""image = Image.open("Logos\Menu icons\Background.png")
bg_image = ImageTk.PhotoImage(image)
image_label = tkinter.Label(master=root, image=bg_image)
image_label.place(relx=0.5, rely=0.5, anchor=tkinter.CENTER)"""



root_width = 960
root_height = 540
screen_width = root.winfo_screenwidth()
screen_height = root.winfo_screenheight()
screen_x = (screen_width / 2) - (root_width / 2)
screen_y = (screen_height / 2) - (root_height / 2)
root.geometry(f"{root_width}x{root_height}+{int(screen_x)}+{int(screen_y)}")


left_frame = customtkinter.CTkFrame(master=root, fg_color=("gray50", "#292929"), corner_radius=15)
left_frame.pack(side="left", pady=5, padx=5, fill="y", expand=False)

main_frame = customtkinter.CTkFrame(master=root, fg_color=("gray50", "#292929"), corner_radius=15)
main_frame.pack(pady=5, padx=5, fill="both", expand=True)

headline_frame = customtkinter.CTkFrame(master=main_frame, fg_color="#0B57C2", corner_radius=15, height=50)
headline_frame.pack(pady=10, padx=10, fill="x")

install_headline_label = customtkinter.CTkLabel(master=headline_frame, text="Velg programvare", text_font=("Roboto Medium", 20))
install_headline_label.pack()

support_headline_label = customtkinter.CTkLabel(master=headline_frame, text="support", text_font=("Roboto Medium", 20))
support_headline_label.pack()


def clicked_home():
    print("Clicked home")

def clicked_install_software():
    print("Clicked install software")

def clicked_support():
    print("Clicked support")
    support_headline_label = customtkinter.CTkLabel(master=headline_frame, text="support", text_font=("Roboto Medium", 20))
    support_headline_label.pack()

def change_mode():
        if mode_switch.get() == 1:
            customtkinter.set_appearance_mode("dark")
        else:
            customtkinter.set_appearance_mode("light")
        


image_size = 55
logo_image_width = 90
logo_image_height = 70



logo_image = ImageTk.PhotoImage(Image.open("Logos\Menu icons\HDDLOGO.png").resize((logo_image_width, logo_image_height)))
logo_label = customtkinter.CTkLabel(master=left_frame, text="", image=logo_image)
logo_label.pack(pady=20, fill="both", expand=False)
""""fg_color="#4d4d4b"""

home_image = ImageTk.PhotoImage(Image.open("Logos\\Menu icons\\Home.png").resize((image_size, image_size)))
home_button = customtkinter.CTkButton(master=left_frame, command=clicked_home, fg_color="#0b57c2", hover_color="#F5681C", text="", width=80, height=80, image=home_image)
home_button.pack(pady=10, padx=10)

install_software_image = ImageTk.PhotoImage(Image.open("Logos\Menu icons\Download.png").resize((image_size, image_size)))
install_software_button = customtkinter.CTkButton(master=left_frame, command=clicked_install_software, fg_color="#0b57c2", hover_color="#F5681C", text="", width=80, height=80, image=install_software_image)
install_software_button.pack(pady=10, padx=10)

support_image = ImageTk.PhotoImage(Image.open("Logos\Menu icons\Support.png").resize((image_size, image_size)))
support_button = customtkinter.CTkButton(master=left_frame, command=clicked_support, fg_color="#0b57c2", hover_color="#F5681C", text="", width=80, height=80, image=support_image)
support_button.pack(pady=10, padx=10)

mode_switch = customtkinter.CTkSwitch(master=left_frame, text="Dark Mode", command=change_mode)
mode_switch.select()
mode_switch.pack(side="bottom", pady=20)




root.mainloop()