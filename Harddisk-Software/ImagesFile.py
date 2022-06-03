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
chrome_image =
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
vlc_image = ImageTk.PhotoImage(Image.open("Logos\\128x128\\VLC 128x128.png").resize((image_size, image_size)))
spotify_image = ImageTk.PhotoImage(Image.open("Logos\\128x128\\Spotify 128x128.png").resize((image_size, image_size)))
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
