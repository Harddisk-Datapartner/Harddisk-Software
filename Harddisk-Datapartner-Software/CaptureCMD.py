import tkinter
import customtkinter
import subprocess
import threading


root = customtkinter.CTk()
bg_frame = customtkinter.CTkFrame(master = root, fg_color="gray")
bg_frame.pack(fill="both", expand=True)

frame1 = customtkinter.CTkFrame(master = bg_frame, fg_color="blue")
frame2 = customtkinter.CTkFrame(master = bg_frame, fg_color="green")
frame1.pack(fill="x", expand=True)
frame2.pack(fill="x", expand=True)

def ping(args):
    if args == 1:
        result = subprocess.check_output("ping google.com")
        result.decode("UTF-8")
        for _ in range(5):
            root.after(1000)
            print(result)


"""def ping(args):
    if args == 1:
        output = subprocess.Popen("ping google.com")
"""
    

"""def ping():
    global line
    with open("output2.txt", "r", encoding=("UTF-8")) as f:
        for line in f:
            print(line)
            test_label.after(1000)
            test_label.configure(text=line)"""

"""def update_label(disp, test_label):
    global line
    test_label.configure(text=disp)"""

"""output = None
def ping(args):
    global f
    global output
    if args == 1:
        f = subprocess.Popen("ping google.com -t")
        print (f)
    if args == 2:
        #print(proc.stdout.read())
        print(f)"""

#test_label = customtkinter.CTkLabel(master=frame2, fg_color="blue", text=f)
#test_label.pack()

button1 = customtkinter.CTkButton(master=frame1, text="One", command=lambda:ping(1))
button1.pack()
button2 = customtkinter.CTkButton(master=frame1, text="Two", command=lambda:ping(2))
button2.pack()

thread2 = threading.Thread(target=ping, args=(1, ))
thread2.start()
print(threading.active_count())
print(threading.enumerate())





"""x = threading.Thread(target=ping, args=(1, )).start
print(threading.active_count())
print(threading.enumerate())"""





"""def ping(args):
    if args == 1:
        with open("output2.txt", "a+", encoding="UTF-8") as f:
            f = subprocess.Popen("ping google.com && ping facebook.com", stdout=f, text=True, shell=True)
            with open("output2.txt", "r", encoding="UTF-8") as f:
                lines=f.readlines()
                test_label = customtkinter.CTkLabel(master=frame2, fg_color="blue", text=lines)
                test_label.pack()
            for line in f:
                count += 1
    if args == 2:
        print(f.readlines)"""

"""def change(args, testvar):
    if args == 1:
        testvar = "hei"
        return testvar

    if args == 2:
        test_label.text = "It worked again!"
        test_label.update"""
"""ping_button = customtkinter.CTkButton(master=frame1, text="Ping", command=lambda:ping(1))
ping_button.pack()"""

"""frame2_label = customtkinter.CTkLabel(master = frame2, text="")
frame2_label.pack()"""

"""def ping(args):
    global p1
    if args == 1:
        p1 = subprocess.check_output("wmic baseboard get product")
        #p1= p1.decode("utf-8")
    if args == 2:
        test_label = customtkinter.CTkLabel(master=frame2, fg_color="blue", text=p1)
        test_label.pack()
"""

#lines=output2.txt.readlines()
#for line in lines:


root.mainloop()