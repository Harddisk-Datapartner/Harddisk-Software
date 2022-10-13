from PIL import Image, ImageTk
import customtkinter
x = 1

# ==========Create Images==========
image_size = 55

logo_image = ImageTk.PhotoImage(Image.open("Logos\\HDDLOGO.ico").resize((90, 90)))
headline_image = ImageTk.PhotoImage(Image.open("Logos\\Fulltextlogo.png").resize((400, 55)))
home_image = ImageTk.PhotoImage(Image.open("Logos\\Menu icons\\Home.png").resize((image_size, image_size)))
install_software_image = ImageTk.PhotoImage(Image.open("Logos\\Menu icons\\Download.png").resize((image_size, image_size)))
support_image = ImageTk.PhotoImage(Image.open("Logos\\Menu icons\\Support.png").resize((image_size, image_size)))




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
