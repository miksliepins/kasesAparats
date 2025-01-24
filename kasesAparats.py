from tkinter import*


logs =  Tk()
logs.title("Kases aparāts")
logs.geometry("800x700")
logs.configure(bg='#E5E5E5')



#################################### Augļu logs
def augļi_darzeņi_logs():
    
    global auglu_darzenuLogs

    auglu_darzenuLogs = Toplevel()
    auglu_darzenuLogs.geometry('500x400')
    auglu_darzenuLogs.title('Augļi un dārzeņi')
    ābols = Button(auglu_darzenuLogs, text='Ābols',fg='white', bg='#3b3b3b', width=12, height=2, command=lambda: lietotaja_izvēle("Ābols"))
    ābols.place(x= 80, y= 50)
    Bumbieris = Button(auglu_darzenuLogs, text='Bumbieris', fg='white', bg='#3b3b3b', width=12, height=2, command=lambda: lietotaja_izvēle("Bumbieris"))
    Bumbieris.place(x= 80, y= 100)
    Apelsīns = Button(auglu_darzenuLogs, text='Apelsīns', fg= 'white', bg= '#3b3b3b', width=12, height= 2, command=lambda: lietotaja_izvēle("Apelsīns"))
    Apelsīns.place(x= 80, y= 150)
    Mandarīni = Button(auglu_darzenuLogs, text='Mandarīni', fg='white', bg='#3b3b3b', width=12, height=2, command= lambda: lietotaja_izvēle("Mandarīni"))
    Mandarīni.place(x= 80, y= 200)
    Sīpoli = Button(auglu_darzenuLogs, text='Sīpoli', fg='white', bg='#3b3b3b', width=12, height=2, command= lambda: lietotaja_izvēle("Sīpoli"))
    Sīpoli.place(x= 270, y= 50)
    Tomāts = Button(auglu_darzenuLogs, text='Tomāts', fg='white', bg='#3b3b3b', width=12, height=2, command= lambda: lietotaja_izvēle("Tomāts"))
    Tomāts.place(x= 270, y= 100)
    Gurķis = Button(auglu_darzenuLogs, text='Gurķis', fg='white', bg='#3b3b3b', width=12, height=2, command= lambda: lietotaja_izvēle("Gurķis"))
    Gurķis.place(x= 270, y= 150)
    Paprika = Button(auglu_darzenuLogs, text='Paprika', fg='white', bg='#3b3b3b', width=12, height=2, command= lambda: lietotaja_izvēle("Paprika"))
    Paprika.place(x= 270, y= 200)

################## Gaļas logs
def Gaļas_atver_logu():
    
    global Gaļas_logs

    Gaļas_logs = Toplevel()
    Gaļas_logs.geometry('500x400')
    Gaļas_logs.title("Gaļas produkti")
    Vistas_gaļa = Button(Gaļas_logs, text='Vistas gaļa', fg='white', bg='#3b3b3b', width=12, height=2, command= lambda: lietotaja_izvēle("Vistas gaļa"))
    Vistas_gaļa.place(x= 80, y= 50)
    Liellopu_gaļa = Button(Gaļas_logs, text='Liellopu gaļa', fg='white', bg='#3b3b3b', width=12, height=2, command= lambda: lietotaja_izvēle("Liellopu gaļa"))
    Liellopu_gaļa.place(x= 80, y= 100)
    Cūkgaļa = Button(Gaļas_logs, text='Cūkgaļa', fg='white', bg='#3b3b3b', width=12, height=2, command= lambda: lietotaja_izvēle("Cūkgaļa"))
    Cūkgaļa.place(x= 80, y= 150)
    Jēru_gaļa = Button(Gaļas_logs, text='Jēru gaļa', fg='white', bg='#3b3b3b', width=12, height=2, command= lambda: lietotaja_izvēle("Jēru gaļa"))
    Jēru_gaļa.place(x= 80, y= 200)

####################################### pogas
augli_darzeni_poga = Button(logs, text='Augļu un dārzeņi', fg='white', bg='#3b3b3b', width=30, height=3, command=augļi_darzeņi_logs)
gaļas_poga = Button(logs, text='Gaļas', fg='white', bg='#3b3b3b', width=30, height=3, command=Gaļas_atver_logu)
graudu_produkti_poga =Button(logs, text='Graudu produkti', fg='white', bg='#3b3b3b', width=30, height=3)
saldētie_produkti_poga = Button(logs, text='Saldētie produkti', fg='white', bg='#3b3b3b', width=30, height=3)
piena_produkti_poga =Button(logs, text='Piena produkti', fg='white', bg='#3b3b3b', width=30, height=3)


augli_darzeni_poga.place(x= 85, y = 60)
gaļas_poga.place(x= 85, y= 130)
graudu_produkti_poga.place(x= 85, y= 200)
saldētie_produkti_poga.place(x = 85, y= 270)
piena_produkti_poga.place(x= 85, y= 340)
########################################


kases_aprāts_ekrāns = Text(logs, width=40, height= 15, bg= 'lightblue', font='Helvetica', padx= 10, pady=10)
kases_aprāts_ekrāns.place(x= 350, y= 55)

ritinātājs = Scrollbar(logs)

lietotaja_preces = []


def lietotaja_izvēle(produkts):
    lietotaja_preces.append(produkts)
    kases_aprāts_ekrāns.insert(END, produkts + "\n")

def nonemt_preces():
    lietotaja_preces.pop()
    kases_aprāts_ekrāns.delete()
    print(lietotaja_preces)


nonemt_preces_poga = Button(logs, text= 'Noņemt pēdējo preci', fg='white', bg='red', command=nonemt_preces, padx=20, pady=20)
nonemt_preces_poga.place(x= 510, y= 630)


poga_1 = Button(logs, text=9, bg='lightgrey',padx=20, pady=20)
poga_1.place(x= 430, y= 380)
poga_2 = Button(logs, text=8, bg='lightgrey',padx=20, pady=20)
poga_2.place(x= 500, y= 380)
poga_3 = Button(logs, text=7, bg='lightgrey',padx=20, pady=20)
poga_3.place(x= 570, y= 380)
poga_4 = Button(logs, text=6, bg='lightgrey',padx=20, pady=20)
poga_4.place(x= 430, y= 470)
poga_5 = Button(logs, text=5, bg='lightgrey',padx=20, pady=20)
poga_5.place(x= 500, y= 470)
poga_6 = Button(logs, text=4, bg='lightgrey',padx=20, pady=20)
poga_6.place(x= 570, y= 470)
poga_7 = Button(logs, text=3, bg='lightgrey',padx=20, pady=20)
poga_7.place(x= 430, y= 560)
poga_8 = Button(logs, text=2, bg='lightgrey',padx=20, pady=20)
poga_8.place(x= 500, y= 560)
poga_9 = Button(logs, text=1, bg='lightgrey',padx=20, pady=20)
poga_9.place(x= 570, y= 560)
poga_enter = Button(logs, text="enter", bg='lightgreen',padx=20, pady=20)
poga_enter.place(x= 430, y= 630)



logs.mainloop()