import tkinter
import mysql.connector
from PIL import ImageTk,Image



window = tkinter.Tk()
window.title("ADMINISTRATOR")
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

def signin():
    window.destroy()
    import New_Registration

def back():
    window.destroy()
    import Login

#Button
signIn_button = tkinter.Button(cursor ="hand2", text ="Sign In", bd = 0, font = ("Goudy old style", 15,), bg ="#6162FF", fg ="white",command =signin)
signIn_button.place(x = 90, y = 50, width = 100, height = 40)

bck = tkinter.Button(cursor ="hand2", text ="BACK", bd = 0, font = ("Goudy old style", 15,), bg ="#6162FF", fg ="white",command =back)
bck.place(x = 90, y = 400, width = 100, height = 40)



window.mainloop()