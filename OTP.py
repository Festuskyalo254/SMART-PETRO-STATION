import random
import tkinter
from tkinter import *
from PIL import ImageTk,Image
from twilio.rest import Client
from tkinter import messagebox

window = tkinter.Tk()
window.geometry("1000x600")
window.title("OTP Verification")
window.resizable(False, False)
n = random.randint(1000,9999)


#Background image
image_0 = Image.open("C:\\Users\\user\\Desktop\\Automated Petro Station\\Final\\images\\Gas.jpg")
bg = ImageTk.PhotoImage(image_0)
lbl=tkinter.Label(window,image = bg)
lbl.place(x = 0,y = 0,relheight=1,relwidth=1)

# Label
OTP_no = Label(text = "OTP Verification Number",bd = 0,font = ("Goudy old style",20,"bold"),fg = "#6162FF", bg = "black")
OTP_no.place(x = 210,y = 170)


#Entry OTP
def otp_enter(e):
    OTP_number.delete(0,'end')
def otp_leave(e):
    if OTP_number.get()=='':
       OTP_number.insert(0,'Username')
OTP_number = tkinter.Entry(font = ("Goudy old style",15,), bg = "#E7E6E6")
OTP_number.insert(0,"OTP NUMBER")
OTP_number.bind("<FocusIn>",otp_enter)
OTP_number.bind("<FocusOut>",otp_leave)
OTP_number.place(x = 210,y = 210)

#Your Twilio phone number,Twilio Account SID and Auth Token
twilio_phone_number = +15076906258
account_sid = "AC573e2a54a489cec3b6ddff73f776d66a"
auth_token = "9322852968912f5cb9ae7400c5de81be"
client = Client(account_sid, auth_token)

def generate_otp():
    digits = "0123456789"
    OTP = ""
    for i in range(6):
        OTP += digits[random.randint(0,9)]
    return OTP

otp = generate_otp()

#Send OTP via SMS using Twilio
def resendOTP():
    client.messages.create(
         body  = 'Your OTP is ' + otp,
         from_ = "++15074971082",
         to    = "+254795282648")


def checkOTP():
    userInput = OTP_number.get()
    if userInput == otp:
       messagebox.showinfo("showinfo", "Verification Success")
       window.destroy()
       import Login
    else:
       messagebox.showwarning("showinfo", "wrong OTP")


def back():
    window.destroy()
    import Login

#Button
sendOTP = Button(text ="SEND OTP",bd = 0,cursor = "hand2",font = ("Goudy old style",20,"bold"),fg = "Green", bg = "black",command = resendOTP)
sendOTP.place(x = 210, y = 300)

submitButtonImage = PhotoImage (file = "submit.png")
submitButton = Button(image = submitButtonImage,border = 0,command = checkOTP)
submitButton.place(x = 400, y = 400)

resendOTPImage = PhotoImage(file = "resendotp.png")
resend = Button(image = resendOTPImage,border = 0,command = resendOTP)
resend.place(x = 210, y = 400)

bck = tkinter.Button(cursor ="hand2", text ="BACK", bd = 0, font = ("Goudy old style", 15,), bg ="#6162FF", fg ="white",command =back)
bck.place(x = 90, y = 460, width = 100, height = 40)
# Print the OTP
print('OTP:', otp)

window.mainloop()
