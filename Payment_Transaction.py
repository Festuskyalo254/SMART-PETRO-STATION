import tkinter
import serial
from tkinter import *
from PIL import ImageTk,Image
from tkinter import messagebox



window = tkinter.Tk()
window.title("Transaction")
window.geometry('1000x600')
window.resizable(False,False)

#Background image
image_0 = Image.open("C:\\Users\\user\\Desktop\\Automated Petro Station\\Final\\images\\Gas.jpg")
bg = ImageTk.PhotoImage(image_0)
lbl=tkinter.Label(window,image = bg)
lbl.place(x = 0,y = 0,relheight=1,relwidth=1)

def send_value():
    ser = serial.Serial('COM5', 9600)
    value = amount_entry.get()
    ser.write(value.encode())
    ser.close()

def check():
    amount = amount_entry.get()
    if amount.isdigit() or amount =="":
        return True
    else:
        messagebox.showwarning("Error", "Invalid Input")
        return False

validate_command_check = window.register(check)

def back():
    window.destroy()
    import Login

def calculate():
    amount = amount_entry.get()
    check_amount = (int(amount))/119
    lit_entry.config(state=NORMAL)
    lit_entry.delete(0, END)
    lit_entry.insert(0, str(check_amount))
    lit_entry.config(state="readonly")

#Amounts
def payment_enter(e):
   amount_entry.delete(0,'end')
def payment_leave(e):
    if amount_entry.get()=='':
        amount_entry.insert(0,'PAYMENT')


amount_user = tkinter.Label(text ="PAYMENT",font = ("Goudy old style",15,"bold"),fg = "#6162FF", bg = "white")
amount_user.place(x = 80, y = 170)
amount_entry = tkinter.Entry(font = ("Goudy old style",15,), bg = "#E7E6E6")
amount_entry.config(validatecommand = check,validate= "focusout")
amount_entry.insert(0,"PAYMENT")
amount_entry.bind("<FocusIn>", payment_enter)
amount_entry.bind("<FocusOut>", payment_leave)
amount_entry.place(x = 80, y = 200, width = 150, height = 35)
lit_entry = tkinter.Entry(text = "calculate")
lit_entry.place(x= 230,y =200, width=150,height=35)



#Litres
def litre_enter(e):
    litre_entry.delete(0,'end')
def litre_leave(e):
    if litre_entry.get()=='':
        litre_entry.insert(0,'LITRES')

litre_user = tkinter.Label(text ="LITRES",font = ("Goudy old style",15,"bold"),fg = "#6162FF", bg = "white")
litre_user.place(x = 450, y = 170)
litre_entry = tkinter.Entry(font = ("Goudy old style",15,), bg = "#E7E6E6")
litre_entry.insert(0,"LITRES")
litre_entry.bind("<FocusIn>", litre_enter)
litre_entry.bind("<FocusOut>", litre_leave)
litre_entry.place(x = 450, y = 200, width = 200, height = 35)
lit_entry = tkinter.Entry(font = ("Goudy old style",15,), bg = "#E7E6E6", state=DISABLED)
lit_entry.place(x= 550,y =200, width=150,height=35)


#Button
calc_button = tkinter.Button(text="CHECK", command = calculate,bd = 0,cursor = "hand2",font = ("Goudy old style",20,"bold"),fg = "#6162FF", bg = "black")
calc_button.place(x=350, y=300,width = 200,height = 40)

accept = tkinter.Button(text ="OKAY",bd = 0,cursor = "hand2",font = ("Goudy old style",20,"bold"),fg = "#6162FF", bg = "black",command=send_value)
accept.place(x = 350, y =380 ,width = 200,height = 40 )

bck = tkinter.Button( cursor ="hand2", text ="BACK", bd = 0, font = ("Goudy old style", 15,), bg ="#6162FF", fg ="white",command =back)
bck.place(x = 350, y = 440, width = 100, height = 40)


window.mainloop()