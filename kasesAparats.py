from tkinter import*

logs =  Tk()
logs.title("Kases aparāts")
logs.geometry("800x700")
logs.configure(bg='#E5E5E5')


lietotaja_preces = []

def lietotaja_izvēle():
    


def augļi_darzeņi_logs():
    auglu_darzenuLogs = Toplevel()
    auglu_darzenuLogs.geometry('500x400')
    auglu_darzenuLogs.title('augļi un dārzeņi')
    abola_izvele = Button(logs, text='Ābols')
    

####################################### pogas
augli_darzeni_poga = Button(logs, text='Augļu un dārzeņi', fg='white', bg='#3b3b3b', width=30, height=3, command=augļi_darzeņi_logs)
gaļas_poga = Button(logs, text='Gaļas', fg='white', bg='#3b3b3b', width=30, height=3)
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

for produkts in lietotaja_preces:
    kases_aprāts_ekrāns.insert(END, produkts + "\n")


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
poga_enter.place(x= 490, y= 630)



logs.mainloop()