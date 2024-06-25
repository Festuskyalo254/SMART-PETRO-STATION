import tkinter
from tkinter import messagebox
from PIL import ImageTk,Image
import mysql



window = tkinter.Tk()
window.title("Start Menu")
window.geometry('1000x600')
window.resizable(False,False)

#Background image
image_0 = Image.open("C:\\Users\\user\\Desktop\\Automated Petro Station\\Final\\images\\Gas.jpg")
bg = ImageTk.PhotoImage(image_0)
lbl=tkinter.Label(window,image = bg)
lbl.place(x = 0,y = 0,relheight=1,relwidth=1)

def login():
    messagebox.showinfo("Welcome","Welcome To My System")
    window.destroy()
    import Login

def self_service():
    messagebox.showinfo("Welcome", "Welcome To My System")
    window.destroy()
    import Mpesa_Transaction


# Button
log_in = tkinter.Button(text="ATTENDEE", bd=0, cursor="hand2", font=("Goudy old style", 20, "bold"), fg="#6162FF",bg="black", command = login)
log_in.place(x=350, y=150, width=200, height=40)

self = tkinter.Button(text="SELF SERVICE", bd=0, cursor="hand2", font=("Goudy old style", 20, "bold"), fg="#6162FF",bg="black", command = self_service)
self.place(x=350, y=250, width=200, height=40)


window.mainloop()