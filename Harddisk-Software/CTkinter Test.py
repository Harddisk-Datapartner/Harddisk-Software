from tkinter import Frame, Tk, ttk 
import tkinter
from tkinter import font
from turtle import home
import customtkinter
from PIL import Image, ImageTk


customtkinter.set_appearance_mode("dark")  # Modes: "System" (standard), "Dark", "Light"
"""customtkinter.set_default_color_theme("blue")  # Themes: "blue" (standard), "green", "dark-blue"""

# Harddisk colors. Blue = "#0B57C2" Orange = "#F5681C"
# (dark mode) Gray colors. Dark = #292929 brighter = #383838
# (light mode) Gray colors. Dark = #d1d0cf brighter = #c4c3c2

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

# ==========Create Images==========
image_size = 55

logo_image = ImageTk.PhotoImage(Image.open("Logos\Menu icons\HDDLOGO.png").resize((90, 70)))
headline_image = ImageTk.PhotoImage(Image.open("Logos\Fulltextlogo.png").resize((400, 55)))
home_image = ImageTk.PhotoImage(Image.open("Logos\\Menu icons\\Home.png").resize((image_size, image_size)))
install_software_image = ImageTk.PhotoImage(Image.open("Logos\Menu icons\Download.png").resize((image_size, image_size)))
support_image = ImageTk.PhotoImage(Image.open("Logos\Menu icons\Support.png").resize((image_size, image_size)))

# ==========Software Images==========

# Browsers/Nettlesere
firefox_image = ImageTk.PhotoImage(Image.open("Logos\\128x128\\Firefox 128x128.png").resize((image_size, image_size)))
vlc_image = ImageTk.PhotoImage(Image.open("Logos\\128x128\\VLC 128x128.png").resize((image_size, image_size)))
spotify_image = ImageTk.PhotoImage(Image.open("Logos\\128x128\\Spotify 128x128.png").resize((image_size, image_size)))
"""chrome_image =
Brave_image =
vivaldi_image =
duckduckgo_image =

# Email Clients/Epost klienter
emclient_image =
thunderbird_image =

# Document management/Dokumentbehandling
adobe_reader_image = 
libreoffice_image =
openoffice_image = 
evernote_image = 
onenote_image = 

# Media
spotify
vlc
itunes_image = 
tidal_image = 
k_lite_codec = 

#Photo editing/Bilderedigering
gimp_image = 
irfanview_image = 
greenshot_image = 

#Games/Spill
steam_image = ImageTk.PhotoImage(Image.open("Logos\\128x128\\Steam 128x128.png").resize((image_size, image_size)))
epic_games_image = 
gog_image =
origin_image= 
blizz_image = 
ubisoft_image = 

# Compression/Komprimering
peazip_image =
sevenzip_image = 

# RGB
openrgb_image = 
icue_image = 
nzxt_image = 
msi_image = 
gigabyte_rgb_image = 
lianli_image = 
# asus armory crate

#Communtication/Kommunikasjon
discord_image = ImageTk.PhotoImage(Image.open("Logos\\128x128\\Discord 128x128.png").resize((image_size, image_size)))
teamwiever_image = ImageTk.PhotoImage(Image.open("Logos\\128x128\\Teamviewer 128x128.png").resize((image_size, image_size)))
skype_image = 
zoom_image = 

# Streaming
obs_image = 
shadowplay_image = 
elgato_image = 

# Drivers
intel_ds_image = 
amd_image = 
nv_ci_image = 
nvidia_ge_image = 
asus_ac_image = 
gigabyte_app_image = 
lenovo_su_image = """

# ==========Hover tooltip==========
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
        tooltip_label = tkinter.Label(tw, text = self.text, background = "#383838", relief = 'solid', borderwidth = 1).pack()

    def hideTooltip(self):
        tw = self.tooltipwindow
        tw.destroy()
        """self.tooltipwindow = None"""



# ==========Softwarelist base varaible==========
software_list = "cmd /k "

# ==========Functions executed from buttons.==========
def toggle_vlc():
    global software_list
    cmd_vlc = "winget install VideoLAN.VLC -e && "
    if "VideoLAN.VLC" in software_list:
        software_list.replace(cmd_vlc, "bæsj")
        chosen_vlc_label.pack_forget()
        print("false")
    else:
        software_list += cmd_vlc
        chosen_vlc_label.pack(side="left")
        print("True")

        
    print(software_list)


"""    cmd_vlc = "winget install VideoLAN.VLC -e && "
    
    if cmd_vlc in software_list:
        software_list.replace(cmd_vlc, "")
    else:
        software_list += cmd_vlc 
    print(software_list)"""

def toggle_firefox():
    global software_list
    cmd_firefox = "winget install Mozilla.Firefox -e && "
    if "VideoLAN.VLC" in software_list:
        software_list.replace(cmd_firefox, "")
        chosen_firefox_label.pack_forget()
    else:
        software_list += cmd_firefox
        chosen_firefox_label.pack(side="left")
    print(software_list)

def toggle_spotify():
    global software_list
    chosen_spotify_label.pack(side="left")
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


        
        
# ==========LEFT FRAME (Packing because it's home screen)==========
left_frame = customtkinter.CTkFrame(master=root, 
                                        fg_color=("#d1d0cf", "#292929"), 
                                        corner_radius=15)
left_frame.pack(side="left", pady=5, padx=5, fill="y", expand=False)

# ==========HEADLINE LOGO==========
headline_label = customtkinter.CTkLabel(master=root, 
                                            fg_color=("#d1d0cf", "#292929"), 
                                            height=50, 
                                            corner_radius=15, 
                                            image = headline_image, 
                                            text="")
headline_label.pack(pady=5, padx=5, ipadx=5, ipady=5, side="top", fill="x")

# ==========HOME SCREEN (Packing because it's home screen)==========
home_frame = customtkinter.CTkFrame(master=root, 
                                        fg_color=("#d1d0cf", "#292929"), 
                                        corner_radius=15)
home_frame.pack(pady=5, padx=5, fill="both", expand=True)

home_headline_frame = customtkinter.CTkFrame(master=home_frame, 
                                                fg_color=("#d1d0cf", "#292929"), 
                                                corner_radius=15, 
                                                height=50)
home_headline_frame.pack(pady=10, padx=10, fill="x")

with open("Text\Hjem.txt") as r:
    home_text = r.read()

home_main_label = customtkinter.CTkLabel(master=home_frame, 
                                            fg_color=("#c4c3c2", "#383838"), 
                                            corner_radius=15, 
                                            text=home_text, 
                                            text_font=("Roboto Medium", 13)) 
home_main_label.pack(pady=10, padx=10, expand=True, fill="x", side="bottom")



# ==========INSTALL SCREEN (No packing)==========

# ==========Sets up the main installation frame==========
install_frame = customtkinter.CTkFrame(master=root, 
                                                fg_color=("#d1d0cf", "#292929"), 
                                                corner_radius=15)

# ==========Sets up the installation headline frame and label/text==========
install_headline_frame = customtkinter.CTkFrame(master=install_frame, 
                                                fg_color=("#c4c3c2", "#383838"), 
                                                height= 20, 
                                                corner_radius=15)

install_headline_label = customtkinter.CTkLabel(master=install_headline_frame, 
                                                text="INSTALLER PROGRAMVARE", 
                                                text_font=("Roboto Medium", 20), 
                                                corner_radius=15)


# ==========Sets up "Standardpakken" screen. ("Home page" of the software installation screen)==========
standardpakke_frame = customtkinter.CTkFrame(master=install_frame, 
                                                fg_color=("#c4c3c2", "#383838"), 
                                                corner_radius=15)



standardpakke_label = customtkinter.CTkLabel(master=standardpakke_frame, 
                                                fg_color=("#c4c3c2", "#383838"), 
                                                text="^^^^ Velg programvare kategorier over ^^^^", 
                                                text_font=("Roboto Medium", 30), 
                                                corner_radius=15)

# ==========Sets up software tabs label==========
software_tabs_frame = customtkinter.CTkFrame(master=install_frame, 
                                                fg_color=("#c4c3c2", "#383838"), 
                                                height= 20, 
                                                corner_radius=15)

software_tabs_filler_left = customtkinter.CTkFrame(master=software_tabs_frame, 
                                                fg_color=("#c4c3c2", "#383838"), 
                                                height=5, 
                                                width=20, 
                                                corner_radius=15)

software_tabs_filler_right = customtkinter.CTkFrame(master=software_tabs_frame, 
                                                fg_color=("#c4c3c2", "#383838"), 
                                                height=5, 
                                                width=20,  
                                                corner_radius=15)



# ==========Sets up the bottom frame with install, update and uninstall buttons==========
install_bottom_frame = customtkinter.CTkFrame(master=root, 
                                                                fg_color=("#d1d0cf", "#292929"), 
                                                                corner_radius=15)

install_selected_button = customtkinter.CTkButton(master=install_bottom_frame, 
                                                                fg_color="#0b57c2", 
                                                                hover_color="#F5681C", 
                                                                text="  Installer Valgte  ", 
                                                                text_font=("Roboto Medium", 20), 
                                                                corner_radius=15)
                                                                

update_selected_button = customtkinter.CTkButton(master=install_bottom_frame, 
                                                                fg_color="#0b57c2", 
                                                                hover_color="#F5681C", 
                                                                text=" Oppdater Valgte ", 
                                                                text_font=("Roboto Medium", 20),
                                                                corner_radius=15)

uninstall_selected_button = customtkinter.CTkButton(master=install_bottom_frame, 
                                                                fg_color="#0b57c2", 
                                                                hover_color="#F5681C", 
                                                                text="Avinstaller Valgte", 
                                                                text_font=("Roboto Medium", 20),
                                                                corner_radius=15)

chosen_software_main_frame = customtkinter.CTkFrame(master=root, 
                                                        fg_color=("#d1d0cf", "#292929"), 
                                                        height=145, 
                                                        corner_radius=15)

chosen_software_frame1 = customtkinter.CTkFrame(master=chosen_software_main_frame, 
                                                        fg_color=("#d1d0cf", "yellow"), 
                                                        height=36.25, 
                                                        corner_radius=15)

chosen_software_frame2 = customtkinter.CTkFrame(master=chosen_software_main_frame, 
                                                        fg_color=("#d1d0cf", "green"), 
                                                        height=36.25,
                                                        corner_radius=15)

chosen_software_frame3 = customtkinter.CTkFrame(master=chosen_software_main_frame, 
                                                        fg_color=("#d1d0cf", "red"),
                                                        height=36.25, 
                                                        corner_radius=15)

chosen_software_frame4 = customtkinter.CTkFrame(master=chosen_software_main_frame, 
                                                        fg_color=("#d1d0cf", "blue"), 
                                                        height=36.25, 
                                                        corner_radius=15)




chosen_vlc_label = customtkinter.CTkLabel(master = chosen_software_main_frame, image=vlc_image, height=145)
chosen_firefox_label = customtkinter.CTkLabel(master = chosen_software_main_frame, image=firefox_image, height=145)
chosen_spotify_label = customtkinter.CTkLabel(master = chosen_software_main_frame, image=spotify_image, height=145)

# ==========Support screen (No packing)==========
support_frame = customtkinter.CTkFrame(master=root, 
                                                    fg_color=("#d1d0cf", "#292929"), 
                                                    corner_radius=15)

support_headline_frame = customtkinter.CTkFrame(master=support_frame, 
                                                    fg_color=("#c4c3c2", "#383838"), 
                                                    corner_radius=15, 
                                                    height=20)

support_headline_label = customtkinter.CTkLabel(master=support_headline_frame, 
                                                    text="Hjelp, support, kontakt oss", 
                                                    text_font=("Roboto Medium", 20))

with open("Text\Support.txt") as r:
    support_text = r.read()
support_main_label = customtkinter.CTkLabel(master=support_frame, 
                                                    fg_color=("#c4c3c2", "#383838"), 
                                                    corner_radius=15, 
                                                    text=support_text, 
                                                    text_font=("Roboto Medium", 1))


# ==========Software Tabs Buttons==========
category1_button = customtkinter.CTkButton(master=software_tabs_frame, 
                                                                fg_color="#0b57c2", 
                                                                hover_color="#F5681C", 
                                                                text="1", 
                                                                text_font=("Roboto Medium", 20),
                                                                width=85, 
                                                                corner_radius=15)

category2_button = customtkinter.CTkButton(master=software_tabs_frame, 
                                                                fg_color="#0b57c2", 
                                                                hover_color="#F5681C", 
                                                                text="2", 
                                                                text_font=("Roboto Medium", 20), 
                                                                width=85, 
                                                                corner_radius=15)

category3_button = customtkinter.CTkButton(master=software_tabs_frame, 
                                                                fg_color="#0b57c2", 
                                                                hover_color="#F5681C", 
                                                                text="3", 
                                                                text_font=("Roboto Medium", 20), 
                                                                width=85, 
                                                                corner_radius=15)

category4_button = customtkinter.CTkButton(master=software_tabs_frame, 
                                                                fg_color="#0b57c2", 
                                                                hover_color="#F5681C", 
                                                                text="4", 
                                                                text_font=("Roboto Medium", 20), 
                                                                width=85, 
                                                                corner_radius=15)


category5_button = customtkinter.CTkButton(master=software_tabs_frame, 
                                                                fg_color="#0b57c2", 
                                                                hover_color="#F5681C", 
                                                                text="5", 
                                                                text_font=("Roboto Medium", 20), 
                                                                width=85, 
                                                                corner_radius=15)

category6_button = customtkinter.CTkButton(master=software_tabs_frame, 
                                                                fg_color="#0b57c2", 
                                                                hover_color="#F5681C", 
                                                                text="6", 
                                                                text_font=("Roboto Medium", 20), 
                                                                width=85, 
                                                                corner_radius=15)

category7_button = customtkinter.CTkButton(master=software_tabs_frame, 
                                                                fg_color="#0b57c2", 
                                                                hover_color="#F5681C", 
                                                                text="7", 
                                                                text_font=("Roboto Medium", 20), 
                                                                width=85, 
                                                                corner_radius=15)

category8_button = customtkinter.CTkButton(master=software_tabs_frame, 
                                                                fg_color="#0b57c2", 
                                                                hover_color="#F5681C", 
                                                                text="8", 
                                                                text_font=("Roboto Medium", 20), 
                                                                width=85, 
                                                                corner_radius=15)

category9_button = customtkinter.CTkButton(master=software_tabs_frame, 
                                                                fg_color="#0b57c2", 
                                                                hover_color="#F5681C", 
                                                                text="9", 
                                                                text_font=("Roboto Medium", 20), 
                                                                width=85, 
                                                                corner_radius=15)

category10_button = customtkinter.CTkButton(master=software_tabs_frame, 
                                                                fg_color="#0b57c2", 
                                                                hover_color="#F5681C", 
                                                                text="10", 
                                                                text_font=("Roboto Medium", 20), 
                                                                width=85, 
                                                                corner_radius=15)

category11_button = customtkinter.CTkButton(master=software_tabs_frame, 
                                                                fg_color="#0b57c2", 
                                                                hover_color="#F5681C", 
                                                                text="11", 
                                                                text_font=("Roboto Medium", 20), 
                                                                width=85, 
                                                                corner_radius=15)

category12_button = customtkinter.CTkButton(master=software_tabs_frame, 
                                                                fg_color="#0b57c2", 
                                                                hover_color="#F5681C", 
                                                                text="12", 
                                                                text_font=("Roboto Medium", 20), 
                                                                width=85, 
                                                                corner_radius=15)

category13_button = customtkinter.CTkButton(master=software_tabs_frame, 
                                                                fg_color="#0b57c2", 
                                                                hover_color="#F5681C", 
                                                                text="13", 
                                                                text_font=("Roboto Medium", 20), 
                                                                width=85, 
                                                                corner_radius=15)


# ==========Sofware Buttons==========

vlc_check = customtkinter.CTkButton(standardpakke_frame, fg_color="#0b57c2", hover_color="#F5681C", text ="VLC", text_font=("Roboto Medium", 20), image=vlc_image, command=toggle_vlc)

firefox_check = customtkinter.CTkButton(standardpakke_frame, fg_color="#0b57c2", hover_color="#F5681C", text ="Firefox", text_font=("Roboto Medium", 20), image=firefox_image, command=toggle_firefox)

spotify_check = customtkinter.CTkButton(standardpakke_frame, fg_color="#0b57c2", hover_color="#F5681C", text ="Spotify", text_font=("Roboto Medium", 20), image=spotify_image, command=toggle_spotify)

"""teamviewer_check = customtkinter.CTkButton(software1_frame, fg_color="#0b57c2", hover_color="#F5681C", text ="Teamwiever", text_font=("Roboto Medium", 20), image=teamwiever_image, command=toggle_teamviewer)
ToolTip(widget = teamviewer_check, text = "Beskrivelse av Teamviewer")

steam_check = customtkinter.CTkButton(software1_frame, fg_color="#0b57c2", hover_color="#F5681C", text ="Steam", text_font=("Roboto Medium", 20), image=steam_image, command=toggle_steam)
ToolTip(widget = steam_check, text = "Beskrivelse av Steam")

discord_check = customtkinter.CTkButton(software1_frame, fg_color="#0b57c2", hover_color="#F5681C", text ="Discord", text_font=("Roboto Medium", 20), image=discord_image, command=toggle_discord)
ToolTip(widget = discord_check, text = "Beskrivelse av Discord")"""


# ==========Left frame buttons. Packing and unpacking widgets==========
# ==========PACK/TOGGLE HOME PAGE==========
def clicked_home():
    print("Clicked home")
    install_frame.pack_forget()
    support_frame.pack_forget()
    install_bottom_frame.pack_forget()
    chosen_software_main_frame.pack_forget()

    home_frame.pack(pady=5, padx=5, fill="both", expand=True)
    home_headline_frame.pack(pady=10, padx=10, fill="x")

# ==========PACK/TOGGLE INSTALL PAGE==========
def clicked_install_software():
    print("Clicked install software")
    home_frame.pack_forget()
    support_frame.pack_forget()

    install_frame.pack(padx=5, fill="both", expand=True)
    install_headline_frame.pack(pady=5, padx=5, fill="x")
    install_headline_label.pack()
    software_tabs_frame.pack(padx=5, fill="x")
    standardpakke_frame.pack(pady=5, padx=5, fill="both", expand=True)
    """standardpakke_headline_label.pack(pady=5, padx=5, fill="x")"""
    standardpakke_label.pack(pady=5, padx=5, fill="both")
    software_tabs_frame.pack(ipadx=5, fill="x")
    software_tabs_filler_left.pack(side="left")
    software_tabs_filler_right.pack(side="right")


    firefox_check.pack()
    spotify_check.pack()
    vlc_check.pack()


    category1_button.pack(pady=5, padx=5, side="left")
    category2_button.pack(pady=5, padx=5, side="left")
    category3_button.pack(pady=5, padx=5, side="left")
    category4_button.pack(pady=5, padx=5, side="left")
    category5_button.pack(pady=5, padx=5, side="left")
    category6_button.pack(pady=5, padx=5, side="left")
    category7_button.pack(pady=5, padx=5, side="left")
    category8_button.pack(pady=5, padx=5, side="left")
    category9_button.pack(pady=5, padx=5, side="left")
    category10_button.pack(pady=5, padx=5, side="left")
    category11_button.pack(pady=5, padx=5, side="left")
    category12_button.pack(pady=5, padx=5, side="left")
    category13_button.pack(pady=5, padx=5, side="left")


    # ==========Packs the bottom frame with install, update and uninstall buttons==========
    install_bottom_frame.pack(pady=5, padx=5, fill="y", expand=False, side="left")
    install_selected_button.pack(pady=5, padx=5, side="top")
    update_selected_button.pack(pady=5, padx=5, side="top")
    uninstall_selected_button.pack(pady=5, padx=5, side="bottom")

    chosen_software_main_frame.pack(pady=5, padx=5, fill="x", expand=True, side="right")
"""    chosen_software_frame1.pack(fill="x")
    chosen_software_frame2.pack(fill="x")
    chosen_software_frame3.pack(fill="x")
    chosen_software_frame4.pack(fill="x")
    """
    


# ==========PACK/TOGGLE SUPPORT PAGE==========
def clicked_support():
    print("Clicked support")
    home_frame.pack_forget()
    install_frame.pack_forget()
    install_bottom_frame.pack_forget()
    chosen_software_main_frame.pack_forget()


    support_frame.pack(pady=5, padx=5, fill="both", expand=True)
    support_main_label.pack(pady=5, padx=20, expand=True, side="bottom")
    support_headline_frame.pack(pady=5, padx=5, fill="x")
    support_headline_label.pack()

# ==========Toggle dark/light mode==========
def change_mode():
        if mode_switch.get() == 1:
            customtkinter.set_appearance_mode("dark")
        else:
            customtkinter.set_appearance_mode("light")
        



# ==========LEFT FRAME BUTTONS========== 

logo_label = customtkinter.CTkLabel(master=left_frame, text="", image=logo_image)
logo_label.pack(pady=20, fill="both", expand=False)


home_button = customtkinter.CTkButton(master=left_frame, command=clicked_home, fg_color="#0b57c2", hover_color="#F5681C", text="", width=80, height=80, image=home_image)
home_button.pack(pady=10, padx=10)


install_software_button = customtkinter.CTkButton(master=left_frame, command=clicked_install_software, fg_color="#0b57c2", hover_color="#F5681C", text="", width=80, height=80, image=install_software_image)
install_software_button.pack(pady=10, padx=10)


support_button = customtkinter.CTkButton(master=left_frame, command=clicked_support, fg_color="#0b57c2", hover_color="#F5681C", text="", width=80, height=80, image=support_image)
support_button.pack(pady=10, padx=10)

mode_switch = customtkinter.CTkSwitch(master=left_frame, text="Dark Mode", command=change_mode)
mode_switch.select()
mode_switch.pack(side="bottom", pady=20)



root.mainloop()