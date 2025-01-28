from tkinter import*
from collections import Counter

logs =  Tk()
logs.title("Kases aparāts")
logs.geometry("800x700")
logs.configure(bg='#E5E5E5')

produkta_cenas = {
    "Ābols": 0.50,
    "Bumbieris": 0.75,
    "Apelsīns": 1.00,
    "Mandarīni": 1.20,
    "Sīpoli": 0.30,
    "Tomāts": 0.80,
    "Gurķis": 0.60,
    "Paprika": 1.10,
    "Vistas gaļa": 5.00,
    "Liellopu gaļa": 7.00,
    "Cūkgaļa": 6.50,
    "Jēru gaļa": 8.00
}

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

####### izmantoju AI
def lietotaja_izvēle(produkts):
    
    global cena

    if produkts in produkta_cenas:
        cena = produkta_cenas[produkts]
        lietotaja_preces.append((produkts, cena))
        kases_aprāts_ekrāns.insert(END, f"{produkts} - €{cena:.2f}\n")


def nonemt_preces():
    if lietotaja_preces:
        lietotaja_preces.pop()
        kases_aprāts_ekrāns.delete(1.0, END)
        for produkts, cena in lietotaja_preces:
            kases_aprāts_ekrāns.insert(END, f"{produkts} - €{cena:.2f}\n")
#########################

def kopējā_summa():
    summa = sum(cena for _, cena in lietotaja_preces)
    summa_text.config(text=f'Kopā: €{summa:.2f}')

summa_text = Label(logs, text="Kopā: 0.00", font=("Helvetica"), bg='#E5E5E5')
summa_text.place(x= 630, y= 420)


nonemt_preces_poga = Button(logs, text= 'Noņemt pēdējo preci', fg='white', bg='red', command=nonemt_preces, padx=27, pady=20)
nonemt_preces_poga.place(x= 440, y= 580)


nauda ={
    '1 cents': 0.01,
    '2 centi': 0.02,
    '5 centi': 0.05,
    '10 centi':0.10,
    '20 centi':0.20,
    '50 centi': 0.50,
    '1 Eiro': 1.00,
    '2 Eiro': 2.00,
    '5 Eiro': 5.00,
    '10 Eiro': 10.00,
    '20 Eiro': 20.00,
    '50 Eiro': 50.00,
    '100 Eiro': 100.00
}

poga_1 = Button(logs, text="1 cents", bg='lightgrey',padx=20, pady=20)
poga_1.place(x= 50, y= 420)
poga_2 = Button(logs, text="2 centi", bg='lightgrey',padx=20, pady=20)
poga_2.place(x= 140, y= 420)
poga_3 = Button(logs, text="5 centi", bg='lightgrey',padx=20, pady=20)
poga_3.place(x= 230, y= 420)
poga_4 = Button(logs, text="10 centi", bg='lightgrey',padx=18, pady=20)
poga_4.place(x= 50, y= 500)
poga_5 = Button(logs, text="20 centi", bg='lightgrey',padx=18, pady=20)
poga_5.place(x= 140, y= 500)
poga_6 = Button(logs, text="50 centi", bg='lightgrey',padx=18, pady=20)
poga_6.place(x= 230, y= 500)
poga_7 = Button(logs, text="1 Eiro", bg='lightgrey',padx=24, pady=20)
poga_7.place(x= 50, y= 580)
poga_8 = Button(logs, text="2 Eiro", bg='lightgrey',padx=24, pady=20)
poga_8.place(x= 140, y= 580)
poga_9 = Button(logs, text="5 Eiro", bg='lightgrey',padx=24, pady=20)
poga_9.place(x= 230, y= 580)
poga_10 = Button(logs, text="10 Eiro", bg='lightgray', padx=20, pady=20)
poga_10.place(x= 350, y= 420)
poga_11 = Button(logs, text='20 Eiro', bg='lightgray', pady=20, padx=20)
poga_11.place(x= 440, y= 420)
poga_12 = Button(logs, text="50 Eiro", bg='lightgrey', pady=20, padx=20)
poga_12.place(x= 530, y= 420)
poga_13 = Button(logs, text='100 Eiro', bg='lightgrey', pady=20, padx=107)
poga_13.place(x= 350,y= 500)


poga_enter = Button(logs, text="enter", bg='lightgreen',padx=20, pady=20, command=kopējā_summa)
poga_enter.place(x= 350, y= 580)


poga_pabiegt_pirkumu = Button(logs, text="Pabeigt pirkumu", bg='lightgreen', padx=20, pady=20)
poga_pabiegt_pirkumu.place(x=620, y=580 )


logs.mainloop()