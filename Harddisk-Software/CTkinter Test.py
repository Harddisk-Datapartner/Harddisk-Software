from tkinter import Tk, ttk 
import tkinter
from tkinter import font
import customtkinter
from PIL import Image, ImageTk
import time

customtkinter.set_appearance_mode("dark")  # Modes: "System" (standard), "Dark", "Light"
"""customtkinter.set_default_color_theme("blue")  # Themes: "blue" (standard), "green", "dark-blue"""

# Harddisk colors. Blue = "#0B57C2" Orange = "#F5681C"
# (dark mode) Gray colors. Dark = #292929 brighter = #383838
# (light mode) Gray colors. Dark = #d1d0cf brighter = #c4c3c2  #c4c3c2

root = customtkinter.CTk()  # create CTk window like you do with the Tk window
root.title("Harddisk Datapartner")
root.iconbitmap(default="Logos\HDDLOGO.ico")

root_width = 1440
root_height = 810
screen_width = root.winfo_screenwidth()
screen_height = root.winfo_screenheight()
screen_x = (screen_width / 2) - (root_width / 2)
screen_y = (screen_height / 2) - (root_height / 2)
root.geometry(f"{root_width}x{root_height}+{int(screen_x)}+{int(screen_y)}")

image_size = 55
logo_image_width = 90
logo_image_height = 70


class ToolTip(object):
    def __init__(self, widget, text):
        self.widget = widget
        self.text = text

        def enter(event):
            self.showTooltip()
        def leave(event):
            self.hideTooltip()
        widget.bind('<Enter>', enter)
        widget.bind('<Leave>', leave)

    def showTooltip(self):
        self.tooltipwindow = tw = tkinter.Toplevel(self.widget)
        tw.wm_overrideredirect(1) # window without border and no normal means of closing
        tw.wm_geometry("+{}+{}".format(self.widget.winfo_rootx(), self.widget.winfo_rooty()))
        tooltip_label = tkinter.Label(tw, text = self.text, background = "#d9dedb", relief = 'solid', borderwidth = 1).pack()

    def hideTooltip(self):
        tw = self.tooltipwindow
        tw.destroy()
        """self.tooltipwindow = None"""

# ==========LEFT FRAME==========
left_frame = customtkinter.CTkFrame(master=root, 
                                        fg_color=("#d1d0cf", "#292929"), 
                                        corner_radius=15)
left_frame.pack(side="left", pady=5, padx=5, fill="y", expand=False)

# ==========HEADLINE LOGO==========
headline_image = ImageTk.PhotoImage(Image.open("Logos\Fulltextlogo.png").resize((400, 55)))
headline_label = customtkinter.CTkLabel(master=root, 
                                            fg_color=("#d1d0cf", "#292929"), 
                                            height=50, 
                                            corner_radius=15, 
                                            image=headline_image, text="")
headline_label.pack(pady=5, padx=5, ipadx=5, ipady=5, side="top", fill="x")

# ==========Home screen (Packing because it's home screen)==========
home_frame = customtkinter.CTkFrame(master=root, 
                                        fg_color=("#d1d0cf", "#292929"), 
                                        corner_radius=15)
home_frame.pack(pady=5, padx=5, fill="both", expand=True)

home_headline_frame = customtkinter.CTkFrame(master=home_frame, 
                                                fg_color=("#d1d0cf", "#292929"), 
                                                corner_radius=15, 
                                                height=50)
home_headline_frame.pack(pady=10, padx=10, fill="x")

home_main_label = customtkinter.CTkLabel(master=home_frame, 
                                            fg_color=("#c4c3c2", "#383838"), 
                                            corner_radius=15, 
                                            text="HEI OG VELKOMMEN TIL BLAH BLAH \n Her kan du blah blah \n Og du kan blah blah blah", 
                                            text_font=("Roboto Medium", 30)) 
home_main_label.pack(expand=True, fill="x", side="bottom")



software_list = "cmd /k "
#Functions executed from buttons.
def toggle_vlc():
    global software_list
    software_list += "winget install VideoLAN.VLC -e && "
    print(software_list)
    print(software_list.replace("winget install VideoLAN.VLC -e && ", "" ))
    print(software_list)


"""    cmd_vlc = "winget install VideoLAN.VLC -e && "
    
    if cmd_vlc in software_list:
        software_list.replace(cmd_vlc, "")
    else:
        software_list += cmd_vlc 
    print(software_list)"""

def toggle_firefox():
    global software_list
    software_list.replace("winget install VideoLAN.VLC -e &&", "test")
    """software_list += "winget install Mozilla.Firefox -e && """
    print(software_list)

def toggle_spotify():
    global software_list
    software_list += "winget install Spotify.Spotify -e && "
    print(software_list)

def toggle_teamviewer():
    global software_list
    software_list += "winget install Teamviewer.Teamviewer -e && "
    print(software_list)

def toggle_steam():
    global software_list
    software_list += "winget install Valve.Steam -e && "
    print(software_list)

def toggle_discord():
    global software_list
    software_list += "winget install Discord.Discord -e && "
    print(software_list)



# ==========Install screen (No packing)==========

# ==========Sets up the main installation frame==========
install_frame = customtkinter.CTkFrame(master=root, 
                                            fg_color=("#d1d0cf", "#292929"), 
                                            corner_radius=15)

# ==========Sets up the installation headline frame and label/text==========
install_headline_frame = customtkinter.CTkFrame(master=install_frame, 
                                                    fg_color=("#c4c3c2", "#383838"), 
                                                    corner_radius=15)

install_headline_label = customtkinter.CTkLabel(master=install_headline_frame, 
                                                    text="INSTALLER PROGRAMVARE", 
                                                    text_font=("Roboto Medium", 20))

software1_frame = customtkinter.CTkFrame(master=install_frame, 
                                                    fg_color=("#c4c3c2", "#383838"), 
                                                    corner_radius=15)

software1_label = customtkinter.CTkLabel(master=software1_frame, 
                                                fg_color=("#c4c3c2", "#383838"), 
                                                text="Programvare rad 1", 
                                                text_font=("Roboto Medium", 15), 
                                                corner_radius=15)

# ==========Sets up the bottom frame with install, update and uninstall buttons==========
install_bottom_frame = customtkinter.CTkFrame(master=root, 
                                                    fg_color=("#d1d0cf", "#292929"), 
                                                    corner_radius=15)

install_selected_button = customtkinter.CTkButton(master=install_bottom_frame, 
                                                                fg_color="#0b57c2", 
                                                                hover_color="#F5681C", 
                                                                text="Installer Valgte", 
                                                                text_font=("Roboto Medium", 20), 
                                                                corner_radius=10)
                                                                

update_selected_button = customtkinter.CTkButton(master=install_bottom_frame, 
                                                                fg_color="#0b57c2", 
                                                                hover_color="#F5681C", 
                                                                text="Oppdater Valgte", 
                                                                text_font=("Roboto Medium", 20),
                                                                corner_radius=10)

uninstall_selected_button = customtkinter.CTkButton(master=install_bottom_frame, 
                                                                fg_color="#0b57c2", 
                                                                hover_color="#F5681C", 
                                                                text="Avinstaller Valgte", 
                                                                text_font=("Roboto Medium", 20),
                                                                corner_radius=10)

# ==========Sofware Buttons==========
vlc_image = ImageTk.PhotoImage(Image.open("Logos\\128x128\\VLC 128x128.png").resize((image_size, image_size)))
"""vlc_check = ttk.Checkbutton(software1_frame, image=vlc_image, text="VLC", compound="left")"""
vlc_check = customtkinter.CTkButton(software1_frame, fg_color="#0b57c2", hover_color="#F5681C", text ="VLC", text_font=("Roboto Medium", 20), image=vlc_image, command=toggle_vlc)
ToolTip(widget = vlc_check, text = "Beskrivelse av Firefox")

firefox_image = ImageTk.PhotoImage(Image.open("Logos\\128x128\\Firefox 128x128.png").resize((image_size, image_size)))
firefox_check = customtkinter.CTkButton(software1_frame, fg_color="#0b57c2", hover_color="#F5681C", text ="Firefox", text_font=("Roboto Medium", 20), image=firefox_image, command=toggle_firefox)
ToolTip(widget = firefox_check, text = "Beskrivelse av Firefox")

spotify_image = ImageTk.PhotoImage(Image.open("Logos\\128x128\\Spotify 128x128.png").resize((image_size, image_size)))
spotify_check = customtkinter.CTkButton(software1_frame, fg_color="#0b57c2", hover_color="#F5681C", text ="Spotify", text_font=("Roboto Medium", 20), image=spotify_image, command=toggle_spotify)
ToolTip(widget = spotify_check, text = "Beskrivelse av Spotify")

teamwiever_image = ImageTk.PhotoImage(Image.open("Logos\\128x128\\Teamviewer 128x128.png").resize((image_size, image_size)))
teamviewer_check = customtkinter.CTkButton(software1_frame, fg_color="#0b57c2", hover_color="#F5681C", text ="Teamwiever", text_font=("Roboto Medium", 20), image=teamwiever_image, command=toggle_teamviewer)
ToolTip(widget = teamviewer_check, text = "Beskrivelse av Teamviewer")

steam_image = ImageTk.PhotoImage(Image.open("Logos\\128x128\\Steam 128x128.png").resize((image_size, image_size)))
steam_check = customtkinter.CTkButton(software1_frame, fg_color="#0b57c2", hover_color="#F5681C", text ="Steam", text_font=("Roboto Medium", 20), image=steam_image, command=toggle_steam)
ToolTip(widget = steam_check, text = "Beskrivelse av Steam")

discord_image = ImageTk.PhotoImage(Image.open("Logos\\128x128\\Discord 128x128.png").resize((image_size, image_size)))
discord_check = customtkinter.CTkButton(software1_frame, fg_color="#0b57c2", hover_color="#F5681C", text ="Discord", text_font=("Roboto Medium", 20), image=discord_image, command=toggle_discord)
ToolTip(widget = discord_check, text = "Beskrivelse av Discord")

# ==========Support screen (No packing)==========
support_frame = customtkinter.CTkFrame(master=root, 
                                            fg_color=("#d1d0cf", "#292929"), 
                                            corner_radius=15)

support_headline_frame = customtkinter.CTkFrame(master=support_frame, 
                                                        fg_color=("#c4c3c2", "#383838"), 
                                                        corner_radius=15, 
                                                        height=50)

support_headline_label = customtkinter.CTkLabel(master=support_headline_frame, 
                                                            text="Hjelp, support, kontakt oss", 
                                                            text_font=("Roboto Medium", 20))
support_main_label = customtkinter.CTkLabel(master=support_frame, 
                                                            fg_color=("#c4c3c2", "#383838"), 
                                                            corner_radius=15, 
                                                            text="Kontakt oss blah blah \n Support Support Support \n Support Support Support \n Support Support Support ", 
                                                            text_font=("Roboto Medium", 30))




# ==========Left frame buttons. Packing and unpacking widgets==========
def clicked_home():
    print("Clicked home")
    install_frame.pack_forget()
    support_frame.pack_forget()
    install_bottom_frame.pack_forget()

    home_frame.pack(pady=5, padx=5, fill="both", expand=True)
    home_headline_frame.pack(pady=10, padx=10, fill="x")


def clicked_install_software():
    print("Clicked install software")
    home_frame.pack_forget()
    support_frame.pack_forget()

    install_frame.pack(pady=5, padx=5, fill="both", expand=True)
    install_headline_frame.pack(pady=5, padx=5, fill="x")
    install_headline_label.pack()

    software1_frame.pack(pady=5, padx=5, fill="x", expand=False)
    software1_label.pack(pady=5, padx=5, fill="x", expand=True)
    vlc_check.pack(side="left", pady=5, padx=5)
    firefox_check.pack(side="left", pady=5, padx=5)
    spotify_check.pack(side="left", pady=5, padx=5)
    teamviewer_check.pack(side="left", pady=5, padx=5)
    steam_check.pack(side="left", pady=5, padx=5)
    discord_check.pack(side="left", pady=5, padx=5)

    # ==========Packs the bottom frame with install, update and uninstall buttons==========
    install_bottom_frame.pack(pady=5, padx=5, fill="x", expand=False, side="bottom")
    uninstall_selected_button.pack(pady=5, padx=105, side="left")
    update_selected_button.pack(pady=5, padx=105, side="left")
    install_selected_button.pack(pady=5, padx=105, side="left")



def clicked_support():
    print("Clicked support")
    home_frame.pack_forget()
    install_frame.pack_forget()
    install_bottom_frame.pack_forget()

    support_frame.pack(pady=5, padx=5, fill="both", expand=True)
    support_main_label.pack(expand=True, side="bottom")
    support_headline_frame.pack(pady=5, padx=5, fill="x")
    support_headline_label.pack()


def change_mode():
        if mode_switch.get() == 1:
            customtkinter.set_appearance_mode("dark")
        else:
            customtkinter.set_appearance_mode("light")
        



# ==========LEFT FRAME BUTTONS==========
logo_image = ImageTk.PhotoImage(Image.open("Logos\Menu icons\HDDLOGO.png").resize((logo_image_width, logo_image_height)))
logo_label = customtkinter.CTkLabel(master=left_frame, text="", image=logo_image)
logo_label.pack(pady=20, fill="both", expand=False)

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