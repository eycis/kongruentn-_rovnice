import math
from tkinter import ttk
from tkinter import *
from tkinter import messagebox

def congruent():
    a_get = int(a.get())
    b_get = int(b.get())
    mod_get = int(mod.get())

    if b_get%math.gcd(a_get, mod_get)!=0: # pokud jednotlivé členy nemají společný násobek, rovnice nemá řešení.
        messagebox.showinfo("error","rovnice nemá řešení")

    nsd=math.gcd(a_get,mod_get)
    if b_get%nsd==0:   #pokud je b dělitelné NSD, můžeme pokračovat.
        a_get =a_get/nsd        #dělení společným násobkem
        b_get= b_get/nsd
        mod_get = mod_get/nsd 
        i=1
        while i<mod_get:        #hledání inverze, poté vyřešení rovnice a výpis řešení v okně.
            if (a_get*i)%mod_get==1:
                b_get=(b_get*i)%mod_get
                print("%i je vysledek kongruence"%(b_get))
                messagebox.showinfo("výsledek kongruence je: ",(b_get))
                break
            else:
                i=i+1

def root():
    root = Tk()
    root.geometry("300x300")

    global a
    a = StringVar()
    global mod
    mod = StringVar()
    global b
    b = StringVar()

    main_label = Label(root, text = "Kongruentní rovnice", width="300", height="3")
    main_label.pack()
    a_entry = Entry(root, width=25, borderwidth=5, text = "a", textvariable=a)
    a_entry.pack()
    b_entry = Entry(root, width=25, borderwidth=5,text = "b", textvariable=b)
    b_entry.pack()
    mod_entry = Entry(root, width=25, borderwidth=5, text = "mod", textvariable=mod)
    mod_entry.pack()
    mainbutton = Button(root, text="vypočti kongruentní rovnici", command=congruent)
    mainbutton.pack()
    root.mainloop()

root()
#congruent(11,1,7171)
#congruent(9,12,15) -má řešení obě
#congruent(2,5,6) - nemá řešení

    