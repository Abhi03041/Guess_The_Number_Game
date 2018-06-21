# -*- coding: utf-8 -*-
"""
Created on Fri Jun 15 13:09:37 2018

@author: ABHINAVMITTAL
"""

from tkinter import*
from tkinter import messagebox

home=Tk()                               #figure home
home.title("Code_Breaker")              #title to the figure
codeframe=Frame(home)                   #frame to the figure
codeframe.grid()

complist = StringVar()                  #computer number 

precompnumber = IntVar(0)               #previous value of computer list

digitnumber = IntVar(0)                 #number of digits in user number
digitnumber.set(0)

guessnumber = IntVar(0)                 #user guessed number
guessnumber.set(0)

messages = IntVar()                     #Message to be display in the messagebox 
messages.set(0)

hintnumber = IntVar()                   #hint for digit position which user want to know 
hintnumber.set(0)

lifenumber = IntVar(0)                  #number of chances/life number
lifenumber.set(0)


def match():                                                            #Match function
    mess ="You have guessed a correct digit in the correct position.\n"
    return mess

def close():                                                            #Close function
    mess ="You have guessed a correct digit but position is wrong.\n"
    return mess

def Nope():                                                             #Nope function
    mess ="You have guessed a wrong digit that is not in the number.\n"
    return mess

def messagedisplay(a):                                                  #Messagedisplay function for message box
    messagebox.showinfo("Message",a)                                    #here is a is message that will be shown in the message box

def listconvert(guess,n):                                                 #List convert function,to convert user guess number into list form
    lt=[]                                                               # list                                                              # n is the number of digits in user guessed number
    while n>0:
        p=int(guess/pow(10,n-1))
        lt.append(p)
        guess=guess%pow(10,n-1)
        n=n-1
    return lt

def startplay():                                                        #startplay function that is in start button command 
    import random                                                       #In this we get the computer number that user has to guessed 
    digits = []                                                         #computer number will be store in digits
    for i in range(1):
        digits+=list(range(10))
        random.shuffle(digits)
    #print(digits)
    digits = ''.join(str(e) for e in digits)                            #To convet list into string
    complist.set(digits)                                                #complist in which we store digits in string  
    #print(complist.get())

def continueplay():                                                     #continueplay function that will work when continue button is pressed
    compnumber = int(complist.get())                                    #convert complist into int and store it in compnumber
    digit = listconvert(compnumber,10)
    guess=guessnumber.get()                                             #user guessed number
    n=digitnumber.get()                                                 # n is storing digitnumber
    t=lifenumber.get()                                                  # t is storing lifenumber
    y = precompnumber.get()                                             # y is storing precompnumber
    #print(y)
    if y != compnumber:
        if t is 0:
            if n>=3:
                lifenumber.set(n-3)
            else:
                lifenumber.set(0)
            precompnumber.set(compnumber)
            #print(precompnumber.get())
    #print(guess)
    lt=[]
    lt=listconvert(guess,n)                                             #convert user guessed number in list
    l=0                                                                 #l is storing the number of digits that have been matched
    p=0                                                                 # p is storing the number of digits that have been checked
    b=''                                                                # b is storing the message that has to be printed into message box
    for i in lt:
        if i  is digit[p]:
            mess=match()
            b=b+mess
            l=l+1
            p=p+1
        elif i in digit[:n]:
            mess=close()
            b=b+mess
            p=p+1
        else:
            mess=Nope()
            b=b+mess
            p=p+1
    if(l==n):                                                           #if all the digits matched 
        b = ''
        mess ="Congratulation,You have guessed the right number!"
        b=mess
    #print(b)
    messagedisplay(b)
    
def hinttosolve():                                                      #hinttosolve function that will work when hint button is pressed
    compnumber = int(complist.get())
    digit = listconvert(compnumber,10)
    d=lifenumber.get()                                                  #d is storing lifenumber
    k=hintnumber.get()                                                  #k is storing hintnumber
    x=digitnumber.get()                                                 #x is storing digit number
    if d>0:
        if(x>=3):
            if(k<=x):
                if(k>0):
                    ans = digit[k-1]
                    if( ans == 0):
                        messagedisplay("0")
                    else:
                        messagedisplay(ans)
                    d=d-1
                    lifenumber.set(d)
    else:
        mess = "You have no life!"
        messagedisplay(mess)
        
titleLabel = Label(codeframe, text = 'Code-Breaker', font = ("Arial", 20, "bold"), justify = CENTER)
titleLabel.grid(row = 1, column = 1, columnspan = 3, pady = 10, padx = 20)

startButton =Button(codeframe, text = "Start", font = ("Arial", 8, "bold"), relief = RAISED, bd=5, justify = CENTER, overrelief = GROOVE, activebackground = "green", activeforeground="blue", command = startplay)
startButton.grid(row = 2, column = 1, ipady = 8, ipadx = 12, pady = 5, sticky = NW, padx = 10)

digitLabel = Label(codeframe, text = "Enter the no. of digits in number: ", font = ("Arial", 16), fg = "blue")
digitLabel.grid(row = 3, column = 1, pady = 10, sticky = NW)

digitnoEntry = Entry(codeframe, width = 15, bd = 5, textvariable = digitnumber)
digitnoEntry.grid(row = 4, column = 1, pady = 10, sticky = NW,padx=10)

lifeLabel = Label(codeframe, text = "Life", font = ("Arial", 16), fg = "blue")
lifeLabel.grid(row = 5, column = 2, pady = 10, sticky = NW)

lifeEntry = Entry(codeframe, width = 15, bd = 5, textvariable = lifenumber)
lifeEntry.grid(row = 6, column = 2, pady = 10, sticky = NW,padx=10)

guessLabel = Label(codeframe, text = "What is your guess?  ", font = ("Arial", 16), fg = "blue")
guessLabel.grid(row = 5, column = 1, pady = 10, sticky = NW)

guessEntry = Entry (codeframe, width = 15, bd = 5, textvariable = guessnumber)
guessEntry.grid(row = 6, column = 1, pady = 10, sticky = NW, padx = 10 )

continueButton =Button(codeframe, text = "Continue", font = ("Arial", 8, "bold"), relief = RAISED, bd=5, justify = CENTER, overrelief = GROOVE, activebackground = "green", activeforeground="blue", command = continueplay)
continueButton.grid(row = 7, column = 1, ipady = 8, ipadx = 12, pady = 5, sticky = NW, padx = 10)

hintLabel = Label(codeframe, text = "Enter the digit position,you want to know:", font = ("Arial", 16), fg = "blue")
hintLabel.grid(row = 8, column = 1, pady = 10, sticky = NW)

hintEntry = Entry (codeframe, width = 15, bd = 5, textvariable = hintnumber)
hintEntry.grid(row = 9, column = 1, pady = 10, sticky = NW, padx = 10 )

hintButton =Button(codeframe, text = "Hint", font = ("Arial", 8, "bold"), relief = RAISED, bd=5, justify = CENTER, overrelief = GROOVE, activebackground = "green", activeforeground="blue", command = hinttosolve)
hintButton.grid(row = 10, column = 1, ipady = 8, ipadx = 12, pady = 5, sticky = NW, padx = 10)

home.mainloop()



