from tkinter import *

window = Tk()
window.geometry("800x600")

def calculate():
    if e1.get() =='':
        Geprek = 0
    else:
        Geprek = e1.get()

    if e2.get() =='':
        Telur = 0
    else:
        Telur = e2.get()

    if e3.get() =='':
        Nugget = 0
    else:
        Nugget = e3.get()

    if e4.get() =='':
        Teh = 0
    else:
        Teh = e4.get()
    
    if e5.get() =='':
        Jeruk = 0
    else:
        Jeruk = e5.get()
    
    total = int(Geprek)*14 + int(Telur)*14 + int(Nugget)*15 + int(Teh)*3 + int(Jeruk)*4

    labeltotal = Label(window, text=total,font="times 20")
    labeltotal.place(x=350,y=450, anchor="center")

    

#---Menu section

Label1 = Label(window,text="Menu", font= "times 28 bold")
Label1.place(x=550, y=70)

Label2 = Label(window,text="Nasi Goreng Geprek         Rp 14K", font= "times 18")
Label2.place(x=450, y=120)

Label3 = Label(window,text="Nasi Goreng Telur          Rp 14K", font= "times 18")
Label3.place(x=450, y=150)

Label3 = Label(window,text="Nasi Goreng Nugget         Rp 15K", font= "times 18")
Label3.place(x=450, y=180)

Label3 = Label(window,text="Teh (Es/Hangat)            Rp 3K", font= "times 18")
Label3.place(x=450, y=210)

Label4 = Label(window,text="Jeruk (Es/Hangat)          Rp 4K", font= "times 18")
Label4.place(x=450, y=240)

#----Billing section

Label5 = Label(window,text="Nasi Goreng Geprek         Rp 14K", font= "times 18")
Label5.place(x=20, y=120)

e1 = Entry(window)
e1.place(x=20,y=150)

Label6 = Label(window,text="Nasi Goreng Telur          Rp 14K", font= "times 18")
Label6.place(x=20, y=180)

e2 = Entry(window)
e2.place(x=20,y=210)

Label7 = Label(window,text="Nasi Goreng Nugget         Rp 15K", font= "times 18")
Label7.place(x=20, y=240)

e3 = Entry(window)
e3.place(x=20,y=270)

Label8 = Label(window,text="Teh (Es/Hangat)            Rp 3K", font= "times 18")
Label8.place(x=20, y=300)

e4 = Entry(window)
e4.place(x=20,y=330)

Label9 = Label(window,text="Jeruk (Es/Hangat)          Rp 4K", font= "times 18")
Label9.place(x=20, y=360)

e5 = Entry(window)
e5.place(x=20,y=390)

b = Button(window,text="Hitung", width=20, command=calculate)
b.place(x=20, y=420)

window.mainloop()