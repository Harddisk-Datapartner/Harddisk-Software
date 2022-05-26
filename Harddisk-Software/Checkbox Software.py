
from tkinter import *
import customtkinter
import os
import threading
import subprocess



root = Tk()
customtkinter.set_appearance_mode("dark") 
customtkinter.set_default_color_theme("blue")
root.title("Harddisk Datapartner")
"""root.iconbitmap(default="HARDDISK-SOFTWARE\\Logos\HDDLOGO.ico")"""
root.configure(background="#383837")

# Set app size and position on the screen (middle)
app_width = 960
app_height = 540
screen_width = root.winfo_screenwidth()
screen_height = root.winfo_screenheight()
screen_x = (screen_width / 2) - (app_width / 2)
screen_y = (screen_height / 2) - (app_height / 2)
root.geometry(f"{app_width}x{app_height}+{int(screen_x)}+{int(screen_y)}")

top_frame = customtkinter.CTkFrame(root, width=950, height=50, fg_color="#0b57c2", border_color="gray", border_width=0.5, corner_radius=10) # Blå
center_frame = customtkinter.CTkFrame(root, width=800, height=400, fg_color="green", corner_radius=10) # 880x490
left_frame = customtkinter.CTkFrame(root, width=80, height=450, fg_color="#4d4d4b", border_color="gray", border_width=0.5, corner_radius=10)

label = customtkinter.CTkLabel(top_frame, text="Test", text_color="silver", text_font=("Roboto", -30))
label.place(relx=0.4, rely=0.1)

def checksize():
    print(app_height)
    print(app_width)

button1 = customtkinter.CTkButton(left_frame, command=checksize, text="1", width=70, height=70).place(relx=0.05, rely=0.03)
button2 = customtkinter.CTkButton(left_frame, command=checksize, text="2", width=70, height=70).place(relx=0.05, rely=0.2)
button3 = customtkinter.CTkButton(left_frame, command=checksize, text="3", width=70, height=70).place(relx=0.05, rely=0.37)
button4 = customtkinter.CTkButton(left_frame, command=checksize, text="4", width=70, height=70).place(relx=0.05, rely=0.54)
button4 = customtkinter.CTkButton(left_frame, command=checksize, text="5", width=70, height=70).place(relx=0.05, rely=0.71)
"""root.grid_rowconfigure(1, weight=1)
root.grid_columnconfigure(0, weight=1)"""

top_frame.grid(row=1, columnspan=1, rowspan=1, sticky="NE")
"""center_frame.grid(sticky="SE")"""
left_frame.grid(columnspan= 1, sticky="W")


"""software_list = "cmd /k "
vlc = IntVar()
firefox = IntVar()
unchecky = IntVar()
spotify = IntVar()
teamviewer = IntVar()
steam = IntVar()
discord = IntVar()
intel = IntVar()

#Function to download chosen packages 
def install_selected_checkbox():
    global software_list
    if (vlc.get()==1):
        software_list += "winget install VideoLAN.VLC -e && "
    elif (vlc.get()==0):
        pass
    
    if (firefox.get()==1):
            software_list += "winget install Mozilla.Firefox -e && "
    elif (firefox.get()==0):
        pass
    
    if (unchecky.get()==1):
            software_list += "winget install Unchecky.Unchecky -e && "
    elif (unchecky.get()==0):
        pass
    
    if (spotify.get()==1):
            software_list += "winget install Spotify.Spotify --force -e && "
    elif (spotify.get()==0):
        pass
    
    if (teamviewer.get()==1):
            software_list += "winget install Teamviewer.Teamviewer -e && "
    elif (teamviewer.get()==0):
        pass
    
    if (steam.get()==1):
            software_list += "winget install Valve.Steam -e && "
    elif (steam.get()==0):
        pass
    
    if(discord.get()==1):
            software_list += "winget install Discord.Discord -e && "
    elif (discord.get()==0):
        pass

    if(intel.get()==1):
            software_list += "winget install Intel.IntelDriverAndSupportAssistant -e && "
    elif (intel.get()==0):
        pass

    # Removes the " -e && " from the end of the software list variable
    software_list = software_list[:-7]
    print(software_list)
    
    # If the length of software list is less than 6 characters, the user has not selected any programs. If it's over proceed with installing
    if len(software_list) < 6:
        print("No software selected")
    else:
        print("Subprosses installing")
        subprocess.Popen(software_list)
    
    # Unchecks all boxes
    vlc.set(0)
    firefox.set(0)
    unchecky.set(0)
    spotify.set(0)
    teamviewer.set(0)
    steam.set(0)
    discord.set(0)
    intel.set(0)

    # Resets the software list variable
    software_list = "cmd /k "

# Function to uninstall selected packages
def uninstall_selected_checkbox():
    global software_list
    if (vlc.get()==1):
        software_list += "winget uninstall VideoLAN.VLC -e && "
    elif (vlc.get()==0):
        pass
    
    if (firefox.get()==1):
            software_list += "winget uninstall Mozilla.Firefox -e && "
    elif (firefox.get()==0):
        pass
    
    if (unchecky.get()==1):
            software_list += "winget uninstall Unchecky.Unchecky -e && "
    elif (unchecky.get()==0):
        pass
    
    if (spotify.get()==1):
            software_list += "winget uninstall Spotify.Spotify -e && "
    elif (spotify.get()==0):
        pass
    
    if (teamviewer.get()==1):
            software_list += "winget uninstall Teamviewer.Teamviewer -e && "
    elif (teamviewer.get()==0):
        pass
    
    if (steam.get()==1):
            software_list += "winget uninstall Valve.Steam -e && "
    elif (steam.get()==0):
        pass
    
    if(discord.get()==1):
            software_list += "winget uninstall Discord.Discord -e && "
    elif (discord.get()==0):
        pass
   
    if(intel.get()==1):
            software_list += "winget uninstall Intel.IntelDriverAndSupportAssistant -e && "
    elif (intel.get()==0):
        pass

    # Removes the " -e && " from the end of the software list variable
    software_list = software_list[:-7]
    print(software_list)
    
    # If the length of software list is less than 6 characters, the user has not selected any programs. If it's over proceed with installing
    if len(software_list) < 6:
        print("No software selected")
    else:
        print("Subprosses installing")
        subprocess.Popen(software_list, stdout=subprocess.PIPE)
        linetest = software_list.stdout.readline()
    
    # Unchecks all boxes
    vlc.set(0)
    firefox.set(0)
    unchecky.set(0)
    spotify.set(0)
    teamviewer.set(0)
    steam.set(0)
    discord.set(0)
    intel.set(0)

    # Resets the software list variable
    software_list = "cmd /k "

# Starts separate threads for installing and uninstalling packages
x = threading.Thread(target=install_selected_checkbox)
x.start()
y = threading.Thread(target=uninstall_selected_checkbox)
y.start()


#Software selection checkboxes
vlc_image = PhotoImage(file="Harddisk-Software\\Logos\\64x64\\VLC 64x64.png")
vlc_check = Checkbutton(root, text ="VLC", image=vlc_image, activebackground="gray", variable=vlc, onvalue=1, offvalue=0).grid(row=1, column=0)

vlc_button = customtkinter.CTkButton(master=frame, image=vlc_image, text="", width=74, height=74, fg_color="#3f57bc").grid(row=1, column=0)

firefox_image = PhotoImage(file="Harddisk-Software\\Logos\\64x64\\Firefox 64x64.png")
firefox_check = Checkbutton(root, text ="Firefox", image=firefox_image, activebackground="gray", variable=firefox, onvalue=1, offvalue=0).grid(row=2, column=0)

spotify_image = PhotoImage(file="Harddisk-Software\\Logos\\64x64\\Spotify 64x64.png")
spotify_check = Checkbutton(root, text ="Spotify", image=spotify_image, activebackground="gray", variable=spotify, onvalue=1, offvalue=0).grid(row=4, column=0)

teamwiever_image = PhotoImage(file="Harddisk-Software\\Logos\\64x64\\Teamviewer 64x64.png")
teamviewer_check = Checkbutton(root, text ="Team Viewer", image=teamwiever_image, activebackground="gray", variable=teamviewer, onvalue=1, offvalue=0).grid(row=5, column=0)

steam_image = PhotoImage(file="Harddisk-Software\\Logos\\64x64\\Steam 64x64.png")
steam_check = Checkbutton(root, text ="Steam", image=steam_image, activebackground="gray", variable=steam, onvalue=1, offvalue=0).grid(row=6, column=0)

discord_image = PhotoImage(file="Harddisk-Software\\Logos\\64x64\\Discord 64x64.png")
discord_check = Checkbutton(root, text ="Discord", image=discord_image, activebackground="gray", variable=discord, onvalue=1, offvalue=0).grid(row=7, column=0)


#Install and uninstall selected programs
install_button = customtkinter.CTkButton(root, text="Installer valgte", command=install_selected_checkbox, width=0, fg_color="#0b57c2", text_color="silver", text_font=("Roboto Medium", -20)).grid(row=10, column=2, padx=300, pady=5)
uninstall_button = customtkinter.CTkButton(root, text="Avinstaller valgte", command=uninstall_selected_checkbox, width=0, fg_color="#0b57c2", hover_color="#f5681c", text_color="silver", text_font=("Roboto Medium", -20)).grid(row=12, column=2, padx=300, pady=5)
"""


root.mainloop()

