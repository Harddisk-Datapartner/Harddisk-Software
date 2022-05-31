import tkinter as tk
import sv_ttk

root = tk.Tk()

sv_ttk.set_theme("light")  # Set light theme
sv_ttk.set_theme("dark")  # Set dark theme

sv_ttk.use_light_theme()  # Set light theme
sv_ttk.use_dark_theme()  # Set dark theme

sv_ttk.toggle_theme()  # Toggle between dark and light theme

print(sv_ttk.get_theme())  # Get what theme the app uses (either 'light' or 'dark')

root.mainloop()




"""vlc_image = ImageTk.PhotoImage(Image.open("Logos\\128x128\\VLC 128x128.png").resize((200, 200)))



check1 = sv_ttk.Checkbutton(root, width=20, image=vlc_image)
check1.pack()
"""




"""class SoftwareButton:
    def __init__(self, name, image, execute):
        self.name = name
        self.image = image
        self.execute = execute"""

        
