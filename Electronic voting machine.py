
import tkinter as tk
from tkinter import *
import os


def globals():
    global i1
    global i2
    global i3
    global i4
    global i5
    global b1
    global r
    global a
    global b2
    global t
    i1, i2, i3, i4, i5 = 0, 0, 0, 0, 0
    b1, r, a, b2, t = 0, 0, 0, 0, 0

def exit1():
    exit()
def reset():
    w3.window3.destroy()
    globals()
    w1()


def w1():
    w1.window1 = tk.Tk()

    w1.window1.title('Intro Window')

    w1.window1.geometry('400x400')

    w1.window1.resizable(False, False)

    frame1 = tk.Frame(w1.window1, width=400, height=600, bg="silver")
    frame1.pack()

    label1 = tk.Label(w1.window1, text="E.V.M", width=14, relief=GROOVE, bg="salmon", borderwidth=5)
    label1.config(font=('Arial bold', 25))
    label1.place(x=55, y=5)

    frame3 = tk.Frame(w1.window1, width=400, height=400, relief=FLAT, borderwidth=9, bg="turquoise")
    frame3.place(x=0, y=133)
    b3 = tk.Button(frame3, text="START\nVOTING", width=18, relief=RAISED, borderwidth=5, bg="aqua", command=w3)
    b3.config(font=('Arial bold', 20))
    b3.grid(row=0, column=0, padx=30)

    w1.window1.mainloop()


i1, i2, i3, i4, i5 = 0, 0, 0, 0, 0
b1, r, a, b2, t = 0, 0, 0, 0, 0
global next
next = True


def next1():
    global next
    next = True


def bjp():
    bjp.voted = True
    jdu.voted = False
    aap.voted = False
    rjd.voted = False
    trs.voted = False
    global next
    if next == True:
        global i1
        global b1
        b1 = i1 + 1
        i1 = b1
        next = False


def jdu():
    bjp.voted = False
    jdu.voted = True
    aap.voted = False
    rjd.voted = False
    trs.voted = False
    global next
    if next == True:
        global i2
        global r
        r = i2 + 1
        i2 = r
        next = False


def aap():
    bjp.voted = False
    jdu.voted = False
    aap.voted = True
    rjd.voted = False
    trs.voted = False
    global next
    if next == True:
        global i3
        global a
        a = i3 + 1
        i3 = a
        next = False


def rjd():
    bjp.voted = False
    jdu.voted = False
    aap.voted = False
    rjd.voted = True
    trs.voted = False
    global next
    if next == True:
        global i4
        global b2
        b2 = i4 + 1
        i4 = b2
        next = False


def trs():
    bjp.voted = False
    jdu.voted = False
    aap.voted = False
    rjd.voted = False
    trs.voted = True
    global next
    if next == True:
        global i5
        global t
        t = i5 + 1
        i5 = t
        next = False


def result():
    w4()


def verifybjp():
    if bjp.voted == True:
        global vote
        vote = "You have given the Vote to B.J.P\nThanks! to Vote."


def verifyjdu():
    if jdu.voted == True:
        global vote
        vote = "You have given the Vote to J.D.U\nThanks! to Vote."


def verifyaap():
    if aap.voted == True:
        global vote
        vote = "You have given the Vote to A.A.P\nThanks! to Vote."


def verifyrjd():
    if rjd.voted == True:
        global vote
        vote = "You have given the Vote to R.J.D\nThanks! to Vote."


def verifytrs():
    if trs.voted == True:
        global vote
        vote = "You have given the Vote to T.R.S\nThanks! to Vote."


def history():
    f = open('D:/E.V.M.txt', 'w')
    f.write("")
    f.close()

    f = open('D:/E.V.M.txt', 'a+')
    verifybjp()
    verifyjdu()
    verifyaap()
    verifyrjd()
    verifytrs()

    global vote
    f.write(vote)
    f.close()
    os.system("D:/E.V.M.txt")


def w3():
    w1.window1.destroy()
    w3.window3 = tk.Tk()
    w3.window3.title('Voting Window')
    w3.window3.geometry('400x600')
    w3.window3.resizable(False, False)

    frame1 = tk.Frame(w3.window3, width=400, height=600, bg="wheat")
    frame1.pack()

    label1 = tk.Label(w3.window3, text="E.V.M", width=14, relief=GROOVE, bg="salmon", borderwidth=5)
    label1.config(font=('Arial bold', 25))
    label1.place(x=55, y=5)
    frame2 = tk.Frame(w3.window3, width=400, height=50, bg="white")
    frame2.place(x=65, y=60)

    b1 = tk.Button(frame2, text="Previous", width=10, relief=RAISED, borderwidth=5, bg="yellow", command=reset)
    b1.config(font=('Arial bold', 10))
    b1.grid(row=0, column=2, padx=20)
    b2 = tk.Button(frame2, text="Exit(X)", width=10, relief=RAISED, borderwidth=5, bg="red", command=exit)
    b2.config(font=('Arial bold', 10))
    b2.grid(row=0, column=3, padx=20)

    frame5 = tk.Frame(w3.window3, width=400, height=400, relief=FLAT, borderwidth=9, bg="silver")
    frame5.place(x=32, y=100)

    b4 = tk.Button(frame5, text="B.J.P", width=20, relief=RAISED, borderwidth=5, bg="orange", command=bjp)
    b4.config(font=('Arial bold', 17))
    b4.grid(row=0, column=0, padx=12, pady=2)
    b5 = tk.Button(frame5, text="J.D.U", width=20, relief=RAISED, borderwidth=5, bg="Blue", command=jdu)
    b5.config(font=('Arial bold', 17))
    b5.grid(row=1, column=0, padx=12, pady=2)
    b6 = tk.Button(frame5, text="A.A.P", width=20, relief=RAISED, borderwidth=5, bg="white", command=aap)
    b6.config(font=('Arial bold', 17))
    b6.grid(row=2, column=0, padx=12, pady=2)
    b7 = tk.Button(frame5, text="R.J.D", width=20, relief=RAISED, borderwidth=5, bg="violet", command=rjd)
    b7.config(font=('Arial bold', 17))
    b7.grid(row=3, column=0, padx=12, pady=2)
    b8 = tk.Button(frame5, text="T.R.S", width=20, relief=RAISED, borderwidth=5, bg="teal", command=trs)
    b8.config(font=('Arial bold', 17))
    b8.grid(row=4, column=0, padx=12, pady=2)

    frame4 = tk.Frame(w3.window3, width=400, height=400, relief=FLAT, borderwidth=9, bg="silver")
    frame4.place(x=37, y=420)
    b9 = tk.Button(frame4, text="NEXT\nVOTER", width=12, relief=RAISED, borderwidth=5, bg="brown", command=next1)
    b9.config(font=('Arial bold', 10))
    b9.grid(row=0, column=0, padx=100, pady=5)

    b10 = tk.Button(frame4, text="RESULT", width=8, relief=RAISED, borderwidth=5, bg="turquoise", command=result)
    b10.config(font=('Arial bold', 15))
    b10.grid(row=1, column=0, padx=100, pady=5)

    w3.window3.mainloop()


def counting():
    f = open('D:/E.V.M.txt', 'w')
    f.write("")
    f.close()

    f = open('D:/E.V.M.txt', 'a+')
    bjp = "Total Votes for B.J.P are:- " + str(b1) + "\n"
    jdu = "Total Votes for J.D.U are:- " + str(r) + "\n"
    aap = "Total Votes for A.A.P are:- " + str(a) + "\n"
    rjd = "Total Votes for R.J.D are:- " + str(b2) + "\n"
    trs = "Total Votes for T.R.S are:- " + str(t) + "\n\n"

    f.write(bjp)
    f.write(jdu)
    f.write(aap)
    f.write(rjd)
    f.write(trs)
    f.close()

    os.system("D:/E.V.M.txt")


global b1winner
global rwinner
global awinner
global b2winner
global twinner
b1winner = False
rwinner = False
awinner = False
b2winner = False
twinner = False
global temptie
temptie=0

def w4():
    w3.window3.destroy()
    w4.window4 = tk.Tk()
    w4.window4.title('Result Window')
    w4.window4.geometry('400x600')
    w4.window4.resizable(False, False)

    frame1 = tk.Frame(w4.window4, width=400, height=600, bg="red")
    frame1.pack()

    label1 = tk.Label(w4.window4, text="E.V.M", width=14, relief=GROOVE, bg="salmon", borderwidth=5)
    label1.config(font=('Arial bold', 25))
    label1.place(x=55, y=5)

    a1 = "B.J.P\n" + str(b1)
    a2 = "J.D.U\n" + str(r)
    a3 = "A.A.P\n" + str(a)
    a4 = "R.J.D\n" + str(b2)
    a5 = "T.R.S\n" + str(t)
    list1 = [b1, r, a, b2, t]
    w4.high = max(list1)
    global temptie
    global tie
    if b1 == w4.high:
        global b1winner
        tie=temptie+1
        temptie=tie
        b1winner = True
    if r == w4.high:
        global rwinner
        tie=temptie+1
        temptie=tie
        rwinner = True
    if a == w4.high:
        global awinner
        tie=temptie+1
        temptie=tie
        awinner = True
    if b2 == w4.high:
        global b2winner
        tie=temptie+1
        temptie=tie
        b2winner = True
    if t == w4.high:
        global twinner
        tie=temptie+1
        temptie=tie
        twinner = True

    frame5 = tk.Frame(w4.window4, width=400, height=400, relief=FLAT, borderwidth=9, bg="white")
    frame5.place(x=28, y=70)

    label7 = tk.Label(frame5, text=a1, width=24, relief=RIDGE, borderwidth=5, bg="orange")
    label7.config(font=('Arial bold', 15))
    label7.grid(row=0, column=0, padx=12, pady=6)
    label8 = tk.Label(frame5, text=a2, width=24, relief=RIDGE, borderwidth=5, bg="blue")
    label8.config(font=('Arial bold', 15))
    label8.grid(row=1, column=0, padx=12, pady=6)
    label9 = tk.Label(frame5, text=a3, width=24, relief=RIDGE, borderwidth=5, bg="white")
    label9.config(font=('Arial bold', 15))
    label9.grid(row=2, column=0, padx=12, pady=6)
    label10 = tk.Label(frame5, text=a4, width=24, relief=RIDGE, borderwidth=5, bg="violet")
    label10.config(font=('Arial bold', 15))
    label10.grid(row=3, column=0, padx=12, pady=6)
    label11 = tk.Label(frame5, text=a5, width=24, relief=RIDGE, borderwidth=5, bg="teal")
    label11.config(font=('Arial bold', 15))
    label11.grid(row=4, column=0, padx=12, pady=6)

    frame4 = tk.Frame(w4.window4, width=500, height=500, relief=FLAT, borderwidth=9, bg="white")
    frame4.place(x=28, y=450)
    b12 = tk.Button(frame4, text="COUNTING", width=9, relief=RAISED, borderwidth=5, bg="skyblue", command=counting)
    b12.config(font=('Arial bold', 15))
    b12.grid(row=0, column=0, padx=100, pady=5)

    b13 = tk.Button(frame4, text="WINNER", width=9, relief=RAISED, borderwidth=5, bg="lime green", command=win5)
    b13.config(font=('Arial bold', 15))
    b13.grid(row=1, column=0, padx=100, pady=5)
    w4.window4.mainloop()

def win5():
    w4.window4.destroy()
    window5 = tk.Tk()
    window5.title('Final Result')
    window5.geometry('400x600')
    window5.resizable(False, False)
    global b1winner
    global rwinner
    global awinner
    global b2winner
    global twinner

    frame1 = tk.Frame(window5, width=400, height=600, bg="#7FFFD4")
    frame1.pack()
    global tie
    if tie > 1:
        strtie="TIE B/W "+str(tie)
        label1 = tk.Label(window5, text=strtie, width=14, relief=RIDGE, bg="hot pink", borderwidth=5)
        label1.config(font=('Arial bold', 25))
        label1.place(x=55, y=5)
    else :
        label1 = tk.Label(window5, text="WINNER", width=14, relief=RIDGE, bg="hot pink", borderwidth=5)
        label1.config(font=('Arial bold', 25))
        label1.place(x=55, y=5)

    a1="B.J.P\n"+str(b1)
    a2="J.D.U\n"+str(r)
    a3="A.A.P\n"+str(a)
    a4="R.J.D\n"+str(b2)
    a5="T.R.S\n"+str(t)


    frame5 = tk.Frame(window5, width=400, height=400, relief=FLAT, borderwidth=9, bg="#7FFFD4")
    frame5.place(x=28, y=70)

    if b1winner == True:
        label7 = tk.Label(frame5, text=a1, width=24, relief=RIDGE, borderwidth=5, bg="orange")
        label7.config(font=('Arial bold', 15))
        label7.grid(row=0, column=0, padx=12, pady=6)
    if rwinner == True:
        label8 = tk.Label(frame5, text=a2, width=24, relief=RIDGE, borderwidth=5, bg="blue")
        label8.config(font=('Arial bold', 15))
        label8.grid(row=1, column=0, padx=12, pady=6)
    if awinner == True:
        label9 = tk.Label(frame5, text=a3, width=24, relief=RIDGE, borderwidth=5, bg="white")
        label9.config(font=('Arial bold', 15))
        label9.grid(row=2, column=0, padx=12, pady=6)
    if b2winner == True:
        label10 = tk.Label(frame5, text=a4, width=24, relief=RIDGE, borderwidth=5, bg="violet")
        label10.config(font=('Arial bold', 15))
        label10.grid(row=3, column=0, padx=12, pady=6)
    if twinner == True:
        label11 = tk.Label(frame5, text=a5, width=24, relief=RIDGE, borderwidth=5, bg="teal")
        label11.config(font=('Arial bold', 15))
        label11.grid(row=4, column=0, padx=12, pady=6)

    btn4 = tk.Button(window5, text="COUNTING", width=9, relief=RAISED, borderwidth=5, bg="lime green",command=counting)
    btn4.config(font=('Arial bold', 15))
    btn4.place(x=132,y=450)
    btn4 = tk.Button(window5, text="EXIT(X)", width=9, relief=RAISED, borderwidth=5, bg="hot pink",command=exit1)
    btn4.config(font=('Arial bold', 15))
    btn4.place(x=132,y=510)

    window5.mainloop()


w1()


