from tkinter import *
import os
import threading
import subprocess

window = Tk()
window.geometry("1000x500")
window.title("Harddisk Datapartner")
window.iconbitmap(default='HDDLOGO.ico')
window.configure(background="Black")
Label (window, text="Velg programvare", bg="Black", fg="white", font="Helvetica 20").grid(row=0, column=0)

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
    
    software_list = software_list[:-7]
    print(software_list)
    subprocess.call(software_list)
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
    software_list = software_list[:-7]
    print(software_list)
    subprocess.call(software_list)
    software_list = "cmd /k "


#Software selection checkboxes

vlc_check = Checkbutton(window, text ="VLC", variable=vlc, onvalue=1, offvalue=0).grid(row=1, column=0)
firefox_check = Checkbutton(window, text ="Firefox", variable=firefox, onvalue=1, offvalue=0).grid(row=2, column=0)
unchecky_check = Checkbutton(window, text ="Unchecky", variable=unchecky, onvalue=1, offvalue=0).grid(row=3, column=0)
spotify_check = Checkbutton(window, text ="Spotify", variable=spotify, onvalue=1, offvalue=0).grid(row=4, column=0)
teamviewer_check = Checkbutton(window, text ="Team Viewer", variable=teamviewer, onvalue=1, offvalue=0).grid(row=5, column=0)
steam_check = Checkbutton(window, text ="Steam", variable=steam, onvalue=1, offvalue=0).grid(row=6, column=0)
discord_check = Checkbutton(window, text ="Discord", variable=discord, onvalue=1, offvalue=0).grid(row=7, column=0)
intel_check = Checkbutton(window, text ="Intel Driver & Support Assistant", variable=intel, onvalue=1, offvalue=0).grid(row=8, column=0)

#Install chosen button (With Threads)
install_button = Button(window, text="Installer valgte", command=threading.Thread(target=install_selected_checkbox).start, width=0).grid(row=1, column=1)
#Uninstall chosen button (With Threads)
uninstall_button = Button(window, text="Avinstaller valgte", command=threading.Thread(target=uninstall_selected_checkbox).start, width=0).grid(row=2, column=1)

# No threads
"""install_button = Button(window, text="Installer valgte", command=install_selected_checkbox, width=0).grid(row=0, column=1)"""


window.mainloop()

