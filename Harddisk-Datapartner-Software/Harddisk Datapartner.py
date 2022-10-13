import tkinter
from tkinter import ttk
import customtkinter
from PIL import Image, ImageTk
import subprocess
import webbrowser
import threading


######## If anyone ever reads this god give you strength as a you navigate this absolutely beautiful and perfectly optimized code. /s ########


# C:\Users\Bruker\AppData\Local\Programs\Python\Python310\Lib\site-packages
customtkinter.set_appearance_mode("dark")  # Modes: "System" (standard), "Dark", "Light"
"""customtkinter.set_default_color_theme("blue")  # Themes: "blue" (standard), "green", "dark-blue"""

# Harddisk colors. Blue = "#0B57C2" Orange = "#F5681C"
# (dark mode) Gray colors. Dark = #292929 brighter = #383838
# (light mode) Gray colors. Dark = #d1d0cf brighter = #c4c3c2

root = customtkinter.CTk()
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

logo_image = ImageTk.PhotoImage(Image.open("Logos\\HDDLOGO.ico").resize((90, 90)))
headline_image = ImageTk.PhotoImage(Image.open("Logos\\Fulltextlogo.png").resize((400, 55)))
home_image = ImageTk.PhotoImage(Image.open("Logos\\Menu icons\\Home.png").resize((image_size, image_size)))
install_software_image = ImageTk.PhotoImage(Image.open("Logos\\Menu icons\\Download.png").resize((image_size, image_size)))
support_image = ImageTk.PhotoImage(Image.open("Logos\\Menu icons\\Support.png").resize((image_size, image_size)))


# ==========Software Images==========
# Browsers/Nettlesere
firefox_image = ImageTk.PhotoImage(Image.open("Logos\\128x128\\Firefox 128x128.png").resize((image_size, image_size)))
chrome_image = ImageTk.PhotoImage(Image.open("Logos\\128x128\\Chrome 128x128.png").resize((image_size, image_size)))
brave_image = ImageTk.PhotoImage(Image.open("Logos\\128x128\\Brave 128x128.png").resize((image_size, image_size)))
vivaldi_image = ImageTk.PhotoImage(Image.open("Logos\\128x128\\Vivaldi 128x128.png").resize((image_size, image_size)))
duckduckgo_image = ImageTk.PhotoImage(Image.open("Logos\\128x128\\DuckDuckGo 128x128.png").resize((image_size, image_size)))

# Email Clients/Epost klienter
emclient_image = ImageTk.PhotoImage(Image.open("Logos\\128x128\\EM Client 128x128.png").resize((image_size, image_size)))
thunderbird_image = ImageTk.PhotoImage(Image.open("Logos\\128x128\\Thunderbird 128x128.png").resize((image_size, image_size)))

# Document management/Dokumentbehandling
libre_office_image = ImageTk.PhotoImage(Image.open("Logos\\128x128\\Libreoffice 128x128.png").resize((image_size, image_size)))
open_office_image = ImageTk.PhotoImage(Image.open("Logos\\128x128\\Open Office 128x128.png").resize((image_size, image_size)))
evernote_image = ImageTk.PhotoImage(Image.open("Logos\\128x128\\Evernote 128x128.png").resize((image_size, image_size)))
onenote_image = ImageTk.PhotoImage(Image.open("Logos\\128x128\\OneNote 128x128.png").resize((image_size, image_size)))
adobe_reader_image = ImageTk.PhotoImage(Image.open("Logos\\128x128\\Adobe_reader 128x128.png").resize((image_size, image_size)))

# Media
vlc_image = ImageTk.PhotoImage(Image.open("Logos\\128x128\\VLC 128x128.png").resize((image_size, image_size)))
spotify_image = ImageTk.PhotoImage(Image.open("Logos\\128x128\\Spotify 128x128.png").resize((image_size, image_size)))
itunes_image = ImageTk.PhotoImage(Image.open("Logos\\128x128\\Itunes 128x128.png").resize((image_size, image_size)))
tidal_image = ImageTk.PhotoImage(Image.open("Logos\\128x128\\Tidal 128x128.png").resize((image_size, image_size)))
k_lite_codec_pack_image = ImageTk.PhotoImage(Image.open("Logos\\128x128\\K-Lite Codec.png").resize((image_size, image_size)))

#Games/Spill
steam_image = ImageTk.PhotoImage(Image.open("Logos\\128x128\\Steam 128x128.png").resize((image_size, image_size)))
epic_games_image = ImageTk.PhotoImage(Image.open("Logos\\128x128\\Epic 128x128.png").resize((image_size, image_size)))
gog_image = ImageTk.PhotoImage(Image.open("Logos\\128x128\\GOG 128x128.png").resize((image_size, image_size)))
ubisoft_image = ImageTk.PhotoImage(Image.open("Logos\\128x128\\Ubisoft 128x128.png").resize((image_size, image_size)))
origin_image= ImageTk.PhotoImage(Image.open("Logos\\128x128\\Origin 128x128.png").resize((image_size, image_size)))

#Photo editing/Bilderedigering
gimp_image = ImageTk.PhotoImage(Image.open("Logos\\128x128\\Gimp 128x128.png").resize((image_size, image_size)))
greenshot_image = ImageTk.PhotoImage(Image.open("Logos\\128x128\\Greenshot 128x128.png").resize((image_size, image_size)))
irfanview_image = ImageTk.PhotoImage(Image.open("Logos\\128x128\\Irfanview 128x128.png").resize((image_size, image_size)))

#Cloud storage
onedrive_image = ImageTk.PhotoImage(Image.open("Logos\\128x128\\onedrive 128x128.png").resize((image_size, image_size)))
dropbox_image = ImageTk.PhotoImage(Image.open("Logos\\128x128\\dropbox 128x128.png").resize((image_size, image_size)))
google_drive_image = ImageTk.PhotoImage(Image.open("Logos\\128x128\\google_drive 128x128.png").resize((image_size, image_size)))

#Communtication/Kommunikasjon
discord_image = ImageTk.PhotoImage(Image.open("Logos\\128x128\\Discord 128x128.png").resize((image_size, image_size)))
teamviewer_image = ImageTk.PhotoImage(Image.open("Logos\\128x128\\Teamviewer 128x128.png").resize((image_size, image_size)))
skype_image = ImageTk.PhotoImage(Image.open("Logos\\128x128\\Skype 128x128.png").resize((image_size, image_size)))
zoom_image = ImageTk.PhotoImage(Image.open("Logos\\128x128\\Zoom 128x128.png").resize((image_size, image_size)))

# Compression/Komprimering
peazip_image = ImageTk.PhotoImage(Image.open("Logos\\128x128\\Peazip 128x128.png").resize((image_size, image_size)))
seven_zip_image = ImageTk.PhotoImage(Image.open("Logos\\128x128\\7zip 128x128.png").resize((image_size, image_size)))

# Streaming
obs_image = ImageTk.PhotoImage(Image.open("Logos\\128x128\\obs 128x128.png").resize((image_size, image_size)))
elgato_image = ImageTk.PhotoImage(Image.open("Logos\\128x128\\elgato 128x128.png").resize((image_size, image_size)))
# Geforce experience image created under #Drivers

# RGB
icue_image = ImageTk.PhotoImage(Image.open("Logos\\128x128\\Icue 128x128.png").resize((image_size, image_size)))
nzxt_image = ImageTk.PhotoImage(Image.open("Logos\\128x128\\Nzxt 128x128.png").resize((image_size, image_size)))
msi_image = ImageTk.PhotoImage(Image.open("Logos\\128x128\\Msi 128x128.png").resize((image_size, image_size)))
gigabyte_image = ImageTk.PhotoImage(Image.open("Logos\\128x128\\Gigabyte_fusion 128x128.png").resize((image_size, image_size)))
lianli_image = ImageTk.PhotoImage(Image.open("Logos\\128x128\\Lianli 128x128.png").resize((image_size, image_size)))
openrgb_image = ImageTk.PhotoImage(Image.open("Logos\\128x128\\Openrgb 128x128.png").resize((image_size, image_size)))

# Drivers
intel_image = ImageTk.PhotoImage(Image.open("Logos\\128x128\\IntelD&SA 128x128.png").resize((image_size, image_size)))
nv_cleaninstall_image = ImageTk.PhotoImage(Image.open("Logos\\128x128\\NV Cleaninstall 128x128.png").resize((image_size, image_size)))
lenovo_image = ImageTk.PhotoImage(Image.open("Logos\\128x128\\LenovoSU 128x128.png").resize((image_size, image_size)))
geforce_experience_image = ImageTk.PhotoImage(Image.open("Logos\\128x128\\Geforce Experience 128x128.png").resize((image_size, image_size)))
amd_image = ImageTk.PhotoImage(Image.open("Logos\\128x128\\AMD 128x128.png").resize((image_size, image_size)))
asus_armourycrate_image = ImageTk.PhotoImage(Image.open("Logos\\128x128\\Armoury Crate 128x128.png").resize((image_size, image_size)))
gigabyte_app_image = ImageTk.PhotoImage(Image.open("Logos\\128x128\\Gigabyte App 128x128.png").resize((image_size, image_size)))

unchecky_image = ImageTk.PhotoImage(Image.open("Logos\\128x128\\Unchecky 128x128.png").resize((image_size, image_size)))






# ==========Base varaibles==========
software_list = "cmd /k " #The base of the winget string. Software package ID's will be appended to this.
labels_toggled = 0
chosen_software_labelframe_height = 145
current_master = 0


# ==========String creation with winget commands==========
# Browsers
cmd_firefox = "winget install Mozilla.Firefox -e && "
cmd_chrome = "winget install Google.Chrome -e && "
cmd_brave = "winget install BraveSoftware.BraveBrowser -e && "
cmd_vivaldi = "winget install VivaldiTechnologies.Vivaldi -e && "
cmd_duckduckgo = "winget install VivaldiTechnologies.Vivaldi -e && "

#Email clients
cmd_emclient = "winget install eMClient.eMClient -e && "
cmd_thunderbird = "winget install Mozilla.Thunderbird -e && "

#Document managers
cmd_libre_office = "winget install TheDocumentFoundation.LibreOffice -e && "
cmd_open_office = "winget install Apache.OpenOffice -e && "
cmd_evernote = "winget install evernote.evernote -e && "
cmd_onenote = "winget install 9WZDNCRFHVJL -e && "  #????
cmd_adobe_reader =  "winget install Adobe.Acrobat.Reader.64-bit -e && "

#Media
cmd_vlc = "winget install VideoLAN.VLC -e && "
cmd_spotify = "winget install Spotify.Spotify -e && "
cmd_itunes = "winget install Apple.iTunes -e && "
cmd_tidal = "winget install TIDALMusicAS.TIDAL -e && "
cmd_k_lite_codec_pack = "winget install CodecGuide.K-LiteCodecPack.Standard -e && "



#Cloud storage
cmd_onedrive = "winget install Microsoft.OneDrive -e && "
cmd_dropbox = "winget install Dropbox.Dropbox -e && "
cmd_google_drive = "winget install Google.Drive -e && "

#Game launchers
cmd_steam = "winget install Valve.Steam -e && "
cmd_epic_games = "winget install EpicGames.EpicGamesLauncher -e && "
cmd_gog = "winget install GOG.Galaxy -e && "
cmd_ubisoft = "winget install Ubisoft.Connect --force -e && "
cmd_origin = "winget install ElectronicArts.EADesktop -e && "
cmd_blizzard = "winget install ???????????????? -e && "

# Photo editing
cmd_gimp = "winget install GIMP.GIMP -e && "
cmd_greenshot = "winget install Greenshot.Greenshot -e && "
cmd_irfanview = "winget install IrfanSkiljan.IrfanView -e && "

#Cloud Storage
cmd_onedrive = "winget install Microsoft.OneDrive -e && "
cmd_dropbox = "winget install Dropbox.Dropbox -e && "
cmd_google_drive = "winget install Google.Drive -e && "

#Communication
cmd_discord = "winget install Discord.Discord -e && "
cmd_skype = "winget install Microsoft.Skype -e && "
cmd_zoom = "winget install Zoom.Zoom -e && "
cmd_teamwiever = "winget install Teamviewer.Teamviewer -e && "

# Compression
cmd_peazip = "winget install Giorgiotani.Peazip -e && "
cmd_seven_zip = "winget install 7zip.7zip -e && "

# Streaming
cmd_obs = "winget install OBSProject.OBSStudio -e && "
cmd_elgato = "winget install Elgato.GameCapture.HD -e && "
cmd_geforce_experience = "winget install Nvidia.GeForceExperience -e && "

# RGB
cmd_icue = "winget install Corsair.iCUE.4 -e && "
cmd_nzxt = "winget install NZXT.CAM -e && "
cmd_msi = "winget install 9NVMNJCR03XV -e && "
cmd_asus = "winget install ???????????????? -e && "
cmd_gigabyte = "winget install ????????????????  -e && "
cmd_lconnect = "winget install ???????????????? -e && "
cmd_openrgb = "winget ???????????????? install  -e && "

#Drivers
cmd_intel = "winget install Intel.IntelDriverAndSupportAssistant -e && "
cmd_nv_cleaninstall = "winget install TechPowerUp.NVCleanstall -e && "
cmd_lenovo = "winget install Lenovo.SystemUpdate -e && "
cmd_amd = "winget install ???????????????? -e && "

# ==========Functions executed from buttons.==========
def toggle_browser_software(args): #Browsers
    global software_list
    global labels_toggled
    global current_master
    global chosen_software_labelframe_height
    print(labels_toggled)
    if args == 1:
        if cmd_firefox in software_list:
            software_list = software_list.replace(cmd_firefox, "")
            #chosen_firefox_label.pack_forget()
            labels_toggled -= 1
        else:
            software_list += cmd_firefox
            #chosen_firefox_label = customtkinter.CTkLabel(master = chosen_software_main_frame, image=firefox_image, width=20,  corner_radius=15)
            chosen_firefox_label.pack(side="left")
            labels_toggled += 1
    if args == 2:
        if cmd_chrome in software_list:
            software_list = software_list.replace(cmd_chrome, "")
            chosen_chrome_label.pack_forget()
            labels_toggled -= 1
        else:
            software_list += cmd_chrome
            #chosen_chrome_label = customtkinter.CTkLabel(master = chosen_software_main_frame, image=chrome_image, width=20,  corner_radius=15 )
            chosen_chrome_label.pack(side="left")
            labels_toggled += 1
    if args == 3:
        if cmd_brave in software_list:
            software_list = software_list.replace(cmd_brave, "")
            #chosen_brave_label.pack_forget()
            labels_toggled -= 1
            
        else:
            software_list += cmd_brave
            #chosen_brave_label = customtkinter.CTkLabel(master = chosen_software_main_frame, image=brave_image, width=20,  corner_radius=15 )
            chosen_brave_label.pack(side="left")
            labels_toggled += 1
    if args == 4:
        if cmd_vivaldi in software_list:
            software_list = software_list.replace(cmd_vivaldi, "")
            #chosen_vivaldi_label.pack_forget()
            labels_toggled -= 1
        else:
            software_list += cmd_vivaldi
            #chosen_vivaldi_label = customtkinter.CTkLabel(master = chosen_software_main_frame, image=vivaldi_image, width=20,  corner_radius=15 )
            chosen_vivaldi_label.pack(side="left")
            labels_toggled += 1
    print(software_list)
    #change_label_size() 

def toggle_email_software(args): #Email Clients
    global software_list
    global labels_toggled
    if args == 1:
        if cmd_emclient in software_list:
            software_list = software_list.replace(cmd_emclient, "")
            chosen_emclient_label.pack_forget()
            labels_toggled -= 1
        else:
            software_list += cmd_emclient
            chosen_emclient_label.pack(side="left")
            labels_toggled += 1
    if args == 2:
        if cmd_thunderbird in software_list:
            software_list = software_list.replace(cmd_thunderbird, "")
            chosen_thunderbird_label.pack_forget()
            labels_toggled -= 1
        else:
            software_list += cmd_thunderbird
            chosen_thunderbird_label.pack(side="left")
            labels_toggled += 1


    print(software_list) 


def toggle_document_software(args): #Document Management
    global software_list
    global labels_toggled
    if args == 1:
        if cmd_libre_office in software_list:
            software_list = software_list.replace(cmd_libre_office, "")
            chosen_libre_office_label.pack_forget()
            labels_toggled -= 1
        else:
            software_list += cmd_libre_office
            #chosen_libre_office_label = customtkinter.CTkLabel(master = chosen_software_main_frame, image=libre_office_image, width=20,  corner_radius=15)
            chosen_libre_office_label.pack(side="left")
            labels_toggled += 1
    if args == 2:
        if cmd_open_office in software_list:
            software_list = software_list.replace(cmd_open_office, "")
            chosen_open_office_label.pack_forget()
            labels_toggled -= 1
        else:
            software_list += cmd_open_office
            #chosen_open_office_label = customtkinter.CTkLabel(master = chosen_software_main_frame, image=open_office_image, width=20,  corner_radius=15)
            chosen_open_office_label.pack(side="left")
            labels_toggled += 1
    if args == 3:
        if cmd_evernote in software_list:
            software_list = software_list.replace(cmd_evernote, "")
            chosen_evernote_label.pack_forget()
            labels_toggled -= 1
        else:
            software_list += cmd_evernote
            #chosen_evernote_label = customtkinter.CTkLabel(master = chosen_software_main_frame, image=evernote_image, width=20,  corner_radius=15)
            chosen_evernote_label.pack(side="left")
            labels_toggled += 1
    if args == 4:
        webbrowser.open("https://www.microsoft.com/nb-no/microsoft-365/onenote/digital-note-taking-app")

    if args == 5:
        if cmd_adobe_reader in software_list:
            software_list = software_list.replace(cmd_adobe_reader, "")
            chosen_adobe_reader_label.pack_forget()
            labels_toggled -= 1
        else:
            software_list += cmd_adobe_reader
            #chosen_adobe_reader_label = customtkinter.CTkLabel(master = chosen_software_main_frame, image=adobe_reader_image, width=20,  corner_radius=15)
            chosen_adobe_reader_label.pack(side="left")
            labels_toggled += 1
    

    print(software_list)
    #change_label_size() 

def toggle_media_software(args): #Media
    global software_list
    global labels_toggled
    if args == 1:
        if cmd_vlc in software_list:
            software_list = software_list.replace(cmd_vlc, "")
            chosen_vlc_label.pack_forget()
            labels_toggled -= 1
        else:
            software_list += cmd_vlc
            chosen_vlc_label.pack(side="left")
            labels_toggled += 1
    if args == 2:
        if cmd_spotify in software_list:
            software_list = software_list.replace(cmd_spotify, "")
            chosen_spotify_label.pack_forget()
            labels_toggled -= 1
        else:
            software_list += cmd_spotify
            chosen_spotify_label.pack(side="left")
            labels_toggled += 1
    if args == 3:
        if cmd_itunes in software_list:
            software_list = software_list.replace(cmd_itunes, "")
            chosen_itunes_label.pack_forget()
            labels_toggled -= 1
        else:
            software_list += cmd_itunes
            chosen_itunes_label.pack(side="left")
            labels_toggled += 1
    if args == 4:
        if cmd_tidal in software_list:
            software_list = software_list.replace(cmd_tidal, "")
            chosen_tidal_label.pack_forget()
            labels_toggled -= 1
        else:
            software_list += cmd_tidal
            chosen_tidal_label.pack(side="left")
            labels_toggled += 1
    if args == 5:
        if cmd_k_lite_codec_pack in software_list:
            software_list = software_list.replace(cmd_k_lite_codec_pack, "")
            chosen_k_lite_codec_pack_label.pack_forget()
            labels_toggled -= 1
        else:
            software_list += cmd_k_lite_codec_pack
            chosen_k_lite_codec_pack_label.pack(side="left")
            labels_toggled += 1

    print(software_list) 

def toggle_game_software(args): #Game launchers
    global software_list
    global labels_toggled
    if args == 1:
        if cmd_steam in software_list:
            software_list = software_list.replace(cmd_steam, "")
            chosen_steam_label.pack_forget()
            labels_toggled -= 1
        else:
            software_list += cmd_steam
            chosen_steam_label.pack(side="left")
            labels_toggled += 1
    if args == 2:
        if cmd_epic_games in software_list:
            software_list = software_list.replace(cmd_epic_games, "")
            chosen_epic_games_label.pack_forget()
            labels_toggled -= 1
        else:
            software_list += cmd_epic_games
            chosen_epic_games_label.pack(side="left")
            labels_toggled += 1
    if args == 3:
        if cmd_gog in software_list:
            software_list = software_list.replace(cmd_gog, "")
            chosen_gog_label.pack_forget()
            labels_toggled -= 1
        else:
            software_list += cmd_gog
            chosen_gog_label.pack(side="left")
            labels_toggled += 1
    if args == 4:
        if cmd_ubisoft in software_list:
            software_list = software_list.replace(cmd_ubisoft, "")
            chosen_ubisoft_label.pack_forget()
            labels_toggled -= 1
        else:
            software_list += cmd_ubisoft
            chosen_ubisoft_label.pack(side="left")
            labels_toggled += 1
    if args == 5:
        if cmd_origin in software_list:
            software_list = software_list.replace(cmd_origin, "")
            chosen_origin_label.pack_forget()
            labels_toggled -= 1
        else:
            software_list += cmd_origin
            chosen_origin_label.pack(side="left")  
            labels_toggled += 1

    print(software_list)    

def toggle_photo_software(args): #Photo Editing
    global software_list
    global labels_toggled
    if args == 1:
        if cmd_gimp in software_list:
            software_list = software_list.replace(cmd_gimp, "")
            chosen_gimp_label.pack_forget()
            labels_toggled -= 1
        else:
            software_list += cmd_gimp
            chosen_gimp_label.pack(side="left")
            labels_toggled += 1
    if args == 2:
        if cmd_irfanview in software_list:
            software_list = software_list.replace(cmd_irfanview, "")
            chosen_irfanview_label.pack_forget()
            labels_toggled -= 1
        else:
            software_list += cmd_irfanview
            chosen_irfanview_label.pack(side="left")
            labels_toggled += 1
    if args == 3:
        if cmd_greenshot in software_list:
            software_list = software_list.replace(cmd_greenshot, "")
            chosen_greenshot_label.pack_forget()
            labels_toggled -= 1
        else:
            software_list += cmd_greenshot
            chosen_greenshot_label.pack(side="left")
            labels_toggled += 1

    print(software_list)

def toggle_cloud_software(args): #Cloud Storage
    global software_list
    global labels_toggled
    if args == 1:
        if cmd_onedrive in software_list:
            software_list = software_list.replace(cmd_onedrive, "")
            chosen_onedrive_label.pack_forget()
            labels_toggled -= 1
        else:
            software_list += cmd_onedrive
            chosen_onedrive_label.pack(side="left")
            labels_toggled += 1
    if args == 2:
        if cmd_dropbox in software_list:
            software_list = software_list.replace(cmd_dropbox, "")
            chosen_dropbox_label.pack_forget()
            labels_toggled -= 1
        else:
            software_list += cmd_dropbox
            chosen_dropbox_label.pack(side="left")
            labels_toggled += 1
    if args == 3:
        if cmd_google_drive in software_list:
            software_list = software_list.replace(cmd_google_drive, "")
            chosen_google_drive_label.pack_forget()
            labels_toggled -= 1
        else:
            software_list += cmd_google_drive
            chosen_google_drive_label.pack(side="left")
            labels_toggled += 1
    

    print(software_list)

def toggle_communication_software(args): #Communication
    global software_list
    global labels_toggled
    if args == 1:
        if cmd_discord in software_list:
            software_list = software_list.replace(cmd_discord, "")
            chosen_discord_label.pack_forget()
            labels_toggled -= 1
        else:
            software_list += cmd_discord
            chosen_discord_label.pack(side="left")
            labels_toggled += 1
    if args == 2:
        if cmd_skype in software_list:
            software_list = software_list.replace(cmd_skype, "")
            chosen_skype_label.pack_forget()
            labels_toggled -= 1
        else:
            software_list += cmd_skype
            chosen_skype_label.pack(side="left")
            labels_toggled += 1
    if args == 3:
        if cmd_zoom in software_list:
            software_list = software_list.replace(cmd_zoom, "")
            chosen_zoom_label.pack_forget()
            labels_toggled -= 1
        else:
            software_list += cmd_zoom
            chosen_zoom_label.pack(side="left")
            labels_toggled += 1
    if args == 4:
        if cmd_teamwiever in software_list:
            software_list = software_list.replace(cmd_teamwiever, "")
            chosen_teamviewer_label.pack_forget()
            labels_toggled -= 1
        else:
            software_list += cmd_teamwiever
            chosen_teamviewer_label.pack(side="left")
            labels_toggled += 1

    print(software_list)

def toggle_compression_software(args): #Compression
    global software_list
    global labels_toggled
    if args == 1:
        if cmd_seven_zip in software_list:
            software_list = software_list.replace(cmd_seven_zip, "")
            chosen_seven_zip_label.pack_forget()
            labels_toggled -= 1
        else:
            software_list += cmd_seven_zip
            chosen_seven_zip_label.pack(side="left")
            labels_toggled += 1
    if args == 2:
        if cmd_peazip in software_list:
            software_list = software_list.replace(cmd_peazip, "")
            chosen_peazip_label.pack_forget()
            labels_toggled -= 1
        else:
            software_list += cmd_peazip
            chosen_peazip_label.pack(side="left")
            labels_toggled += 1

    print(software_list)   

def toggle_streaming_software(args): #Streaming
    global software_list
    global labels_toggled
    if args == 1:
        if cmd_obs in software_list:
            software_list = software_list.replace(cmd_obs, "")
            chosen_obs_label.pack_forget()
            labels_toggled -= 1
        else:
            software_list += cmd_obs
            chosen_obs_label.pack(side="left")
            labels_toggled += 1
    if args == 2:
        if cmd_geforce_experience in software_list:
            software_list = software_list.replace(cmd_geforce_experience, "")
            chosen_geforce_experience_label.pack_forget()
            labels_toggled -= 1
        else:
            software_list += cmd_geforce_experience
            chosen_geforce_experience_label.pack(side="left")
            labels_toggled += 1
    if args == 3:
        if cmd_elgato in software_list:
            software_list = software_list.replace(cmd_elgato, "")
            chosen_elgato_label.pack_forget()
            labels_toggled -= 1
        else:
            software_list += cmd_elgato
            chosen_elgato_label.pack(side="left")
            labels_toggled += 1
    

    print(software_list)

def toggle_rgb_software(args): #RGB Software
    global software_list
    global labels_toggled
    global current_master
    if args == 1:
        if cmd_icue in software_list:
            software_list = software_list.replace(cmd_icue, "")
            chosen_icue_label.pack_forget()
            labels_toggled -= 1
        else:
            software_list += cmd_icue
            chosen_icue_label.pack(side="left")
            labels_toggled += 1
    if args == 2:
        if cmd_nzxt in software_list:
            software_list = software_list.replace(cmd_nzxt, "")
            chosen_nzxt_label.pack_forget()
            labels_toggled -= 1
        else:
            software_list += cmd_nzxt
            chosen_nzxt_label.pack(side="left")
            labels_toggled += 1
    if args == 3:
        webbrowser.open("https://www.msi.com/Landing/mystic-light-rgb-gaming-pc/download")
    if args == 4:
        webbrowser.open("https://www.asus.com/supportonly/Armoury%20Crate/HelpDesk_Download/")
    if args == 5:
        webbrowser.open("https://www.gigabyte.com/MicroSite/512/rgb2.html")
    if args == 6:
        webbrowser.open("https://lian-li.com/l-connect3/")
    if args == 7:
        webbrowser.open("https://openrgb.org/")
    

    print(software_list)    

def toggle_driver_software(args): #Drivers
    global software_list
    global labels_toggled
    if args == 1:
        if cmd_intel in software_list:
            software_list = software_list.replace(cmd_intel, "")
            chosen_intel_label.pack_forget()
            labels_toggled -= 1
        else:
            software_list += cmd_intel
            chosen_intel_label.pack(side="left")
            labels_toggled += 1
    if args == 2:
        if cmd_nv_cleaninstall in software_list:
            software_list = software_list.replace(cmd_nv_cleaninstall, "")
            chosen_nv_cleaninstall_label.pack_forget()
            labels_toggled -= 1
        else:
            software_list += cmd_nv_cleaninstall
            chosen_nv_cleaninstall_label.pack(side="left")
            labels_toggled += 1
    if args == 3:
        if cmd_lenovo in software_list:
            software_list = software_list.replace(cmd_lenovo, "")
            chosen_lenovo_label.pack_forget()
            labels_toggled -= 1
            
        else:
            software_list += cmd_lenovo
            chosen_lenovo_label.pack(side="left")
            labels_toggled += 1
    if args == 4:
        if cmd_geforce_experience in software_list:
            software_list = software_list.replace(cmd_geforce_experience, "")
            chosen_geforce_experience_label.pack_forget()
            labels_toggled -= 1
        else:
            software_list += cmd_geforce_experience
            chosen_geforce_experience_label.pack(side="left")
            labels_toggled += 1
    if args == 5:
        webbrowser.open("https://www.amd.com/en/support")
    if args == 6:
        webbrowser.open("https://www.asus.com/supportonly/Armoury%20Crate/HelpDesk_Download/")
    if args == 7:
        webbrowser.open("https://www.gigabyte.com/Support/Utility")
    


    print(software_list)

# ==========LEFT FRAME (Packing because it's always present)==========
left_frame = customtkinter.CTkFrame(master=root, 
                                        fg_color=("#d1d0cf", "#292929"), 
                                        corner_radius=15)
left_frame.pack(side="left", pady=5, padx=5, fill="y", expand=False)



# ==========HOME SCREEN (Packing because it's home screen)==========
home_frame = customtkinter.CTkFrame(master=root, 
                                        fg_color=("#d1d0cf", "#292929"), 
                                        corner_radius=15)
home_frame.pack(pady=5, padx=5, fill="both", expand=True)

home_headline_frame = customtkinter.CTkFrame(master=home_frame, 
                                                fg_color=("#c4c3c2", "#383838"), 
                                                corner_radius=15, 
                                                height=50)
home_headline_frame.pack(pady=5, padx=5, fill="x")


home_frame2 = customtkinter.CTkFrame(master=home_frame, 
                                        fg_color=("#d1d0cf", "#383838"), 
                                        corner_radius=15)
home_frame2.pack(pady=5, padx=5, fill="both", expand=True)

# ==========HEADLINE LOGO==========
headline_label = customtkinter.CTkLabel(master=home_headline_frame, 
                                            fg_color=("#d1d0cf", "#383838"), 
                                            height=50, 
                                            corner_radius=15, 
                                            image = headline_image, 
                                            text="")
headline_label.pack(pady=5, padx=5, ipadx=5, ipady=5, side="top", fill="x")


home_headline_label = customtkinter.CTkLabel(master=home_headline_frame, 
                                                fg_color=("#c4c3c2", "#383838"), 
                                                text="Velkommen til Harddisk-programmet", 
                                                text_font=("Roboto Medium", 30), 
                                                corner_radius=15)
home_headline_label.pack(pady=5, padx=5, fill="x", side="top")


with open("Text\Hjem.txt", encoding="utf-8") as r:
    home_text = r.read()

home_main_label = customtkinter.CTkLabel(master=home_frame2, 
                                            fg_color=("#c4c3c2", "#383838"), 
                                            corner_radius=15, 
                                            text=home_text, 
                                            text_font=("Roboto Medium", 15)) 
home_main_label.pack(pady=5, padx=5, ipady=20, expand=False, fill="x", side="top")


home_secondary_label = customtkinter.CTkLabel(master=home_frame2, 
                                            fg_color=("#c4c3c2", "#383838"), 
                                            corner_radius=15, 
                                            text="*Vi kan ikke garantere for tredjepartsprogrammers sikkerhet.", 
                                            anchor="se", 
                                            text_font=("Roboto Medium", 10)) 
home_secondary_label.pack(pady=5, padx=5, fill="x", side="bottom")


p1 = ""
f = None
#stepvalue = 0.0
def compile_selected(args, ):
    global software_list
    #global stepvalue
    global p1
    global f
    software_list = software_list[:-7]
    if len(software_list) < 6: # < er riktig
        print("No software selected")
    else:
        progressbar_frame.pack(side="top", padx=5, pady=5, fill="both", expand=True)
        chosen_software_progressbar.pack(fill="x", expand=True)
        output_label.pack(fill="both", expand=True)
        #chosen_software_progressbar.set(stepvalue)
        
        if args==1:
                chosen_software_progressbar.start(30)
                print("Subprosses installing")
                #stepvalue += 0.1
                #software_list += " --accept-package-agreements"
                #with open("output.txt", "w") as f:
                #outputlol = subprocess.check_output("ping google.com", shell=True)
                f = subprocess.Popen(software_list, stdout=f, shell=True)
                f=("Hei hei test test")
                # output = subprocess.getoutput(software_list)
                print(software_list)
                #tick(f)
        if args == 2:
                #software_list = software_list.replace("install", "upgrade")
                # print("Subprosses updating")
                # print(output)
                subprocess.Popen(software_list)
        if args == 3:
                software_list = software_list.replace("install", "uninstall")
            
                if "--force" in software_list:
                    print("Force is in the list")
                    software_list = software_list.replace(" --force ", "hei")
                    print(software_list)
                else:
                    print("Force is NOT in the list")
                    print("Subprosses uninstalling")
                    print(software_list)
                    subprocess.Popen(software_list)
        # Resets the software list variable
        software_list = "cmd /k "
        unpack_chosen_labels()

"""def tick(f):
    for _ in range(40):
        print(f)
        output_label.configure(text=f)
        output_label.after(100)"""

"""def compile_selected(args):
    global software_list
    x.start()
    if args == 1:
        # Removes the " -e && " from the end of the software list variable
        software_list = software_list[:-7]
        print(software_list)
    
        # If the length of software list is less than 6 characters, the user has not selected any programs. If it's over proceed with installing
        if len(software_list) < 6:
            print("No software selected")
        else:
            print("Subprosses installing")
            print(software_list)
            chosen_software_progressbar.start()
            s = subprocess.Popen(software_list)
            # Resets the software list variable
            software_list = "cmd /k "
            unpack_chosen_labels()

    elif args == 2:
        
        # Removes the " -e && " from the end of the software list variable
        software_list = software_list[:-7]
        print(software_list)
    
        # If the length of software list is less than 6 characters, the user has not selected any programs. If it's over proceed with installing
        if len(software_list) < 6:
            print("No software selected")
        else:
            software_list = software_list.replace("install", "upgrade")
            print("Subprosses updating")
            print(software_list)
            # subprocess.Popen(software_list)
            
        # Resets the software list variable
        software_list = "cmd /k "
        unpack_chosen_labels()
    
    elif args == 3:
        
        # Removes the " -e && " from the end of the software list variable
        software_list = software_list[:-7]
        print(software_list)
    
        # If the length of software list is less than 6 characters, the user has not selected any programs. If it's over proceed with installing
        if len(software_list) < 6:
            print("No software selected")
        else:
            software_list = software_list.replace("install", "uninstall")
        
        if "--force" in software_list:
            print("Force is in the list")
            software_list = software_list.replace(" --force ", "hei")
            print(software_list)
        else:
            print("Force is NOT in the list")
            print("Subprosses uninstalling")
            print(software_list)
            # subprocess.Popen(software_list)
        
        # Resets the software list variable
        software_list = "cmd /k "
        unpack_chosen_labels()
    for line in s.stdout.readlines():
        print(line)

"""


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
                                                text="^^^^ Velg programvare kategorier over ^^^^\nNoen programmer kan ikke installeres via Harddisk programmet\nDersom du trykker på de vil nettsiden til leverandøren åpnes ", 
                                                text_font=("Roboto Medium", 30), 
                                                corner_radius=15)

# ==========Sets up software tabs label==========
software_tabs_frame1 = customtkinter.CTkFrame(master=install_headline_frame, 
                                                fg_color=("#c4c3c2", "#383838"), 
                                                height= 20, 
                                                corner_radius=15)
software_tabs_frame2 = customtkinter.CTkFrame(master=install_headline_frame, 
                                                fg_color=("#c4c3c2", "#383838"), 
                                                height= 20, 
                                                corner_radius=15)
software_tabs1_filler_left = customtkinter.CTkFrame(master=software_tabs_frame1, 
                                                fg_color=("#c4c3c2", "#383838"), 
                                                height=5, 
                                                width=100, 
                                                corner_radius=15)

software_tabs1_filler_right = customtkinter.CTkFrame(master=software_tabs_frame1, 
                                                fg_color=("#c4c3c2", "#383838"), 
                                                height=5, 
                                                width=100,  
                                                corner_radius=15)

software_tabs2_filler_left = customtkinter.CTkFrame(master=software_tabs_frame2, 
                                                fg_color=("#c4c3c2", "#383838"), 
                                                height=5, 
                                                width=100, 
                                                corner_radius=15)

software_tabs2_filler_right = customtkinter.CTkFrame(master=software_tabs_frame2, 
                                                fg_color=("#c4c3c2", "#383838"), 
                                                height=5, 
                                                width=100,  
                                                corner_radius=15)


# ==========Sets up the bottom frame with install, update and uninstall buttons==========
install_bottom_frame = customtkinter.CTkFrame(master=root, 
                                                                fg_color=("#d1d0cf", "#292929"), 
                                                                corner_radius=15)

install_selected_button = customtkinter.CTkButton(master=install_bottom_frame, 
                                                                command=lambda:compile_selected(1),  
                                                                fg_color="#0b57c2", 
                                                                hover_color="#F5681C", 
                                                                text="  Installer Valgte  ", 
                                                                text_font=("Roboto Medium", 20), 
                                                                corner_radius=15)
                                                                



update_selected_button = customtkinter.CTkButton(master=install_bottom_frame, 
                                                                command=lambda:compile_selected(2), 
                                                                fg_color="#0b57c2", 
                                                                hover_color="#F5681C", 
                                                                text=" Oppdater Valgte ", 
                                                                text_font=("Roboto Medium", 20),
                                                                corner_radius=15)

uninstall_selected_button = customtkinter.CTkButton(master=install_bottom_frame, 
                                                                command=lambda:compile_selected(3), 
                                                                fg_color="#0b57c2", 
                                                                hover_color="#F5681C", 
                                                                text="Avinstaller Valgte", 
                                                                text_font=("Roboto Medium", 20),
                                                                corner_radius=15)

chosen_software_main_frame = customtkinter.CTkFrame(master=root, 
                                                        fg_color=("#d1d0cf", "#383838"), 
                                                        height=145, 
                                                        corner_radius=15)

style = ttk.Style()
style.theme_use("clam")
style.configure("Custom.Horizontal.TProgressbar", troughcolor = "#292929", background = "#0b57c2", bordercolor="#292929", lightcolor="#292929", darkcolor="#292929")


progressbar_frame = customtkinter.CTkFrame(master=chosen_software_main_frame, 
                                                        fg_color=("#d1d0cf", "#383838"), 
                                                         
                                                        corner_radius=15)


chosen_software_progressbar = ttk.Progressbar(master=progressbar_frame, 
                                                mode="indeterminate",
                                                style="Custom.Horizontal.TProgressbar",
                                                length=100)


"""chosen_software_progressbar = customtkinter.CTkProgressBar(master=progressbar_frame,
                                                        fg_color=("#c4c3c2", "#292929"), 
                                                        progress_color=("#0b57c2"), 
                                                        corner_radius=15, 
                                                        height=15)"""

output_label = customtkinter.CTkLabel(master=progressbar_frame, 
                                                        fg_color=("#c4c3c2", "#383838"),
                                                        text="Installerer valgte programmer WIP",
                                                        text_font=("Roboto Medium", 30),
                                                        corner_radius=15)

"""#Supertest
def read_doc():
    with open ("output.txt", "r") as f:
        f=f.read()
    super_test_label = customtkinter.CTkLabel(master=chosen_software_main_frame, 
                                        fg_color=("#c4c3c2", "green"), 
                                        corner_radius=15, 
                                        text=f, 
                                        text_font=("Roboto Medium", 13))
    super_test_label.pack()
    print("Reached here")"""

"""def change_label_size(): # Creating label frames based on how many labels are activated
    global labels_toggled
    if labels_toggled == 1:
        chosen_software_labelframe1 = customtkinter.CTkFrame(master=chosen_software_main_frame, fg_color=("#d1d0cf", "red"), corner_radius=15)
        chosen_software_labelframe1.pack(side="top", fill="both", expand=True)
        print("1")
    elif labels_toggled == 2:
        chosen_software_labelframe2 = customtkinter.CTkFrame(master=chosen_software_main_frame, fg_color=("#d1d0cf", "blue"), corner_radius=15)
        chosen_software_labelframe2.pack(side="top", fill="both", expand=True)
        print("2")
    elif labels_toggled == 3:
        chosen_software_labelframe3 = customtkinter.CTkFrame(master=chosen_software_main_frame, fg_color=("#d1d0cf", "yellow"), corner_radius=15)
        chosen_software_labelframe3.pack(side="top", fill="both", expand=True)
        print("3")
    elif labels_toggled == 4:
        chosen_software_labelframe4 = customtkinter.CTkFrame(master=chosen_software_main_frame, fg_color=("#d1d0cf", "green"), corner_radius=15)
        chosen_software_labelframe4.pack(side="top", fill="both", expand=True)
        print("4")
    elif labels_toggled > 5:
        print("max labelline toggled")
"""

# ==========Selected software Labels==========
#Browsers
chosen_firefox_label = customtkinter.CTkLabel(master = chosen_software_main_frame, image=firefox_image, width=20,  corner_radius=15)
chosen_chrome_label = customtkinter.CTkLabel(master = chosen_software_main_frame, image=chrome_image, width=20,  corner_radius=15 )
chosen_brave_label = customtkinter.CTkLabel(master = chosen_software_main_frame, image=brave_image, width=20,  corner_radius=15 )
chosen_vivaldi_label = customtkinter.CTkLabel(master = chosen_software_main_frame, image=vivaldi_image, width=20,  corner_radius=15 )
# Email Clients/Epost klienter
chosen_emclient_label = customtkinter.CTkLabel(master = chosen_software_main_frame, image=emclient_image, width=20,  corner_radius=15 )
chosen_thunderbird_label = customtkinter.CTkLabel(master = chosen_software_main_frame, image=thunderbird_image, width=20,  corner_radius=15 )
# Document management Labels
chosen_libre_office_label = customtkinter.CTkLabel(master = chosen_software_main_frame, image=libre_office_image, width=20,  corner_radius=15 )
chosen_open_office_label = customtkinter.CTkLabel(master = chosen_software_main_frame, image=open_office_image, width=20,  corner_radius=15 )
chosen_evernote_label = customtkinter.CTkLabel(master = chosen_software_main_frame, image=evernote_image, width=20,  corner_radius=15 )
chosen_onenote_label = customtkinter.CTkLabel(master = chosen_software_main_frame, image=onenote_image, width=20,  corner_radius=15 )
chosen_adobe_reader_label = customtkinter.CTkLabel(master = chosen_software_main_frame, image=adobe_reader_image, width=20,  corner_radius=15 )
# Media
chosen_vlc_label = customtkinter.CTkLabel(master = chosen_software_main_frame, image=vlc_image, width=20, corner_radius=15 )
chosen_spotify_label = customtkinter.CTkLabel(master = chosen_software_main_frame, image=spotify_image, width=20, corner_radius=15 )
chosen_itunes_label = customtkinter.CTkLabel(master = chosen_software_main_frame, image=itunes_image, width=20, corner_radius=15 )
chosen_tidal_label = customtkinter.CTkLabel(master = chosen_software_main_frame, image=tidal_image, width=20, corner_radius=15 )
chosen_k_lite_codec_pack_label = customtkinter.CTkLabel(master = chosen_software_main_frame, image=k_lite_codec_pack_image, width=20, corner_radius=15 )
# Games
chosen_steam_label = customtkinter.CTkLabel(master = chosen_software_main_frame, image=steam_image, width=20, corner_radius=15 )
chosen_epic_games_label = customtkinter.CTkLabel(master = chosen_software_main_frame, image=epic_games_image, width=20, corner_radius=15 )
chosen_gog_label = customtkinter.CTkLabel(master = chosen_software_main_frame, image=gog_image, width=20, corner_radius=15 )
chosen_ubisoft_label = customtkinter.CTkLabel(master = chosen_software_main_frame, image=ubisoft_image, width=20, corner_radius=15 )
chosen_origin_label = customtkinter.CTkLabel(master = chosen_software_main_frame, image=origin_image, width=20, corner_radius=15 )
#Images
chosen_gimp_label = customtkinter.CTkLabel(master = chosen_software_main_frame, image=gimp_image, width=20, corner_radius=15 )
chosen_greenshot_label = customtkinter.CTkLabel(master = chosen_software_main_frame, image=greenshot_image, width=20, corner_radius=15 )
chosen_irfanview_label = customtkinter.CTkLabel(master = chosen_software_main_frame, image=irfanview_image, width=20, corner_radius=15 )
#Cloud storage
chosen_onedrive_label = customtkinter.CTkLabel(master = chosen_software_main_frame, image=onedrive_image, width=20, corner_radius=15 )
chosen_dropbox_label = customtkinter.CTkLabel(master = chosen_software_main_frame, image=dropbox_image, width=20, corner_radius=15 )
chosen_google_drive_label = customtkinter.CTkLabel(master = chosen_software_main_frame, image=google_drive_image, width=20, corner_radius=15 )
#Communication
chosen_discord_label = customtkinter.CTkLabel(master = chosen_software_main_frame, image=discord_image, width=20, corner_radius=15 )
chosen_skype_label = customtkinter.CTkLabel(master = chosen_software_main_frame, image=skype_image, width=20, corner_radius=15 )
chosen_zoom_label = customtkinter.CTkLabel(master = chosen_software_main_frame, image=zoom_image, width=20, corner_radius=15 )
chosen_teamviewer_label = customtkinter.CTkLabel(master = chosen_software_main_frame, image=teamviewer_image, width=20, corner_radius=15 )
#Compression
chosen_seven_zip_label = customtkinter.CTkLabel(master = chosen_software_main_frame, image=seven_zip_image, width=20,  corner_radius=15 )
chosen_peazip_label = customtkinter.CTkLabel(master = chosen_software_main_frame, image=peazip_image, width=20,  corner_radius=15 )
#Streaming
chosen_obs_label = customtkinter.CTkLabel(master = chosen_software_main_frame, image=obs_image, width=20,  corner_radius=15 )
#Geforce label created under #Drivers
chosen_elgato_label = customtkinter.CTkLabel(master = chosen_software_main_frame, image=elgato_image, width=20,  corner_radius=15 )
#RGB
chosen_icue_label = customtkinter.CTkLabel(master = chosen_software_main_frame, image=icue_image, width=20,  corner_radius=15)
chosen_nzxt_label = customtkinter.CTkLabel(master = chosen_software_main_frame, image=nzxt_image, width=20,  corner_radius=15)
chosen_msi_label = customtkinter.CTkLabel(master = chosen_software_main_frame, image=msi_image, width=20,  corner_radius=15)
chosen_asus_label = customtkinter.CTkLabel(master = chosen_software_main_frame, image=asus_armourycrate_image, width=20,  corner_radius=15)
chosen_gigabyte_label = customtkinter.CTkLabel(master = chosen_software_main_frame, image=gigabyte_image, width=20,  corner_radius=15)
chosen_lianli_label = customtkinter.CTkLabel(master = chosen_software_main_frame, image=lianli_image, width=20,  corner_radius=15)
chosen_openrgb_label = customtkinter.CTkLabel(master = chosen_software_main_frame, image=openrgb_image, width=20,  corner_radius=15)
#Drivers
chosen_intel_label = customtkinter.CTkLabel(master = chosen_software_main_frame, image=intel_image, width=20, corner_radius=15)
chosen_nv_cleaninstall_label = customtkinter.CTkLabel(master = chosen_software_main_frame, image=nv_cleaninstall_image, width=20, corner_radius=15)
chosen_geforce_experience_label = customtkinter.CTkLabel(master = chosen_software_main_frame, image=geforce_experience_image, width=20,  corner_radius=15)
chosen_lenovo_label = customtkinter.CTkLabel(master = chosen_software_main_frame, image=lenovo_image, width=20, corner_radius=15)

chosen_unchecky_label = customtkinter.CTkLabel(master = chosen_software_main_frame, image=unchecky_image, width=20,  corner_radius=15 )



def unpack_chosen_labels():
    for label in (chosen_firefox_label, chosen_chrome_label, chosen_brave_label, chosen_vivaldi_label, 
    chosen_emclient_label, chosen_thunderbird_label, chosen_libre_office_label, chosen_open_office_label, chosen_evernote_label, 
    chosen_onenote_label, chosen_adobe_reader_label, chosen_vlc_label, chosen_spotify_label, chosen_itunes_label, chosen_tidal_label, chosen_k_lite_codec_pack_label, 
    chosen_steam_label, chosen_epic_games_label, chosen_gog_label, chosen_ubisoft_label, chosen_origin_label, chosen_gimp_label, chosen_irfanview_label, chosen_greenshot_label, 
    chosen_onedrive_label, chosen_dropbox_label, chosen_google_drive_label, chosen_discord_label, chosen_skype_label, chosen_zoom_label, chosen_teamviewer_label, 
    chosen_seven_zip_label, chosen_peazip_label, chosen_obs_label, chosen_geforce_experience_label, chosen_elgato_label, chosen_icue_label, chosen_nzxt_label, chosen_msi_label, 
    chosen_intel_label, chosen_nv_cleaninstall_label, chosen_lenovo_label, chosen_unchecky_label):
        label.pack_forget()




# ==========Support screen (No packing)==========
support_frame = customtkinter.CTkFrame(master=root, 
                                                    fg_color=("#d1d0cf", "#292929"), 
                                                    corner_radius=15)

support_headline_frame = customtkinter.CTkFrame(master=support_frame, 
                                                    fg_color=("#c4c3c2", "#383838"), 
                                                    corner_radius=15, 
                                                    height=20)

support_headline_label = customtkinter.CTkLabel(master=support_headline_frame, 
                                                    text="Hjelp og kontaktinformasjon", 
                                                    text_font=("Roboto Medium", 30))

support_frame2 = customtkinter.CTkFrame(master=support_frame, 
                                        fg_color=("#c4c3c2", "#383838"), 
                                        corner_radius=15)

with open("Text\\Contact.txt", encoding="utf-8") as r:
    contact_text = r.read()

with open("Text\\Support.txt", encoding="utf-8") as r:
    support_text = r.read()

support_top_label = customtkinter.CTkLabel(master=support_frame2, 
                                                    fg_color=("#c4c3c2", "#383838"), 
                                                    corner_radius=15, 
                                                    text=contact_text, 
                                                    text_font=("Roboto Medium", 20))
support_bottom_label = customtkinter.CTkLabel(master=support_frame2, 
                                                    fg_color=("#c4c3c2", "#383838"), 
                                                    corner_radius=15, 
                                                    text=support_text, 
                                                    text_font=("Roboto Medium", 13))


support_teamviewer_frame = customtkinter.CTkFrame(master= support_frame2,
                                                    fg_color=("#c4c3c2", "#383838"), 
                                                    corner_radius=15)

teamviewer_support_icon = customtkinter.CTkLabel(support_teamviewer_frame, text ="Teamviewer ikon: ", text_font=("Roboto Medium", 20), compound="right", image=teamviewer_image)




def toggle_category_frame(args):
    # Every time the function is called it hides previously created frames.
    for frame in (category1_frame, category2_frame, category3_frame, category4_frame, category5_frame, category6_frame
    , category7_frame, category8_frame, category9_frame, category10_frame, category11_frame, category12_frame):
        frame.pack_forget()
    standardpakke_frame.pack_forget()
    for button in (category1_tab, category2_tab, category3_tab, category4_tab, category5_tab, category6_tab
    , category7_tab, category8_tab, category9_tab, category10_tab, category11_tab, category12_tab):
        button.configure(fg_color="#0B57C2")
    if args == 1:
        category1_frame.pack(pady=5, padx=5, fill="both", expand=True)
        category1_headline_frame.pack(pady=5, padx=5, fill="x")
        category1_headline_label.pack()
        for frame in (category1_software_frame1, category1_software_frame2, category1_software_frame3, 
        category1_software_frame4):
            frame.pack(pady=5, padx=5, fill="x") 
        for button in (firefox_check, chrome_check, brave_check, vivaldi_check):
            button.pack(side="left", fill="y")
        for label in (category1_software_label1, category1_software_label2, category1_software_label3, 
        category1_software_label4):
            label.pack(side="left")
        category1_tab.configure(fg_color="#F5681C")
    
    if args == 2:
        category2_frame.pack(pady=5, padx=5, fill="both", expand=True)
        category2_headline_frame.pack(pady=5, padx=5, fill="x")
        category2_headline_label.pack()
        for frame in (category2_software_frame1, category2_software_frame2):
            frame.pack(pady=5, padx=5, fill="x")
        for button in (emclient_check, thunderbird_check):
            button.pack(side="left", fill="y")
        for label in (category2_software_label1, category2_software_label2):
            label.pack(side="left")
        category2_tab.configure(fg_color="#F5681C")

    
    if args == 3:
        category3_frame.pack(pady=5, padx=5, fill="both", expand=True)
        category3_headline_frame.pack(pady=5, padx=5, fill="x")
        category3_headline_label.pack()
        for frame in (category3_software_frame1, category3_software_frame2, category3_software_frame3, 
        category3_software_frame4, category3_software_frame5):
            frame.pack(pady=5, padx=5, fill="x")
        for button in (libre_office_check, open_office_check, evernote_check, onenote_check, adobe_reader_check):
            button.pack(side="left", fill="y")
        for label in (category3_software_label1, category3_software_label2, category3_software_label3, 
        category3_software_label4, category3_software_label5):
            label.pack(side="left")
        category3_tab.configure(fg_color="#F5681C")

    if args == 4:
        category4_frame.pack(pady=5, padx=5, fill="both", expand=True)
        category4_headline_frame.pack(pady=5, padx=5, fill="x")
        category4_headline_label.pack()
        for frame in (category4_software_frame1, category4_software_frame2, category4_software_frame3, 
        category4_software_frame4, category4_software_frame5):
            frame.pack(pady=5, padx=5, fill="x")
        for button in (vlc_check, spotify_check, itunes_check, tidal_check, k_lite_codec_pack_check):
            button.pack(side="left", fill="y")
        for label in (category4_software_label1, category4_software_label2, category4_software_label3, 
        category4_software_label4, category4_software_label5):
            label.pack(side="left")
        category4_tab.configure(fg_color="#F5681C")

    if args == 5:
        category5_frame.pack(pady=5, padx=5, fill="both", expand=True)
        category5_headline_frame.pack(pady=5, padx=5, fill="x")
        category5_headline_label.pack()  
        for frame in (category5_software_frame1, category5_software_frame2, category5_software_frame3, 
        category5_software_frame4, category5_software_frame5):
            frame.pack(pady=5, padx=5, fill="x")
        for button in (steam_check, epic_check, gog_check, ubisoft_check, origin_check):
            button.pack(side="left", fill="y")
        for label in (category5_software_label1, category5_software_label2, category5_software_label3, 
        category5_software_label4, category5_software_label5):
            label.pack(side="left")   
        category5_tab.configure(fg_color="#F5681C")    


    if args == 6:
        category6_frame.pack(pady=5, padx=5, fill="both", expand=True)
        category6_headline_frame.pack(pady=5, padx=5, fill="x")
        category6_headline_label.pack()
        for frame in (category6_software_frame1, category6_software_frame2, category6_software_frame3):
            frame.pack(pady=5, padx=5, fill="x")
        for button in (gimp_check, greenshot_check, irfanview_check):
            button.pack(side="left", fill="y")
        for label in (category6_software_label1, category6_software_label2, category6_software_label3):
            label.pack(side="left")
        category6_tab.configure(fg_color="#F5681C")
        

    if args == 7:
        category7_frame.pack(pady=5, padx=5, fill="both", expand=True)
        category7_headline_frame.pack(pady=5, padx=5, fill="x")
        category7_headline_label.pack()

        for frame in (category7_software_frame1, category7_software_frame2, category7_software_frame3):
            frame.pack(pady=5, padx=5, fill="x")
        for button in (onedrive_check, dropbox_check, google_drive_check):
            button.pack(side="left", fill="y")
        for label in (category7_software_label1, category7_software_label2, category7_software_label3):
            label.pack(side="left")
        category7_tab.configure(fg_color="#F5681C")


    if args == 8:
        category8_frame.pack(pady=5, padx=5, fill="both", expand=True)
        category8_headline_frame.pack(pady=5, padx=5, fill="x")
        category8_headline_label.pack()

        for frame in (category8_software_frame1, category8_software_frame2, category8_software_frame3, category8_software_frame4):
            frame.pack(pady=5, padx=5, fill="x")
        for button in (discord_check, skype_check, zoom_check, teamviewer_check):
            button.pack(side="left", fill="y")
        for label in (category8_software_label1, category8_software_label2, category8_software_label3, category8_software_label4):
            label.pack(side="left")
        category8_tab.configure(fg_color="#F5681C")
    
    if args == 9:
        category9_frame.pack(pady=5, padx=5, fill="both", expand=True)
        category9_headline_frame.pack(pady=5, padx=5, fill="x")
        category9_headline_label.pack()

        for frame in (category9_software_frame1, category9_software_frame2):
            frame.pack(pady=5, padx=5, fill="x")
        for button in (seven_zip_check, peazip_check):
            button.pack(side="left", fill="y")
        for label in (category9_software_label1, category9_software_label2):
            label.pack(side="left")
        category9_tab.configure(fg_color="#F5681C")

    if args == 10:
        category10_frame.pack(pady=5, padx=5, fill="both", expand=True)
        category10_headline_frame.pack(pady=5, padx=5, fill="x")
        category10_headline_label.pack()

        for frame in (category10_software_frame1, category10_software_frame2, category10_software_frame3):
            frame.pack(pady=5, padx=5, fill="x")
        for button in (obs_check, shadowplay_check, elgato_check):
            button.pack(side="left", fill="y")
        for label in (category10_software_label1, category10_software_label2, category10_software_label3):
            label.pack(side="left")
        category10_tab.configure(fg_color="#F5681C")
   
   
    if args == 11:
        category11_frame.pack(pady=5, padx=5, fill="both", expand=True)
        category11_headline_frame.pack(pady=5, padx=5, fill="x")
        category11_headline_label.pack()
        category11_frame_left.pack(fill="both", side="left", pady=10)
        category11_frame_right.pack(fill="both", side="right", pady=10)
    
        for frame in (category11_software_frame1, category11_software_frame2, category11_software_frame3, 
            category11_software_frame4, category11_software_frame5, category11_software_frame6, category11_software_frame7):
                    frame.pack(pady=5, padx=5, fill="x")
        for button in (icue_check, nzxt_check, msi_check, asus_check, gigabyte_check, lianli_check, openrgb_check):
            button.pack(side="left", fill="y")
        for label in (category11_software_label1, category11_software_label2, category11_software_label3, 
            category11_software_label4, category11_software_label5, category11_software_label6, category11_software_label7):
                    label.pack(side="left")
        category11_tab.configure(fg_color="#F5681C")


    if args == 12:
        category12_frame.pack(pady=5, padx=5, fill="both", expand=True)
        category12_headline_frame.pack(pady=5, padx=5, fill="x")
        category12_headline_label.pack()
        category12_frame_left.pack(fill="both", side="left", pady=10)
        category12_frame_right.pack(fill="both", side="right", pady=10)

        for frame in (category12_software_frame1, category12_software_frame2, category12_software_frame3, 
        category12_software_frame4, category12_software_frame5, category12_software_frame6, category12_software_frame7):
            frame.pack(pady=5, padx=5, fill="x")
        for button in (intel_check, nv_cleaninstall_check, lenovo_check, geforce_experience_check, amd_check, asus_ac_check, 
        gigabyte_app_center_check):
            button.pack(side="left", fill="y")
        for label in (category12_software_label1, category12_software_label2, category12_software_label3, 
        category12_software_label4, category12_software_label5, category12_software_label6, category12_software_label7):
            label.pack(side="left")
        category12_tab.configure(fg_color="#F5681C")




# ==========Software Tabs Buttons==========
category1_tab = customtkinter.CTkButton(master=software_tabs_frame1, fg_color="#0B57C2", hover_color="#F5681C", text="Nettlesere", text_font=("Roboto Medium", 15), height= 50, corner_radius=15, command=lambda:toggle_category_frame(1))
category2_tab = customtkinter.CTkButton(master=software_tabs_frame1, fg_color="#0B57C2", hover_color="#F5681C", text="E-post Klienter", text_font=("Roboto Medium", 15), height= 50, corner_radius=15, command=lambda:toggle_category_frame(2))
category3_tab = customtkinter.CTkButton(master=software_tabs_frame1, fg_color="#0B57C2", hover_color="#F5681C", text="Dokumentbehandling", text_font=("Roboto Medium", 15), height= 50, corner_radius=15, command=lambda:toggle_category_frame(3))
category4_tab = customtkinter.CTkButton(master=software_tabs_frame1, fg_color="#0B57C2", hover_color="#F5681C", text="Media", text_font=("Roboto Medium", 15), height= 50, corner_radius=15, command=lambda:toggle_category_frame(4))
category5_tab = customtkinter.CTkButton(master=software_tabs_frame1, fg_color="#0B57C2", hover_color="#F5681C", text="Spill", text_font=("Roboto Medium", 15), height= 50, corner_radius=15, command=lambda:toggle_category_frame(5))
category6_tab = customtkinter.CTkButton(master=software_tabs_frame1, fg_color="#0B57C2", hover_color="#F5681C", text="Bilderedigering", text_font=("Roboto Medium", 15), height= 50, corner_radius=15, command=lambda:toggle_category_frame(6))
category7_tab = customtkinter.CTkButton(master=software_tabs_frame2, fg_color="#0B57C2", hover_color="#F5681C", text="Skylagring", text_font=("Roboto Medium", 15), height= 50, corner_radius=15, command=lambda:toggle_category_frame(7))
category8_tab = customtkinter.CTkButton(master=software_tabs_frame2, fg_color="#0B57C2", hover_color="#F5681C", text="Kommunikasjon", text_font=("Roboto Medium", 15), height= 50, corner_radius=15, command=lambda:toggle_category_frame(8))
category9_tab = customtkinter.CTkButton(master=software_tabs_frame2, fg_color="#0B57C2", hover_color="#F5681C", text="Komprimering", text_font=("Roboto Medium", 15), height= 50, corner_radius=15, command=lambda:toggle_category_frame(9))
category10_tab = customtkinter.CTkButton(master=software_tabs_frame2, fg_color="#0B57C2", hover_color="#F5681C", text="Streaming", text_font=("Roboto Medium", 15), height= 50, corner_radius=15, command=lambda:toggle_category_frame(10))
category11_tab = customtkinter.CTkButton(master=software_tabs_frame2, fg_color="#0B57C2", hover_color="#F5681C", text="RGB", text_font=("Roboto Medium", 15), height= 50, corner_radius=15, command=lambda:toggle_category_frame(11))
category12_tab = customtkinter.CTkButton(master=software_tabs_frame2, fg_color="#0B57C2", hover_color="#F5681C", text="Drivere", text_font=("Roboto Medium", 15), height= 50, corner_radius=15, command=lambda:toggle_category_frame(12))





# ==========Category 1 frame, headline, software frames==========
category1_frame = customtkinter.CTkFrame(master=install_frame, 
                                            fg_color=("#c4c3c2", "#383838"), 
                                            corner_radius=15)
category1_headline_frame = customtkinter.CTkFrame(master=category1_frame, 
                                            fg_color=("#c4c3c2", "#383838"), 
                                            corner_radius=15, 
                                            height=20)
category1_headline_label = customtkinter.CTkLabel(master=category1_headline_frame, 
                                            text="Nettlesere", 
                                            text_font=("Roboto Medium", 20))   

category1_software_frame1 = customtkinter.CTkFrame(master=category1_frame, fg_color=("#c4c3c2", "#383838"), corner_radius=15)
category1_software_frame2 = customtkinter.CTkFrame(master=category1_frame, fg_color=("#c4c3c2", "#383838"), corner_radius=15)
category1_software_frame3 = customtkinter.CTkFrame(master=category1_frame, fg_color=("#c4c3c2", "#383838"), corner_radius=15)
category1_software_frame4 = customtkinter.CTkFrame(master=category1_frame, fg_color=("#c4c3c2", "#383838"), corner_radius=15)
category1_software_frame5 = customtkinter.CTkFrame(master=category1_frame, fg_color=("#c4c3c2", "#383838"), corner_radius=15)

category1_software_label1 = customtkinter.CTkLabel(master=category1_software_frame1, fg_color=("#c4c3c2", "#383838"), text="Mozilla Firefox er en nettleser som fokuserer på sikkerhet og alt fra enkel bruk til veldig avansert", justify="left", text_font=("Roboto Medium", 15), corner_radius=15)
category1_software_label2 = customtkinter.CTkLabel(master=category1_software_frame2, fg_color=("#c4c3c2", "#383838"), text="Google Chrome er verdens mest brukte nettleser", justify="left", text_font=("Roboto Medium", 15), corner_radius=15)
category1_software_label3 = customtkinter.CTkLabel(master=category1_software_frame3, fg_color=("#c4c3c2", "#383838"), text="Brave er en nettleser som fokuserer på cryptovaluta og blokkering av reklame", justify="left", text_font=("Roboto Medium", 15), corner_radius=15)
category1_software_label4 = customtkinter.CTkLabel(master=category1_software_frame4, fg_color=("#c4c3c2", "#383838"), text="Vivaldi er en nettleser som utviklet av nordmenn. De har hovedkontor i Oslo", justify="left", text_font=("Roboto Medium", 15), corner_radius=15)





# ==========Category 2 frame, headline, software frames==========
category2_frame = customtkinter.CTkFrame(master=install_frame, 
                                            fg_color=("#c4c3c2", "#383838"), 
                                            corner_radius=15)
category2_headline_frame = customtkinter.CTkFrame(master=category2_frame, 
                                            fg_color=("#c4c3c2", "#383838"), 
                                            corner_radius=15, 
                                            height=20)
category2_headline_label = customtkinter.CTkLabel(master=category2_headline_frame, 
                                            text="E-post klienter", 
                                            text_font=("Roboto Medium", 20)) 

category2_software_frame1 = customtkinter.CTkFrame(master=category2_frame, fg_color=("#c4c3c2", "#383838"), corner_radius=15)
category2_software_frame2 = customtkinter.CTkFrame(master=category2_frame, fg_color=("#c4c3c2", "#383838"), corner_radius=15)

category2_software_label1 = customtkinter.CTkLabel(master=category2_software_frame1, fg_color=("#c4c3c2", "#383838"), text="EM Client er en moderne e-post klient som har de fleste funskjoner man måtte trenger", justify="left", text_font=("Roboto Medium", 15), corner_radius=15)
category2_software_label2 = customtkinter.CTkLabel(master=category2_software_frame2, fg_color=("#c4c3c2", "#383838"), text="Mozilla Thunderbird er den mest populære gratis e-post klienten for Windows", justify="left", text_font=("Roboto Medium", 15), corner_radius=15)

# ==========Category 3 frame, headline, software frames==========
category3_frame = customtkinter.CTkFrame(master=install_frame, 
                                            fg_color=("#c4c3c2", "#383838"), 
                                            corner_radius=15)
category3_headline_frame = customtkinter.CTkFrame(master=category3_frame, 
                                            fg_color=("#c4c3c2", "#383838"), 
                                            corner_radius=15, 
                                            height=20)
category3_headline_label = customtkinter.CTkLabel(master=category3_headline_frame, 
                                            text="Dokumentbehandling", 
                                            text_font=("Roboto Medium", 20)) 

category3_software_frame1 = customtkinter.CTkFrame(master=category3_frame, fg_color=("#c4c3c2", "#383838"), corner_radius=15)
category3_software_frame2 = customtkinter.CTkFrame(master=category3_frame, fg_color=("#c4c3c2", "#383838"), corner_radius=15)
category3_software_frame3 = customtkinter.CTkFrame(master=category3_frame, fg_color=("#c4c3c2", "#383838"), corner_radius=15)
category3_software_frame4 = customtkinter.CTkFrame(master=category3_frame, fg_color=("#c4c3c2", "#383838"), corner_radius=15)
category3_software_frame5 = customtkinter.CTkFrame(master=category3_frame, fg_color=("#c4c3c2", "#383838"), corner_radius=15)

category3_software_label1 = customtkinter.CTkLabel(master=category3_software_frame1, fg_color=("#c4c3c2", "#383838"), text="LibreOffice videreutvikler fra fundamentet til OpenOffice", justify="left", text_font=("Roboto Medium", 15), corner_radius=15)
category3_software_label2 = customtkinter.CTkLabel(master=category3_software_frame2, fg_color=("#c4c3c2", "#383838"), text="OpenOffice kjenner de fleste til. Denne pakken har mye av de samme egenskapene som Microsoft Office", justify="left", text_font=("Roboto Medium", 15), corner_radius=15)
category3_software_label3 = customtkinter.CTkLabel(master=category3_software_frame3, fg_color=("#c4c3c2", "#383838"), text="Evernote anses som den beste programvaren for notater", justify="left", text_font=("Roboto Medium", 15), corner_radius=15)
category3_software_label4 = customtkinter.CTkLabel(master=category3_software_frame4, fg_color=("#c4c3c2", "#383838"), text="OneNote kan integreres med resten av Microsoft 365 på en sømløs måte", justify="left", text_font=("Roboto Medium", 15), corner_radius=15)
category3_software_label5 = customtkinter.CTkLabel(master=category3_software_frame5, fg_color=("#c4c3c2", "#383838"), text="Adobe Acrobat Reader brukes til å lese og redigere PDF filer", justify="left", text_font=("Roboto Medium", 15), corner_radius=15)

# ==========Category 4 frame, headline, software frames==========
category4_frame = customtkinter.CTkFrame(master=install_frame, 
                                            fg_color=("#c4c3c2", "#383838"), 
                                            corner_radius=15)
category4_headline_frame = customtkinter.CTkFrame(master=category4_frame, 
                                            fg_color=("#c4c3c2", "#383838"), 
                                            corner_radius=15, 
                                            height=20)
category4_headline_label = customtkinter.CTkLabel(master=category4_headline_frame, 
                                            text="Media", 
                                            text_font=("Roboto Medium", 20)) 

category4_software_frame1 = customtkinter.CTkFrame(master=category4_frame, fg_color=("#c4c3c2", "#383838"), corner_radius=15)
category4_software_frame2 = customtkinter.CTkFrame(master=category4_frame, fg_color=("#c4c3c2", "#383838"), corner_radius=15)
category4_software_frame3 = customtkinter.CTkFrame(master=category4_frame, fg_color=("#c4c3c2", "#383838"), corner_radius=15)
category4_software_frame4 = customtkinter.CTkFrame(master=category4_frame, fg_color=("#c4c3c2", "#383838"), corner_radius=15)
category4_software_frame5 = customtkinter.CTkFrame(master=category4_frame, fg_color=("#c4c3c2", "#383838"), corner_radius=15)

category4_software_label1 = customtkinter.CTkLabel(master=category4_software_frame1, fg_color=("#c4c3c2", "#383838"), text="VLC støtter (nesten) alle typer videofiler og har en rekke funksjoner for både avanserte og enkle brukere", justify="left", text_font=("Roboto Medium", 15), corner_radius=15)
category4_software_label2 = customtkinter.CTkLabel(master=category4_software_frame2, fg_color=("#c4c3c2", "#383838"), text="Alle kjenner til Spotify. Verdens største musikk strømmetjeneste", justify="left", text_font=("Roboto Medium", 15), corner_radius=15)
category4_software_label3 = customtkinter.CTkLabel(master=category4_software_frame3, fg_color=("#c4c3c2", "#383838"), text="iTunes hjelper deg overføre data fra Apple produkter og fungerer som en digital musikkbutikk", justify="left", text_font=("Roboto Medium", 15), corner_radius=15)
category4_software_label4 = customtkinter.CTkLabel(master=category4_software_frame4, fg_color=("#c4c3c2", "#383838"), text="Tidal er en musikk strømmetjeneste som leverer HiFi lydkvalitet", justify="left", text_font=("Roboto Medium", 15), corner_radius=15)
category4_software_label5 = customtkinter.CTkLabel(master=category4_software_frame5, fg_color=("#c4c3c2", "#383838"), text="K-Lite Codec dekoder video og lydfiler for optimal kvalitet.\n Man får også med Media Player Classic for den klassiske Windows XP stilen.", justify="left", text_font=("Roboto Medium", 15), corner_radius=15)

# ==========Category 5 frame, headline, software frames==========
category5_frame = customtkinter.CTkFrame(master=install_frame, 
                                            fg_color=("#c4c3c2", "#383838"), 
                                            corner_radius=15)
category5_headline_frame = customtkinter.CTkFrame(master=category5_frame, 
                                            fg_color=("#c4c3c2", "#383838"), 
                                            corner_radius=15, 
                                            height=20)
category5_headline_label = customtkinter.CTkLabel(master=category5_headline_frame, 
                                            text="Spill", 
                                            text_font=("Roboto Medium", 20))

category5_software_frame1 = customtkinter.CTkFrame(master=category5_frame, fg_color=("#c4c3c2", "#383838"), corner_radius=15)
category5_software_frame2 = customtkinter.CTkFrame(master=category5_frame, fg_color=("#c4c3c2", "#383838"), corner_radius=15)
category5_software_frame3 = customtkinter.CTkFrame(master=category5_frame, fg_color=("#c4c3c2", "#383838"), corner_radius=15)
category5_software_frame4 = customtkinter.CTkFrame(master=category5_frame, fg_color=("#c4c3c2", "#383838"), corner_radius=15)
category5_software_frame5 = customtkinter.CTkFrame(master=category5_frame, fg_color=("#c4c3c2", "#383838"), corner_radius=15)

category5_software_label1 = customtkinter.CTkLabel(master=category5_software_frame1, fg_color=("#c4c3c2", "#383838"), text="Steam er en digital distribusjons spill og kommunikasjonsplatform", justify="left", text_font=("Roboto Medium", 15), corner_radius=15)
category5_software_label2 = customtkinter.CTkLabel(master=category5_software_frame2, fg_color=("#c4c3c2", "#383838"), text="Epic games er tilsvarende Steam", justify="left", text_font=("Roboto Medium", 15), corner_radius=15)
category5_software_label3 = customtkinter.CTkLabel(master=category5_software_frame3, fg_color=("#c4c3c2", "#383838"), text="GOG Galaxy begynte med fokus på eldre spill, men har utvidet til å ha nyere spill også.\nStort fokus på digitale eier rettigheter", justify="left", text_font=("Roboto Medium", 15), corner_radius=15)
category5_software_label4 = customtkinter.CTkLabel(master=category5_software_frame4, fg_color=("#c4c3c2", "#383838"), text="Ubisoft Connect er Ubisoft sin digitale spilldistrubisjons platform", justify="left", text_font=("Roboto Medium", 15), corner_radius=15)
category5_software_label5 = customtkinter.CTkLabel(master=category5_software_frame5, fg_color=("#c4c3c2", "#383838"), text="Origin er EA sin digitale spilldistrubisjons platform", justify="left", text_font=("Roboto Medium", 15), corner_radius=15)

# ==========Category 6 frame, headline, software frames==========
category6_frame = customtkinter.CTkFrame(master=install_frame, 
                                            fg_color=("#c4c3c2", "#383838"), 
                                            corner_radius=15)
category6_headline_frame = customtkinter.CTkFrame(master=category6_frame, 
                                            fg_color=("#c4c3c2", "#383838"), 
                                            corner_radius=15, 
                                            height=20)
category6_headline_label = customtkinter.CTkLabel(master=category6_headline_frame, 
                                            text="Bilderedigering", 
                                            text_font=("Roboto Medium", 20)) 

category6_software_frame1 = customtkinter.CTkFrame(master=category6_frame, fg_color=("#c4c3c2", "#383838"), corner_radius=15)
category6_software_frame2 = customtkinter.CTkFrame(master=category6_frame, fg_color=("#c4c3c2", "#383838"), corner_radius=15)
category6_software_frame3 = customtkinter.CTkFrame(master=category6_frame, fg_color=("#c4c3c2", "#383838"), corner_radius=15)

category6_software_label1 = customtkinter.CTkLabel(master=category6_software_frame1, fg_color=("#c4c3c2", "#383838"), text="GIMP er et av de beste gratis bilderedigeringsprogrammene.\nDet har alle de mest brukte funksjonene og kan måles med de fleste betalbare programmene", justify="left", text_font=("Roboto Medium", 15), corner_radius=15)
category6_software_label2 = customtkinter.CTkLabel(master=category6_software_frame2, fg_color=("#c4c3c2", "#383838"), text="IrfanView er primært utviklet for bildevisning men det har en robust bilderedigerinsfunskjon", justify="left", text_font=("Roboto Medium", 15), corner_radius=15)
category6_software_label3 = customtkinter.CTkLabel(master=category6_software_frame3, fg_color=("#c4c3c2", "#383838"), text="Greenshot er et lettvekt program for å raskt ta skjermbilde og redigere disse", justify="left", text_font=("Roboto Medium", 15), corner_radius=15)

# ==========Category 7 frame, headline, software frames==========
category7_frame = customtkinter.CTkFrame(master=install_frame, 
                                            fg_color=("#c4c3c2", "#383838"), 
                                            corner_radius=15)
category7_headline_frame = customtkinter.CTkFrame(master=category7_frame, 
                                            fg_color=("#c4c3c2", "#383838"), 
                                            corner_radius=15, 
                                            height=20)
category7_headline_label = customtkinter.CTkLabel(master=category7_headline_frame, 
                                            text="Skylagring", 
                                            text_font=("Roboto Medium", 20)) 

category7_software_frame1 = customtkinter.CTkFrame(master=category7_frame, fg_color=("#c4c3c2", "#383838"), corner_radius=15)
category7_software_frame2 = customtkinter.CTkFrame(master=category7_frame, fg_color=("#c4c3c2", "#383838"), corner_radius=15)
category7_software_frame3 = customtkinter.CTkFrame(master=category7_frame, fg_color=("#c4c3c2", "#383838"), corner_radius=15)

category7_software_label1 = customtkinter.CTkLabel(master=category7_software_frame1, fg_color=("#c4c3c2", "#383838"), text="OneDrive er laget av Microsoft og integreres sømløst i Windows\nMan får 5GB gratis lagring og kan utvide dette ved å verve andre", justify="left", text_font=("Roboto Medium", 15), corner_radius=15)
category7_software_label2 = customtkinter.CTkLabel(master=category7_software_frame2, fg_color=("#c4c3c2", "#383838"), text="Dropbox tilbyr 2GB gratis lagringsplass", justify="left", text_font=("Roboto Medium", 15), corner_radius=15)
category7_software_label3 = customtkinter.CTkLabel(master=category7_software_frame3, fg_color=("#c4c3c2", "#383838"), text="Google Drive har man allerede dersom man bruker en Android telefon. Man får får 15GB gratis", justify="left", text_font=("Roboto Medium", 15), corner_radius=15)

# ==========Category 8 frame, headline, software frames==========
category8_frame = customtkinter.CTkFrame(master=install_frame, 
                                            fg_color=("#c4c3c2", "#383838"), 
                                            corner_radius=15)
category8_headline_frame = customtkinter.CTkFrame(master=category8_frame, 
                                            fg_color=("#c4c3c2", "#383838"), 
                                            corner_radius=15, 
                                            height=20)
category8_headline_label = customtkinter.CTkLabel(master=category8_headline_frame, 
                                            text="Kommunikasjon", 
                                            text_font=("Roboto Medium", 20)) 

category8_software_frame1 = customtkinter.CTkFrame(master=category8_frame, fg_color=("#c4c3c2", "#383838"), corner_radius=15)
category8_software_frame2 = customtkinter.CTkFrame(master=category8_frame, fg_color=("#c4c3c2", "#383838"), corner_radius=15)
category8_software_frame3 = customtkinter.CTkFrame(master=category8_frame, fg_color=("#c4c3c2", "#383838"), corner_radius=15)
category8_software_frame4 = customtkinter.CTkFrame(master=category8_frame, fg_color=("#c4c3c2", "#383838"), corner_radius=15)

category8_software_label1 = customtkinter.CTkLabel(master=category8_software_frame1, fg_color=("#c4c3c2", "#383838"), text="Discord er det mest utbredte programmet for muntlig kommunikasjon blant yngre.\nBrukes i forbindelse med spill, hobbyer og interessegrupper.", justify="left", text_font=("Roboto Medium", 15), corner_radius=15)
category8_software_label2 = customtkinter.CTkLabel(master=category8_software_frame2, fg_color=("#c4c3c2", "#383838"), text="De fleste kjenner til Skype. Mye brukt i bedriftsmarkedet.", justify="left", text_font=("Roboto Medium", 15), corner_radius=15)
category8_software_label3 = customtkinter.CTkLabel(master=category8_software_frame3, fg_color=("#c4c3c2", "#383838"), text="Verdens mest populære videokonferanseprogram.", justify="left", text_font=("Roboto Medium", 15), corner_radius=15)
category8_software_label4 = customtkinter.CTkLabel(master=category8_software_frame4, fg_color=("#c4c3c2", "#383838"), text="Fjernstyring. Deler skjerm med motparten. Brukes som regel for å hjelpe eller får hjelp.", justify="left", text_font=("Roboto Medium", 15), corner_radius=15)

# ==========Category 9 frame, headline, software frames==========
category9_frame = customtkinter.CTkFrame(master=install_frame, 
                                            fg_color=("#c4c3c2", "#383838"), 
                                            corner_radius=15)
category9_headline_frame = customtkinter.CTkFrame(master=category9_frame, 
                                            fg_color=("#c4c3c2", "#383838"), 
                                            corner_radius=15, 
                                            height=20)
category9_headline_label = customtkinter.CTkLabel(master=category9_headline_frame, 
                                            text="Komprimering", 
                                            text_font=("Roboto Medium", 20)) 

category9_software_frame1 = customtkinter.CTkFrame(master=category9_frame, fg_color=("#c4c3c2", "#383838"), corner_radius=15)
category9_software_frame2 = customtkinter.CTkFrame(master=category9_frame, fg_color=("#c4c3c2", "#383838"), corner_radius=15)

category9_software_label1 = customtkinter.CTkLabel(master=category9_software_frame1, fg_color=("#c4c3c2", "#383838"), text="7-Zip er et enkelt og greit komprimeringsverktøy som har det meste man trenger til daglig bruk", justify="left", text_font=("Roboto Medium", 15), corner_radius=15)
category9_software_label2 = customtkinter.CTkLabel(master=category9_software_frame2, fg_color=("#c4c3c2", "#383838"), text="PeaZip er et komprimeringsverktøy med et moderne brukergrensesnitt", justify="left", text_font=("Roboto Medium", 15), corner_radius=15)

# ==========Category 10 frame, headline, software frames==========
category10_frame = customtkinter.CTkFrame(master=install_frame, 
                                            fg_color=("#c4c3c2", "#383838"), 
                                            corner_radius=15)
category10_headline_frame = customtkinter.CTkFrame(master=category10_frame, 
                                            fg_color=("#c4c3c2", "#383838"), 
                                            corner_radius=15, 
                                            height=20)
category10_headline_label = customtkinter.CTkLabel(master=category10_headline_frame, 
                                            text="Streaming", 
                                            text_font=("Roboto Medium", 20)) 

category10_software_frame1 = customtkinter.CTkFrame(master=category10_frame, fg_color=("#c4c3c2", "#383838"), corner_radius=15)
category10_software_frame2 = customtkinter.CTkFrame(master=category10_frame, fg_color=("#c4c3c2", "#383838"), corner_radius=15)
category10_software_frame3 = customtkinter.CTkFrame(master=category10_frame, fg_color=("#c4c3c2", "#383838"), corner_radius=15)

category10_software_label1 = customtkinter.CTkLabel(master=category10_software_frame1, fg_color=("#c4c3c2", "#383838"), text="Opptak og strømming", justify="left", text_font=("Roboto Medium", 15), corner_radius=15)
category10_software_label2 = customtkinter.CTkLabel(master=category10_software_frame2, fg_color=("#c4c3c2", "#383838"), text="Shadowplay brukes til opptak og er en del av GeForce Experience\nKan kun brukes sammen med NVIDIA skjermkort.", justify="left", text_font=("Roboto Medium", 15), corner_radius=15)
category10_software_label3 = customtkinter.CTkLabel(master=category10_software_frame3, fg_color=("#c4c3c2", "#383838"), text="Opptak og strømming", justify="left", text_font=("Roboto Medium", 15), corner_radius=15)

# ==========Category 11 frame, headline, software frames==========
category11_frame = customtkinter.CTkFrame(master=install_frame, 
                                            fg_color=("#c4c3c2", "#383838"), 
                                            corner_radius=15)
category11_headline_frame = customtkinter.CTkFrame(master=category11_frame, 
                                            fg_color=("#c4c3c2", "#383838"), 
                                            corner_radius=15, 
                                            height=20)
category11_headline_label = customtkinter.CTkLabel(master=category11_headline_frame, 
                                            text="RGB programvare", 
                                            text_font=("Roboto Medium", 20)) 
category11_frame_left = customtkinter.CTkFrame(master=category11_frame, 
                                            fg_color=("#c4c3c2", "#383838"), 
                                            corner_radius=15)
category11_frame_right = customtkinter.CTkFrame(master=category11_frame, 
                                            fg_color=("#c4c3c2", "#383838"), 
                                            corner_radius=15)

category11_software_frame1 = customtkinter.CTkFrame(master=category11_frame_left, fg_color=("#c4c3c2", "#383838"), corner_radius=15)
category11_software_frame2 = customtkinter.CTkFrame(master=category11_frame_left, fg_color=("#c4c3c2", "#383838"), corner_radius=15)
category11_software_frame3 = customtkinter.CTkFrame(master=category11_frame_left, fg_color=("#c4c3c2", "#383838"), corner_radius=15)
category11_software_frame4 = customtkinter.CTkFrame(master=category11_frame_left, fg_color=("#c4c3c2", "#383838"), corner_radius=15)
category11_software_frame5 = customtkinter.CTkFrame(master=category11_frame_left, fg_color=("#c4c3c2", "#383838"), corner_radius=15)
category11_software_frame6 = customtkinter.CTkFrame(master=category11_frame_right, fg_color=("#c4c3c2", "#383838"), corner_radius=15)
category11_software_frame7 = customtkinter.CTkFrame(master=category11_frame_right, fg_color=("#c4c3c2", "#383838"), corner_radius=15)

category11_software_label1 = customtkinter.CTkLabel(master=category11_software_frame1, fg_color=("#c4c3c2", "#383838"), text="Corsair iCUE styrer RGB for Corsair produkter", justify="left", text_font=("Roboto Medium", 12), corner_radius=15)
category11_software_label2 = customtkinter.CTkLabel(master=category11_software_frame2, fg_color=("#c4c3c2", "#383838"), text="NZXT CAM styrer RGB for NZXT produkter", justify="left", text_font=("Roboto Medium", 12), corner_radius=15)
category11_software_label3 = customtkinter.CTkLabel(master=category11_software_frame3, fg_color=("#c4c3c2", "#383838"), text="MSI Mystic Light styrer RGB for MSI produkter", justify="left", text_font=("Roboto Medium", 12), corner_radius=15)
category11_software_label4 = customtkinter.CTkLabel(master=category11_software_frame4, fg_color=("#c4c3c2", "#383838"), text="ASUS Armoury Crate styrer RGB for ASUS produkter", justify="left", text_font=("Roboto Medium", 12), corner_radius=15)
category11_software_label5 = customtkinter.CTkLabel(master=category11_software_frame5, fg_color=("#c4c3c2", "#383838"), text="GIGABYTE RGB Fusion styrer RGB for GIGABYTE produkter", justify="left", text_font=("Roboto Medium", 12), corner_radius=15)
category11_software_label6 = customtkinter.CTkLabel(master=category11_software_frame6, fg_color=("#c4c3c2", "#383838"), text="L-connect styrer RGB for LIAN LI produkter", justify="left", text_font=("Roboto Medium", 12), corner_radius=15)
category11_software_label7 = customtkinter.CTkLabel(master=category11_software_frame7, fg_color=("#c4c3c2", "#383838"), text="OpenRGB er utviklet for å ha et samlet program\nsom kan styre alt av RGB på PC-en", justify="left", text_font=("Roboto Medium", 12), corner_radius=15)

# ==========Category 12 frame, headline, software frames==========
category12_frame = customtkinter.CTkFrame(master=install_frame, 
                                            fg_color=("#c4c3c2", "#383838"), 
                                            corner_radius=15)
category12_headline_frame = customtkinter.CTkFrame(master=category12_frame, 
                                            fg_color=("#c4c3c2", "#383838"), 
                                            corner_radius=15, 
                                            height=20)
category12_headline_label = customtkinter.CTkLabel(master=category12_headline_frame, 
                                            text="Drivere", 
                                            text_font=("Roboto Medium", 20))

category12_frame_left = customtkinter.CTkFrame(master=category12_frame, 
                                            fg_color=("#c4c3c2", "#383838"), 
                                            corner_radius=15)
category12_frame_right = customtkinter.CTkFrame(master=category12_frame, 
                                            fg_color=("#c4c3c2", "#383838"), 
                                            corner_radius=15)

category12_software_frame1 = customtkinter.CTkFrame(master=category12_frame_left, fg_color=("#c4c3c2", "#383838"), corner_radius=15)
category12_software_frame2 = customtkinter.CTkFrame(master=category12_frame_left, fg_color=("#c4c3c2", "#383838"), corner_radius=15)
category12_software_frame3 = customtkinter.CTkFrame(master=category12_frame_left, fg_color=("#c4c3c2", "#383838"), corner_radius=15)
category12_software_frame4 = customtkinter.CTkFrame(master=category12_frame_left, fg_color=("#c4c3c2", "#383838"), corner_radius=15)
category12_software_frame5 = customtkinter.CTkFrame(master=category12_frame_left, fg_color=("#c4c3c2", "#383838"), corner_radius=15)
category12_software_frame6 = customtkinter.CTkFrame(master=category12_frame_right, fg_color=("#c4c3c2", "#383838"), corner_radius=15)
category12_software_frame7 = customtkinter.CTkFrame(master=category12_frame_right, fg_color=("#c4c3c2", "#383838"), corner_radius=15)


category12_software_label1 = customtkinter.CTkLabel(master=category12_software_frame1, fg_color=("#c4c3c2", "#383838"), text="Installerer drivere til diverse intel produkter", justify="left", text_font=("Roboto Medium", 11), corner_radius=15)
category12_software_label2 = customtkinter.CTkLabel(master=category12_software_frame2, fg_color=("#c4c3c2", "#383838"), text="Laster ned og installerer nyeste NVIDIA drivere.\nMan kan skreddersy driveren til å\nkun inkludere komponentene man ønsker.", justify="left", text_font=("Roboto Medium", 12), corner_radius=15)
category12_software_label3 = customtkinter.CTkLabel(master=category12_software_frame3, fg_color=("#c4c3c2", "#383838"), text="Lenovo System Update installerer drivere til Lenovo maskiner", justify="left", text_font=("Roboto Medium", 11), corner_radius=15)
category12_software_label4 = customtkinter.CTkLabel(master=category12_software_frame4, fg_color=("#c4c3c2", "#383838"), text="GeForce Experience har flere funksjoner.\nbla. videoopptak, driver oppdatering,\noptimalisering av spill osv.", justify="left", text_font=("Roboto Medium", 12), corner_radius=15)
category12_software_label5 = customtkinter.CTkLabel(master=category12_software_frame5, fg_color=("#c4c3c2", "#383838"), text="Oppdager og installerer drivere til brikkesett og skjermkort.", justify="left", text_font=("Roboto Medium", 11), corner_radius=15)
category12_software_label6 = customtkinter.CTkLabel(master=category12_software_frame6, fg_color=("#c4c3c2", "#383838"), text="ASUS Armoury Crate installerer drivere til utvalgte\nASUS maskiner og hovedkort.", justify="left", text_font=("Roboto Medium", 12), corner_radius=15)
category12_software_label7 = customtkinter.CTkLabel(master=category12_software_frame7, fg_color=("#c4c3c2", "#383838"), text="Gigabyte App Center installerer drivere til\nGigabyte hovedkort", justify="left", text_font=("Roboto Medium", 11), corner_radius=15)

# ==========Sofware Buttons==========

# Browsers buttons
firefox_check = customtkinter.CTkButton(category1_software_frame1, fg_color="#0b57c2", hover_color="#F5681C", text ="Firefox", text_font=("Roboto Medium", 20), image=firefox_image, command=lambda:toggle_browser_software(1))
chrome_check = customtkinter.CTkButton(category1_software_frame2, fg_color="#0b57c2", hover_color="#F5681C", text ="Chrome", text_font=("Roboto Medium", 20), image=chrome_image, command=lambda:toggle_browser_software(2))
brave_check = customtkinter.CTkButton(category1_software_frame3, fg_color="#0b57c2", hover_color="#F5681C", text ="Brave", text_font=("Roboto Medium", 20), image=brave_image, command=lambda:toggle_browser_software(3))
vivaldi_check = customtkinter.CTkButton(category1_software_frame4, fg_color="#0b57c2", hover_color="#F5681C", text ="Vivaldi", text_font=("Roboto Medium", 20), image=vivaldi_image, command=lambda:toggle_browser_software(4))
# Email Clients buttons
emclient_check = customtkinter.CTkButton(category2_software_frame1, fg_color="#0b57c2", hover_color="#F5681C", text ="EM Client", text_font=("Roboto Medium", 20), image=emclient_image, command=lambda:toggle_email_software(1))
thunderbird_check = customtkinter.CTkButton(category2_software_frame2, fg_color="#0b57c2", hover_color="#F5681C", text ="Thunderbird", text_font=("Roboto Medium", 20), image=thunderbird_image, command=lambda:toggle_email_software(2))
# Document management buttons
libre_office_check = customtkinter.CTkButton(category3_software_frame1, fg_color="#0b57c2", hover_color="#F5681C", text ="Libre Office", text_font=("Roboto Medium", 20), image=libre_office_image, command=lambda:toggle_document_software(1))
open_office_check = customtkinter.CTkButton(category3_software_frame2, fg_color="#0b57c2", hover_color="#F5681C", text ="Open Office", text_font=("Roboto Medium", 20), image=open_office_image, command=lambda:toggle_document_software(2))
evernote_check = customtkinter.CTkButton(category3_software_frame3, fg_color="#0b57c2", hover_color="#F5681C", text ="Evernote", text_font=("Roboto Medium", 20), image=evernote_image, command=lambda:toggle_document_software(3))
onenote_check = customtkinter.CTkButton(category3_software_frame4, fg_color="#0b57c2", hover_color="#F5681C", text ="OneNote", text_font=("Roboto Medium", 20), image=onenote_image, command=lambda:toggle_document_software(4))
adobe_reader_check = customtkinter.CTkButton(category3_software_frame5, fg_color="#0b57c2", hover_color="#F5681C", text ="Adobe Reader", text_font=("Roboto Medium", 20), image=adobe_reader_image, command=lambda:toggle_document_software(5))
# Media
vlc_check = customtkinter.CTkButton(category4_software_frame1, fg_color="#0b57c2", hover_color="#F5681C", text ="VLC", text_font=("Roboto Medium", 20), image=vlc_image, command=lambda:toggle_media_software(1))
spotify_check = customtkinter.CTkButton(category4_software_frame2, fg_color="#0b57c2", hover_color="#F5681C", text ="Spotify", text_font=("Roboto Medium", 20), image=spotify_image, command=lambda:toggle_media_software(2))
itunes_check = customtkinter.CTkButton(category4_software_frame3, fg_color="#0b57c2", hover_color="#F5681C", text ="iTunes", text_font=("Roboto Medium", 20), image=itunes_image, command=lambda:toggle_media_software(3))
tidal_check = customtkinter.CTkButton(category4_software_frame4, fg_color="#0b57c2", hover_color="#F5681C", text ="Tidal", text_font=("Roboto Medium", 20), image=tidal_image, command=lambda:toggle_media_software(4))
k_lite_codec_pack_check = customtkinter.CTkButton(category4_software_frame5, fg_color="#0b57c2", hover_color="#F5681C", text ="K-Lite Codec Pack", text_font=("Roboto Medium", 20), image=k_lite_codec_pack_image, command=lambda:toggle_media_software(5))
# Games
steam_check = customtkinter.CTkButton(category5_software_frame1, fg_color="#0b57c2", hover_color="#F5681C", text ="Steam", text_font=("Roboto Medium", 20), image=steam_image, command=lambda:toggle_game_software(1))
epic_check = customtkinter.CTkButton(category5_software_frame2, fg_color="#0b57c2", hover_color="#F5681C", text ="Epic Games", text_font=("Roboto Medium", 20), image=epic_games_image, command=lambda:toggle_game_software(2))
gog_check = customtkinter.CTkButton(category5_software_frame3, fg_color="#0b57c2", hover_color="#F5681C", text ="GOG Galaxy", text_font=("Roboto Medium", 20), image=gog_image, command=lambda:toggle_game_software(3))
ubisoft_check = customtkinter.CTkButton(category5_software_frame4, fg_color="#0b57c2", hover_color="#F5681C", text ="Ubisoft Connect", text_font=("Roboto Medium", 20), image=ubisoft_image, command=lambda:toggle_game_software(4))
origin_check = customtkinter.CTkButton(category5_software_frame5, fg_color="#0b57c2", hover_color="#F5681C", text ="Origin", text_font=("Roboto Medium", 20), image=origin_image, command=lambda:toggle_game_software(5))
#Images
gimp_check = customtkinter.CTkButton(category6_software_frame1, fg_color="#0b57c2", hover_color="#F5681C", text ="Gimp", text_font=("Roboto Medium", 20), image=gimp_image, command=lambda:toggle_photo_software(1))
irfanview_check = customtkinter.CTkButton(category6_software_frame2, fg_color="#0b57c2", hover_color="#F5681C", text ="Irfanview", text_font=("Roboto Medium", 20), image=irfanview_image, command=lambda:toggle_photo_software(2))
greenshot_check = customtkinter.CTkButton(category6_software_frame3, fg_color="#0b57c2", hover_color="#F5681C", text ="Greenshot", text_font=("Roboto Medium", 20), image=greenshot_image, command=lambda:toggle_photo_software(3))
#Cloud storage
onedrive_check = customtkinter.CTkButton(category7_software_frame1, fg_color="#0b57c2", hover_color="#F5681C", text ="Onedrive", text_font=("Roboto Medium", 20), image=onedrive_image, command=lambda:toggle_cloud_software(1))
dropbox_check = customtkinter.CTkButton(category7_software_frame2, fg_color="#0b57c2", hover_color="#F5681C", text ="Dropbox", text_font=("Roboto Medium", 20), image=dropbox_image, command=lambda:toggle_cloud_software(2))
google_drive_check = customtkinter.CTkButton(category7_software_frame3, fg_color="#0b57c2", hover_color="#F5681C", text ="Google Drive", text_font=("Roboto Medium", 20), image=google_drive_image, command=lambda:toggle_cloud_software(3))
#Communication
discord_check = customtkinter.CTkButton(category8_software_frame1, fg_color="#0b57c2", hover_color="#F5681C", text ="Discord", text_font=("Roboto Medium", 20), image=discord_image, command=lambda:toggle_communication_software(1))
skype_check = customtkinter.CTkButton(category8_software_frame2, fg_color="#0b57c2", hover_color="#F5681C", text ="Skype", text_font=("Roboto Medium", 20), image=skype_image, command=lambda:toggle_communication_software(2))
zoom_check = customtkinter.CTkButton(category8_software_frame3, fg_color="#0b57c2", hover_color="#F5681C", text ="Zoom", text_font=("Roboto Medium", 20), image=zoom_image, command=lambda:toggle_communication_software(3))
teamviewer_check = customtkinter.CTkButton(category8_software_frame4, fg_color="#0b57c2", hover_color="#F5681C", text ="Teamwiever", text_font=("Roboto Medium", 20), image=teamviewer_image, command=lambda:toggle_communication_software(4))
#Compression
seven_zip_check = customtkinter.CTkButton(category9_software_frame1, fg_color="#0b57c2", hover_color="#F5681C", text ="7 Zip", text_font=("Roboto Medium", 20), image=seven_zip_image, command=lambda:toggle_compression_software(1))
peazip_check = customtkinter.CTkButton(category9_software_frame2, fg_color="#0b57c2", hover_color="#F5681C", text ="PeaZip", text_font=("Roboto Medium", 20), image=peazip_image, command=lambda:toggle_compression_software(2))
#Streaming
obs_check = customtkinter.CTkButton(category10_software_frame1, fg_color="#0b57c2", hover_color="#F5681C", text ="OBS", text_font=("Roboto Medium", 20), image=obs_image, command=lambda:toggle_streaming_software(1))
shadowplay_check = customtkinter.CTkButton(category10_software_frame2, fg_color="#0b57c2", hover_color="#F5681C", text ="Shadowplay", text_font=("Roboto Medium", 20), image=geforce_experience_image, command=lambda:toggle_streaming_software(2))
elgato_check = customtkinter.CTkButton(category10_software_frame3, fg_color="#0b57c2", hover_color="#F5681C", text ="Elgato Game Capture", text_font=("Roboto Medium", 20), image=elgato_image, command=lambda:toggle_streaming_software(3))
#RGB
icue_check = customtkinter.CTkButton(category11_software_frame1, fg_color="#0b57c2", hover_color="#F5681C", text ="Corsair Icue", text_font=("Roboto Medium", 15), image=icue_image, command=lambda:toggle_rgb_software(1))
nzxt_check = customtkinter.CTkButton(category11_software_frame2, fg_color="#0b57c2", hover_color="#F5681C", text ="NZXT CAM", text_font=("Roboto Medium", 15), image=nzxt_image, command=lambda:toggle_rgb_software(2))
msi_check = customtkinter.CTkButton(category11_software_frame3, fg_color="#0b57c2", hover_color="#F5681C", text ="MSI Mystic Light", text_font=("Roboto Medium", 15), image=msi_image, command=lambda:toggle_rgb_software(3))
asus_check = customtkinter.CTkButton(category11_software_frame4, fg_color="#0b57c2", hover_color="#F5681C", text ="Armoury Crate", text_font=("Roboto Medium", 15), image=asus_armourycrate_image, command=lambda:toggle_rgb_software(4))
gigabyte_check = customtkinter.CTkButton(category11_software_frame5, fg_color="#0b57c2", hover_color="#F5681C", text ="Gigabyte Fusion", text_font=("Roboto Medium", 15), image=gigabyte_image, command=lambda:toggle_rgb_software(5))
lianli_check = customtkinter.CTkButton(category11_software_frame6, fg_color="#0b57c2", hover_color="#F5681C", text ="L-Connect", text_font=("Roboto Medium", 15), image=lianli_image, command=lambda:toggle_rgb_software(6))
openrgb_check = customtkinter.CTkButton(category11_software_frame7, fg_color="#0b57c2", hover_color="#F5681C", text ="OpenRGB", text_font=("Roboto Medium", 15), image=openrgb_image, command=lambda:toggle_rgb_software(7))
#Drivers
intel_check = customtkinter.CTkButton(category12_software_frame1, fg_color="#0b57c2", hover_color="#F5681C", text ="Intel D&U", text_font=("Roboto Medium", 13), image=intel_image, command=lambda:toggle_driver_software(1))
nv_cleaninstall_check = customtkinter.CTkButton(category12_software_frame2, fg_color="#0b57c2", hover_color="#F5681C", text ="NV Clean install", text_font=("Roboto Medium", 13), image=nv_cleaninstall_image, command=lambda:toggle_driver_software(2))
lenovo_check = customtkinter.CTkButton(category12_software_frame3, fg_color="#0b57c2", hover_color="#F5681C", text ="Lenovo SU", text_font=("Roboto Medium", 15), image=lenovo_image, command=lambda:toggle_driver_software(3))
geforce_experience_check = customtkinter.CTkButton(category12_software_frame4, fg_color="#0b57c2", hover_color="#F5681C", text ="Geforce Experience", text_font=("Roboto Medium", 13), image=geforce_experience_image, command=lambda:toggle_driver_software(4))
amd_check = customtkinter.CTkButton(category12_software_frame5, fg_color="#0b57c2", hover_color="#F5681C", text ="AMD Auto Detect", text_font=("Roboto Medium", 13), image=amd_image, command=lambda:toggle_driver_software(5))
asus_ac_check = customtkinter.CTkButton(category12_software_frame6, fg_color="#0b57c2", hover_color="#F5681C", text ="Armoury Crate", text_font=("Roboto Medium", 13), image=asus_armourycrate_image, command=lambda:toggle_driver_software(6))
gigabyte_app_center_check = customtkinter.CTkButton(category12_software_frame7, fg_color="#0b57c2", hover_color="#F5681C", text ="Gigabyte App Center", text_font=("Roboto Medium", 13), image=gigabyte_app_image, command=lambda:toggle_driver_software(7))



# EMPLOYEE VERSION. DELETE FOR CUSTOMER VERSION
def standardpakke(args):
    global software_list
    cmd_ansatt = "cmd /k winget install Mozilla.Firefox -e && winget install VideoLAN.VLC -e && winget install Unchecky.Unchecky -e && winget install Adobe.Acrobat.Reader.64-bit -e && winget install Teamviewer.Teamviewer -e && "
    if args == 1:
        if cmd_ansatt in software_list:
            software_list = "cmd /k "
            unpack_chosen_labels()
        else:
            software_list = cmd_ansatt
            for chosen_ansatt_label in (chosen_firefox_label, chosen_vlc_label, chosen_adobe_reader_label, chosen_unchecky_label, chosen_teamviewer_label):
                chosen_ansatt_label.pack(side="left")
    else:
        pass

ansatt_frame = customtkinter.CTkFrame(standardpakke_frame, fg_color=("#c4c3c2", "#383838"))
ansatt_label= customtkinter.CTkLabel(ansatt_frame, fg_color=("#c4c3c2", "#383838"), text="Standardpakke Ansatt versjon", text_font=("Roboto Medium", 20))
ansatt_button = customtkinter.CTkButton(ansatt_frame, fg_color=("#d1d0cf", "#292929"), hover_color="#F5681C", text="Standardpakke", text_font=("Roboto Medium", 20), image=logo_image, command=lambda:standardpakke(1))



# ==========Left frame buttons. Packing and unpacking widgets==========
# ==========PACK/TOGGLE HOME PAGE==========
def clicked_home():
    global software_list
    global cmd_ansatt
    print("Clicked home")
    software_list = "cmd /k "
    cmd_ansatt = "cmd /k "
    unpack_chosen_labels()
    for frame in (install_frame, support_frame, install_bottom_frame, chosen_software_main_frame, ansatt_frame):
        frame.pack_forget()


    home_frame.pack(pady=5, padx=5, fill="both", expand=True)
    #home_headline_frame.pack(pady=5, padx=5, fill="x")
    home_headline_label.pack()

# ==========PACK/TOGGLE INSTALL PAGE==========
def clicked_install_software():
    global software_list
    global cmd_ansatt
    print("Clicked install software")
    software_list = "cmd /k "
    cmd_ansatt = "cmd /k "
    unpack_chosen_labels()
    thread2 = threading.Thread(target=compile_selected, args=(1, ))
    thread2.start()
    print(threading.active_count())
    print(threading.enumerate())

    for frame in (category1_frame, category2_frame, category3_frame, category4_frame, category5_frame, category6_frame, 
    category7_frame, category8_frame, category9_frame, category10_frame, category11_frame, category12_frame, 
    home_frame, support_frame):
        frame.pack_forget()

    install_frame.pack(padx=5, fill="both", expand=True)
    install_headline_frame.pack(pady=5, padx=5, ipady=3, fill="x")
    install_headline_label.pack()
    standardpakke_frame.pack(pady=5, padx=5, fill="both", expand=True)
    standardpakke_label.pack(pady=5, padx=5, fill="both")
    software_tabs_frame1.pack(ipadx=5, fill="x")
    software_tabs_frame2.pack(ipadx=5, fill="x")
    software_tabs1_filler_left.pack(side="left", expand=True)
    software_tabs1_filler_right.pack(side="right", expand=True)
    software_tabs2_filler_left.pack(side="left", expand=True)
    software_tabs2_filler_right.pack(side="right", expand=True)

    ansatt_frame.pack(side = "bottom", padx=5, pady=5, fill="x", expand=True)
    ansatt_label.pack(side="top")
    ansatt_button.pack()

    for button in (category1_tab, category2_tab, category3_tab, category4_tab, category5_tab, category6_tab, 
    category7_tab, category8_tab, category9_tab, category10_tab, category11_tab, category12_tab):
        button.pack(padx=2, pady=2, side="left")


    # ==========Packs the bottom frame with install, update and uninstall buttons==========
    install_bottom_frame.pack(pady=5, padx=5, fill="y", expand=False, side="left")
    install_selected_button.pack(pady=5, padx=5, side="top")
    update_selected_button.pack(pady=5, padx=5, side="top")
    uninstall_selected_button.pack(pady=5, padx=5, side="bottom")

    chosen_software_main_frame.pack(pady=5, padx=5, fill="both", side="right", expand=True)

# ==========PACK/TOGGLE SUPPORT PAGE==========
def clicked_support():
    global software_list
    global cmd_ansatt
    print("Clicked support")
    software_list = "cmd /k "
    cmd_ansatt = "cmd /k "
    unpack_chosen_labels()
    for frame in (home_frame, install_frame, install_bottom_frame, chosen_software_main_frame, ansatt_frame):
        frame.pack_forget()

    support_frame.pack(pady=5, padx=5, fill="both", expand=True)
    support_headline_label.pack(side="top")
    support_teamviewer_frame.pack(pady=5, padx=5, fill="both", side="bottom", expand=True)
    teamviewer_support_icon.pack(pady=5, padx=5)
    support_bottom_label.pack(pady=5, padx=5, expand=True, fill="both", side="bottom")
    support_top_label.pack(pady=5, padx=5, fill="both", side="bottom")
    support_headline_frame.pack(pady=5, padx=5, fill="both")
    support_frame2.pack(pady=5, padx=5, fill="both")

    

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
