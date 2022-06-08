import tkinter as tk
from tkinter import ttk
import sv_ttk

root = tk.Tk()
"""style= ttk.Style(root)
root.tk.call("source", "sun-valley.tcl")"""



sv_ttk.set_theme("dark")  # Set dark theme
sv_ttk.use_dark_theme()  # Set dark theme

install_notebook = ttk.Notebook(root)
install_notebook.pack()
frame1 = ttk.Notebook(install_notebook)
frame1.pack()
frame2 = ttk.Notebook(install_notebook)
frame2.pack()
frame3 = ttk.Notebook(install_notebook)
frame3.pack()

install_notebook.add(frame1, text="Nettleser")
install_notebook.add(frame2, text="Media")
install_notebook.add(frame3, text="Fjernstyring")

root.mainloop()











"""from tkinter import *
import tkinter
import sv_ttk

root = tkinter.Tk()
root.tk.call("source", "sun-valley.tcl")

sv_ttk.set_theme("dark")  # Set dark theme
sv_ttk.use_dark_theme()  # Set dark theme

sv_ttk.toggle_theme()  # Toggle between dark and light theme

print(sv_ttk.get_theme())  # Get what theme the app uses (either 'light' or 'dark')

root.mainloop()

"""


"""vlc_image = ImageTk.PhotoImage(Image.open("Logos\\128x128\\VLC 128x128.png").resize((200, 200)))



check1 = sv_ttk.Checkbutton(root, width=20, image=vlc_image)
check1.pack()
"""




"""class SoftwareButton:
    def __init__(self, name, image, execute):
        self.name = name
        self.image = image
        self.execute = execute"""

        
