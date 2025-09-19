# THIS PROJECT IS ABOUT CALCULATING THE INTERNET SPEED

from tkinter import *
import speedtest 

def speedcheck():

    sp = speedtest.Speedtest()
    sp.get_servers()

    down = str(round(sp.download()/10**6)) + "Mbps"
    upload = str(round(sp.upload()/10**6)) + "Mbps"

    lab_down.config(text = down)
    lab_up.config(text = upload)

sp = Tk()
sp.title(" Internet speed Test")
sp.geometry("500x600")
sp.configure(bg="Grey")

lab = Label(sp, text ="Internet Speed Test", font = ("Time New Roman",20,"bold"), bg = "Grey")
lab.place(x=120,y=50,height = 50, width = 300)

lab = Label(sp, text ="Download Speed", font = ("Time New Roman",20,"bold"), bg = "Grey")
lab.place(x=120,y=150,height = 50, width = 300)

lab_down= Label(sp, text ="00", font = ("Time New Roman",20,"bold"), bg = "Grey")
lab_down.place(x=100,y=230,height = 50, width = 300)

lab = Label(sp, text ="Upload Speed", font = ("Time New Roman",20,"bold"), bg = "Grey")
lab.place(x=100,y=310,height = 50, width = 300)

lab_up = Label(sp, text ="00", font = ("Time New Roman",20,"bold"), bg = "Grey")
lab_up.place(x=100,y=390,height = 50, width = 300)

button = Button(sp, text ="Check Speed", font = ("Time New Roman",20,"bold"),
            relief =RAISED,command = speedcheck)
button.place(x=150,y=470,height = 50, width = 200)

sp.mainloop()