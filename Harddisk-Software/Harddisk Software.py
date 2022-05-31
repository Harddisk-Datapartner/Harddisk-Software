from tkinter import *
import os
import threading
"""from tracemalloc import start"""


window = Tk()
window.geometry("1000x500")
window.title("Harddisk Datapartner")
"""window.iconbitmap(default='HDDLOGO.ico')"""
window.configure(background="Black")
Label (window, text="VLC Media Player", bg="Black", fg="white", font="Helvetica 20").grid(row=0, column=0)


def install_vlc():
    os.system('cmd /k winget install VideoLAN.VLC')
    Label (window, text= "Installerer VLC", bg="black", fg="white", font="Times 20 italic bold").grid(row=1, column=2)

def upgrade_vlc():
    os.system('cmd /k winget upgrade VideoLAN.VLC')
    Label (window, text= "Oppdaterer VLC", bg="black", fg="white", font="Times 20 italic bold").grid(row=2, column=2)

def uninstall_vlc():
    os.system('cmd /k winget uninstall VideoLAN.VLC')
    Label (window, text= "Avinstallerer VLC", bg="black", fg="white", font="Times 20 italic bold").grid(row=3, column=2)

def standard_pakke():
    os.system('winget install VideoLAN.VLC -e && winget install Mozilla.Firefox')

button = Button(window, text="Installer", command=threading.Thread(target=install_vlc).start, width=0).grid(row=1, column=0)
button = Button(window, text="Oppdater", command=threading.Thread(target=upgrade_vlc).start, width=0).grid(row=2, column=0)
button = Button(window, text="Avinstaller", command=threading.Thread(target=uninstall_vlc).start, width=0).grid(row=3, column=0)
button = Button(window, text="Standardpakken", command=threading.Thread(target=standard_pakke).start, width=0).grid(row=5, column=0)

window.mainloop()


"""threading.Thread(target=install_vlc).start()"""