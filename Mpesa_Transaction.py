import serial
import tkinter
import mysql.connector
from tkinter import messagebox
from PIL import ImageTk,Image


window = tkinter.Tk()
window.title("Mpesa_Payment")
window.geometry('1000x600')
window.resizable(False,False)

#Database
connection = mysql.connector.connect( host='localhost',
                                      user = 'root',
                                      port = '3306',
                                      password = '1234#',
                                      database = 'final_project')
c = connection.cursor()

#Background image
image_0 = Image.open("C:\\Users\\user\\Desktop\\Automated Petro Station\\Final\\images\\Gas.jpg")
bg = ImageTk.PhotoImage(image_0)
lbl=tkinter.Label(window,image = bg)
lbl.place(x = 0,y = 0,relheight=1,relwidth=1)

# Phone Number
def username_enter(e):
    phone_entry.delete(0,'end')
def username_leave(e):
    if phone_entry.get()=='':
           phone_entry.insert(0,'Phone Number')
lbu_phone = tkinter.Label(text ="PHONE NUMBER: ",font = ("Goudy old style",15,"bold"),fg = "Blue", bg = "black")
lbu_phone.place(x = 90, y = 200)
phone_entry = tkinter.Entry(font = ("Goudy old style",15,), bg = "#E7E6E6")
phone_entry.insert(0,"Phone Number")
phone_entry.bind("<FocusIn>",username_enter)
phone_entry.bind("<FocusOut>",username_leave)
phone_entry.place(x = 300, y = 200, width = 320, height = 30)


# Amount
def username_enter(e):
    amount_entry.delete(0,'end')
def username_leave(e):
    if amount_entry.get()=='':
           amount_entry.insert(0,'Amount')
lbu_amount = tkinter.Label(text ="AMOUNT: ",font = ("Goudy old style",15,"bold"),fg = "Blue", bg = "black")
lbu_amount.place(x = 90, y = 250)
amount_entry = tkinter.Entry(font = ("Goudy old style",15,), bg = "#E7E6E6")
amount_entry.insert(0,"Amount")
amount_entry.bind("<FocusIn>",username_enter)
amount_entry.bind("<FocusOut>",username_leave)
amount_entry.place(x = 300, y = 250, width = 320, height = 30)


def payment():
    phone_no = phone_entry.get().strip()
    amount = amount_entry.get()
    vals = (phone_no,amount,)
    select_query = "SELECT * FROM transaction WHERE phone_number = %s and amount = %s"
    c.execute(select_query,vals)
    user = c.fetchone()
    if  user is not None:
       status = user[3]
       if status == "YES":
           ser = serial.Serial('COM5', 9600)
           value = amount_entry.get()
           ser.write(value.encode())
           ser.close()
           window.destroy()
           messagebox.showinfo("Mpesa","Payment confirmed. MPESA code = " + user[0] + " Amount = " + str(user[2]))
       else:
           messagebox.showwarning("Error","Payment Not confirmed")
    else:
       messagebox.showwarning("Error","Invalid Entry")


#Button
Okay = tkinter.Button(text="CONFIRM", bd=0, cursor="hand2", font=("Goudy old style", 20, "bold"), fg="#6162FF",bg="black",command = payment)
Okay.place(x=350, y=320, width=200, height=40)

window.mainloop()