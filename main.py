from tkinter import *



calcule=""
def ajoute_calcul(symbol):
    global calcule
    calcule+=str(symbol)
    text_resultat.delete(1.0,"end")
    text_resultat.insert(1.0,calcule)
def eval_calcul():
    global calcule
    try:
        calcule=str(eval(calcule))
        resultat.delete(1.0,"end")
        resultat.insert(1.0,calcule)
    except:
        effacer_ecran()
        resultat.insert(1.0,"Erreur")
def effacer_ecran():
    global calcule
    calcule=""
    text_resultat.delete(1.0,"end")
    resultat.delete(1.0,"end")

root= Tk()
root.title("Calculatrise")
root.geometry("315x310")
#frame_window.resizable( width=False,height=False)
root.config(bg="skyblue")

frame_window = Frame(root,width=320, height=310,bg="blue")
frame_window.grid(row=0, column=0, padx=10, pady=5)

text_resultat = Text(frame_window,height=1,width=16,font=('Arial',24))
text_resultat.grid(columnspan=5)

resultat = Text(frame_window,height=1,width=16,font=('Arial',24))
resultat.grid(columnspan=5)


btn_1 = Button(frame_window,text="1",command=lambda:ajoute_calcul(11),width=5,font=('Arial',14))
btn_1.grid(row=3,column=1)

btn_2 = Button(frame_window,text="2",command=lambda:ajoute_calcul(2),width=5,font=('Arial',14))
btn_2.grid(row=3,column=2)

btn_3 = Button(frame_window,text="3",command=lambda:ajoute_calcul(3),width=5,font=('Arial',14))
btn_3.grid(row=3,column=3)

btn_4 = Button(frame_window,text="4",command=lambda:ajoute_calcul(4),width=5,font=('Arial',14))
btn_4.grid(row=4,column=1)

btn_5 = Button(frame_window,text="5",command=lambda:ajoute_calcul(5),width=5,font=('Arial',14))
btn_5.grid(row=4,column=2)

btn_6 = Button(frame_window,text="6",command=lambda:ajoute_calcul(6),width=5,font=('Arial',14))
btn_6.grid(row=4,column=3)

btn_7 = Button(frame_window,text="7",command=lambda:ajoute_calcul(7),width=5,font=('Arial',14))
btn_7.grid(row=5,column=1)

btn_8 = Button(frame_window,text="8",command=lambda:ajoute_calcul(8),width=5,font=('Arial',14))
btn_8.grid(row=5,column=2)

btn_9 = Button(frame_window,text="9",command=lambda:ajoute_calcul(9),width=5,font=('Arial',14))
btn_9.grid(row=5,column=3)

btn_0 = Button(frame_window,text="0",command=lambda:ajoute_calcul(0),width=5,font=('Arial',14))
btn_0.grid(row=6,column=2)

btn_clear = Button(frame_window,text="C",width=5,font=('Arial',14),command=effacer_ecran)
btn_clear.grid(row=7,column=2)

btn_open = Button(frame_window,text=")",command=lambda:ajoute_calcul(")"),width=5,font=('Arial',14))
btn_open.grid(row=6,column=3)
#place
btn_close = Button(frame_window,text="(",command=lambda:ajoute_calcul("("),width=5,font=('Arial',14))
btn_close.grid(row=6,column=1)

btn_equale = Button(frame_window,text="=",command=eval_calcul,width=5,font=('Arial',14))
btn_equale.grid(row=7,column=4)

btn_addition = Button(frame_window,text="+",command=lambda:ajoute_calcul("+"),width=5,font=('Arial',14))
btn_addition.grid(row=3,column=4)

btn_soudration = Button(frame_window,text="-",command=lambda:ajoute_calcul("-"),width=5,font=('Arial',14))
btn_soudration.grid(row=4,column=4)

btn_division = Button(frame_window,text="/",command=lambda:ajoute_calcul("/"),width=5,font=('Arial',14))
btn_division.grid(row=5,column=4)

btn_multiplication = Button(frame_window,text="*",command=lambda:ajoute_calcul("*"),width=5,font=('Arial',14))
btn_multiplication.grid(row=6,column=4)




frame_window.mainloop()