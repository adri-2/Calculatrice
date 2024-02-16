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
        text_resultat.delete(1.0,"end")
        text_resultat.insert(1.0,calcule)
    except:
        effacer_ecran()
        text_resultat.insert(1.0,"Erreur")
def effacer_ecran():
    global calcule
    calcule=""
    text_resultat.delete(1.0,"end")

root = Tk()
root.title("Calculatrise")
root.geometry("300x275")

text_resultat = Text(root,height=2,width=16,font=('Arial',24))
text_resultat.grid(columnspan=5)


btn_1 = Button(root,text="1",command=lambda:ajoute_calcul(1),width=5,font=('Arial',14))
btn_1.grid(row=2,column=1)

btn_2 = Button(root,text="2",command=lambda:ajoute_calcul(2),width=5,font=('Arial',14))
btn_2.grid(row=2,column=2)

btn_3 = Button(root,text="3",command=lambda:ajoute_calcul(3),width=5,font=('Arial',14))
btn_3.grid(row=2,column=3)

btn_4 = Button(root,text="4",command=lambda:ajoute_calcul(4),width=5,font=('Arial',14))
btn_4.grid(row=3,column=1)

btn_5 = Button(root,text="5",command=lambda:ajoute_calcul(5),width=5,font=('Arial',14))
btn_5.grid(row=3,column=2)

btn_6 = Button(root,text="6",command=lambda:ajoute_calcul(6),width=5,font=('Arial',14))
btn_6.grid(row=3,column=3)

btn_7 = Button(root,text="7",command=lambda:ajoute_calcul(7),width=5,font=('Arial',14))
btn_7.grid(row=4,column=1)

btn_8 = Button(root,text="8",command=lambda:ajoute_calcul(8),width=5,font=('Arial',14))
btn_8.grid(row=4,column=2)

btn_9 = Button(root,text="9",command=lambda:ajoute_calcul(9),width=5,font=('Arial',14))
btn_9.grid(row=4,column=3)

btn_0 = Button(root,text="0",command=lambda:ajoute_calcul(0),width=5,font=('Arial',14))
btn_0.grid(row=5,column=2)

btn_clear = Button(root,text="C",width=5,font=('Arial',14),command=effacer_ecran)
btn_clear.grid(row=1,column=2)

btn_open = Button(root,text=")",command=lambda:ajoute_calcul(")"),width=5,font=('Arial',14))
btn_open.grid(row=5,column=3)
#place
btn_close = Button(root,text="(",command=lambda:ajoute_calcul("("),width=5,font=('Arial',14))
btn_close.grid(row=5,column=1)

btn_addition = Button(root,text="+",command=lambda:ajoute_calcul("+"),width=5,font=('Arial',14))
btn_addition.grid(row=1,column=4)

btn_soudration = Button(root,text="-",command=lambda:ajoute_calcul("-"),width=5,font=('Arial',14))
btn_soudration.grid(row=2,column=4)

btn_division = Button(root,text="/",command=lambda:ajoute_calcul("/"),width=5,font=('Arial',14))
btn_division.grid(row=3,column=4)

btn_multiplication = Button(root,text="*",command=lambda:ajoute_calcul("*"),width=5,font=('Arial',14))
btn_multiplication.grid(row=4,column=4)

btn_equale = Button(root,text="=",command=eval_calcul,width=5,font=('Arial',14))
btn_equale.grid(row=5,column=4)


root.mainloop()