from tkinter import *
import os
import threading
import subprocess

checkbox_window = Tk()
checkbox_window.title("Harddisk Datapartner")
checkbox_window.iconbitmap(default='C:\\Users\\steffen\\Desktop\\HDD-Software 0.1\\Harddisk-Software\\Logos\\HDDLOGO.ico')
checkbox_window.configure(background="Black")

# Set app size and position on the screen (middle)
app_width = 960
app_height = 540
screen_width = checkbox_window.winfo_screenwidth()
screen_height = checkbox_window.winfo_screenheight()
screen_x = (screen_width / 2) - (app_width / 2)
screen_y = (screen_height / 2) - (app_height / 2)
checkbox_window.geometry(f"{app_width}x{app_height}+{int(screen_x)}+{int(screen_y)}")

Label (checkbox_window, text="Velg programvare", bg="Black", fg="white", font="Helvetica 20").grid(row=0, column=1)

software_list = "cmd /k "
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
        """subprocess.call(software_list)"""
    
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
        """subprocess.call(software_list)"""
    
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
x = threading.Thread(target=install_selected_checkbox, args=())
x.start()
y = threading.Thread(target=uninstall_selected_checkbox, args=())
y.start()

#Software selection checkboxes
vlc_image = PhotoImage(file="C:\\Users\\steffen\\Desktop\\HDD-Software 0.1\\Harddisk-Software\\Logos\\64x64\\VLC 64x64.png")
vlc_check = Checkbutton(checkbox_window, text ="VLC", image=vlc_image, activebackground="gray", variable=vlc, onvalue=1, offvalue=0).grid(row=1, column=0)

firefox_image = PhotoImage(file="C:\\Users\\steffen\\Desktop\\HDD-Software 0.1\\Harddisk-Software\\Logos\\64x64\\Firefox 64x64.png")
firefox_check = Checkbutton(checkbox_window, text ="Firefox", image=firefox_image, activebackground="gray", variable=firefox, onvalue=1, offvalue=0).grid(row=2, column=0)

spotify_image = PhotoImage(file="C:\\Users\\steffen\\Desktop\\HDD-Software 0.1\\Harddisk-Software\\Logos\\64x64\\Spotify 64x64.png")
spotify_check = Checkbutton(checkbox_window, text ="Spotify", image=spotify_image, activebackground="gray", variable=spotify, onvalue=1, offvalue=0).grid(row=4, column=0)

teamwiever_image = PhotoImage(file="C:\\Users\\steffen\\Desktop\\HDD-Software 0.1\\Harddisk-Software\\Logos\\64x64\\Teamviewer 64x64.png")
teamviewer_check = Checkbutton(checkbox_window, text ="Team Viewer", image=teamwiever_image, activebackground="gray", variable=teamviewer, onvalue=1, offvalue=0).grid(row=5, column=0)

steam_image = PhotoImage(file="C:\\Users\\steffen\\Desktop\\HDD-Software 0.1\\Harddisk-Software\\Logos\\64x64\\Steam 64x64.png")
steam_check = Checkbutton(checkbox_window, text ="Steam", image=steam_image, activebackground="gray", variable=steam, onvalue=1, offvalue=0).grid(row=6, column=0)

discord_image = PhotoImage(file="C:\\Users\\steffen\\Desktop\\HDD-Software 0.1\\Harddisk-Software\\Logos\\64x64\\Discord 64x64.png")
discord_check = Checkbutton(checkbox_window, text ="Discord", image=discord_image, activebackground="gray", variable=discord, onvalue=1, offvalue=0).grid(row=7, column=0)


#Install and uninstall selected programs
install_button = Button(checkbox_window, text="Installer valgte", command=install_selected_checkbox, width=0).grid(row=1, column=1)
uninstall_button = Button(checkbox_window, text="Avinstaller valgte", command=uninstall_selected_checkbox, width=0).grid(row=2, column=1)

checkbox_window.mainloop()

