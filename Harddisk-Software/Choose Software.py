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

#Functions executed from buttons.
def toggle_vlc():
    global software_list
    software_list += "winget install VideoLAN.VLC -e && "
    print(software_list)

def toggle_firefox():
    global software_list
    software_list += "winget install Mozilla.Firefox -e && "
    print(software_list)


def toggle_spotify():
    global software_list
    software_list += "winget install Spotify.Spotify -e && "
    print(software_list)

def toggle_unchecky():
    global software_list
    software_list += "winget install Unchecky.Unchecky -e && "
    print(software_list)

def toggle_geforce_experience():
    global software_list
    software_list += "winget install Nvidia.GeForceExperience -e && "
    print(software_list)

#Function to download chosen packages 
def install_selected():
    global software_list
    software_list = software_list[:-7]
    subprocess.call(software_list)
    print(software_list)

#Software selection buttons
button = Button(window, text="VLC", command=toggle_vlc, width=0).grid(row=1, column=0)
button = Button(window, text="Firefox", command=threading.Thread(target=toggle_firefox).start, width=0).grid(row=2, column=0)
button = Button(window, text="Spotify", command=threading.Thread(target=toggle_spotify).start, width=0).grid(row=3, column=0)
button = Button(window, text="Unchecky", command=threading.Thread(target=toggle_unchecky).start, width=0).grid(row=4, column=0)
button = Button(window, text="GeForce Experience", command=threading.Thread(target=toggle_geforce_experience).start, width=0).grid(row=5, column=0)

#Install chosen button
button = Button(window, text="Installer programmer", command=threading.Thread(target=install_selected).start, width=0).grid(row=1, column=1)

window.mainloop()


"""Prøv denne på jobb:
testprog = "winget install VideoLAN.VLC -e && spotify"
os.system('cmd /k') + testprog
eller
os.system('cmd /k'), testprog"""

"""software_list = "winget install """

"""def install_selected():
    global software_list
    software_list = software_list[:-7]
    os.system('cmd /k') + software_list
    # print(software_list)"""