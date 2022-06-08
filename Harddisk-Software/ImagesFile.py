from PIL import Image, ImageTk
import customtkinter


imagesroot = customtkinter.CTk()
# ==========Create Images==========
image_size = 55

logo_image = ImageTk.PhotoImage(Image.open("Logos\Menu icons\HDDLOGO.png").resize((90, 70)))
headline_image = ImageTk.PhotoImage(Image.open("Logos\Fulltextlogo.png").resize((400, 55)))
home_image = ImageTk.PhotoImage(Image.open("Logos\\Menu icons\\Home.png").resize((image_size, image_size)))
install_software_image = ImageTk.PhotoImage(Image.open("Logos\Menu icons\Download.png").resize((image_size, image_size)))
support_image = ImageTk.PhotoImage(Image.open("Logos\Menu icons\Support.png").resize((image_size, image_size)))

# ==========Software Images==========

# Browsers/Nettlesere
"""firefox_image = ImageTk.PhotoImage(Image.open("Logos\\128x128\\Firefox 128x128.png").resize((image_size, image_size)))
chrome_image = ImageTk.PhotoImage(Image.open("Logos\\128x128\\Chrome 128x128.png").resize((image_size, image_size)))
Brave_image = ImageTk.PhotoImage(Image.open("Logos\\128x128\\Brave 128x128.png").resize((image_size, image_size)))
vivaldi_image = ImageTk.PhotoImage(Image.open("Logos\\128x128\\Vivaldi 128x128.png").resize((image_size, image_size)))
duckduckgo_image = ImageTk.PhotoImage(Image.open("Logos\\128x128\\DuckDuckGo 128x128.png").resize((image_size, image_size)))

# Email Clients/Epost klienter
emclient_image = ImageTk.PhotoImage(Image.open("Logos\\128x128\\EM Client 128x128.png").resize((image_size, image_size)))
thunderbird_image = ImageTk.PhotoImage(Image.open("Logos\\128x128\\Thunderbird 128x128.png").resize((image_size, image_size)))

# Document management/Dokumentbehandling
adobe_reader_image = 
libreoffice_image = ImageTk.PhotoImage(Image.open("Logos\\128x128\\Libreoffice 128x128.png").resize((image_size, image_size)))
openoffice_image = ImageTk.PhotoImage(Image.open("Logos\\128x128\\Open Office 128x128.png").resize((image_size, image_size)))
evernote_image = ImageTk.PhotoImage(Image.open("Logos\\128x128\\Evernote 128x128.png").resize((image_size, image_size)))
onenote_image = ImageTk.PhotoImage(Image.open("Logos\\128x128\\OneNote 128x128.png").resize((image_size, image_size)))

# Media
vlc_image = ImageTk.PhotoImage(Image.open("Logos\\128x128\\VLC 128x128.png").resize((image_size, image_size)))
spotify_image = ImageTk.PhotoImage(Image.open("Logos\\128x128\\Spotify 128x128.png").resize((image_size, image_size)))
itunes_image = ImageTk.PhotoImage(Image.open("Logos\\128x128\\Itunes 128x128.png").resize((image_size, image_size)))
tidal_image = ImageTk.PhotoImage(Image.open("Logos\\128x128\\Tidal 128x128.png").resize((image_size, image_size)))
k_lite_codec = ImageTk.PhotoImage(Image.open("Logos\\128x128\\K-Kite Codec 128x128.png").resize((image_size, image_size)))

#Photo editing/Bilderedigering
gimp_image = ImageTk.PhotoImage(Image.open("Logos\\128x128\\Gimp 128x128.png").resize((image_size, image_size)))
irfanview_image = 
greenshot_image = ImageTk.PhotoImage(Image.open("Logos\\128x128\\Greenshot 128x128.png").resize((image_size, image_size)))

#Games/Spill
steam_image = ImageTk.PhotoImage(Image.open("Logos\\128x128\\Steam 128x128.png").resize((image_size, image_size)))
epic_games_image = 
gog_image =
origin_image= 
blizz_image = 
ubisoft_image = 

# Compression/Komprimering
peazip_image = ImageTk.PhotoImage(Image.open("Logos\\128x128\\Peazip 128x128.png").resize((image_size, image_size)))
sevenzip_image = ImageTk.PhotoImage(Image.open("Logos\\128x128\\7zip 128x128.png").resize((image_size, image_size)))

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
intel_ds_image = ImageTk.PhotoImage(Image.open("Logos\\128x128\\IntelD&SA 128x128.png").resize((image_size, image_size)))
amd_image = ImageTk.PhotoImage(Image.open("Logos\\128x128\\AMD 128x128.png").resize((image_size, image_size)))
nv_ci_image = ImageTk.PhotoImage(Image.open("Logos\\128x128\\NV Cleaninstall 128x128.png").resize((image_size, image_size)))
nvidia_ge_image = ImageTk.PhotoImage(Image.open("Logos\\128x128\\Geforce Experience 128x128.png").resize((image_size, image_size)))
asus_ac_image = ImageTk.PhotoImage(Image.open("Logos\\128x128\\Armoury Crate 128x128.png").resize((image_size, image_size)))
gigabyte_app_image = ImageTk.PhotoImage(Image.open("Logos\\128x128\\Gigabyte App 128x128.png").resize((image_size, image_size)))
lenovo_su_image = ImageTk.PhotoImage(Image.open("Logos\\128x128\\LenovoSU 128x128.png").resize((image_size, image_size)))
"""