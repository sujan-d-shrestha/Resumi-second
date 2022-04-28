from tkinter import *
from necessities import *
import random
a = [0,1,2,3,4,5,6,7,8]
i = random.choice([0,1])
AI_active = False
Bot = AI()
once_count = 1

def input0():
    global i; i = (i+ 1)%2; a[0] = Symbols[i] ;button_0.configure(text=Symbols[i],state=DISABLED)
    if(state(a)=="O")or(state(a)=="X"):disable_all()
    if AI_active: AI_plays(a)
    update_frame()
def input1():
    global i; i = (i+ 1)%2; a[1] = Symbols[i] ;button_1.configure(text=Symbols[i],state=DISABLED)
    if(state(a)=="O")or(state(a)=="X"):disable_all()
    if AI_active: AI_plays(a)
    update_frame()
def input2():
    global i;i = (i+ 1)%2;a[2] = Symbols[i] ;button_2.configure(text=Symbols[i],state=DISABLED)
    if(state(a)=="O")or(state(a)=="X"):disable_all()
    if AI_active: AI_plays(a)
    update_frame()
def input3():
    global i;i = (i+ 1)%2;a[3] = Symbols[i] ;button_3.configure(text=Symbols[i],state=DISABLED)
    if(state(a)=="O")or(state(a)=="X"):disable_all()
    if AI_active: AI_plays(a)
    update_frame()
def input4():
    global i;i = (i+ 1)%2;a[4] = Symbols[i] ;button_4.configure(text=Symbols[i],state=DISABLED)
    if(state(a)=="O")or(state(a)=="X"):disable_all()
    if AI_active: AI_plays(a)
    update_frame()
def input5():
    global i;i = (i+ 1)%2;a[5] = Symbols[i] ;button_5.configure(text=Symbols[i],state=DISABLED)
    if(state(a)=="O")or(state(a)=="X"):disable_all()
    if AI_active: AI_plays(a)
    update_frame()
def input6():
    global i;i = (i+ 1)%2;a[6] = Symbols[i] ;button_6.configure(text=Symbols[i],state=DISABLED)
    if(state(a)=="O")or(state(a)=="X"):disable_all()
    if AI_active: AI_plays(a)
    update_frame()
def input7():
    global i;i = (i+ 1)%2;a[7] = Symbols[i] ;button_7.configure(text=Symbols[i],state=DISABLED)
    if(state(a)=="O")or(state(a)=="X"):disable_all()
    if AI_active: AI_plays(a)
    update_frame()
def input8():
    global i;i = (i+ 1)%2;a[8] = Symbols[i] ;button_8.configure(text=Symbols[i],state=DISABLED)
    if(state(a)=="O")or(state(a)=="X"):disable_all()
    if AI_active: AI_plays(a)
    update_frame()
    
def reset(): 
    global i,a,once_count ;i = random.choice([0,1]);a =[0,1,2,3,4,5,6,7,8];enable_all();once_count = 1
    if AI_active:AI_plays(a);Bot.me = Symbols[(i+1)%2]
    else: i = random.choice([0,1]) 
    

def Activate_Ai():
    global AI_active,Bot
    if AI_active == False:
        AI_active = True; AI_or_not_button.configure(text="Vs Human")
        Ai_first.pack(side=RIGHT)
        You_are.pack(side=LEFT,padx=2)
    else:
        AI_active = False; AI_or_not_button.configure(text="Vs AI")
        Ai_first.pack_forget()
        You_are.pack_forget()
    reset()
    update_frame()
   

def Ai_first_or_not():
    if Bot.first: Bot.first = False; Ai_first.configure(text="AI Second")
    else: Bot.first = True; Ai_first.configure(text="AI First")
    reset()

root = Tk()
root.title("Tic Tac Toe")
root.resizable(False,False)


design_label = Label(root,text="Tic Tac Toe",font="Times 20 bold")
design_label.pack()

You_are = Label(root)

frame = LabelFrame(root,text=Symbols[(i+1)%2]+"'s turn")
frame.pack(padx=0,pady=0)

reset_button = Button(root,text="Reset",command=reset)
reset_button.pack(side=RIGHT,padx=1)

Ai_first = Button(root,text="AI First",command=Ai_first_or_not)

AI_or_not_button = Button(root,text="Vs AI",command=Activate_Ai)
AI_or_not_button.pack(side=LEFT,padx=1)

button_0 = Button(frame,height=5,width=10,command=input0)
button_1 = Button(frame,height=5,width=10,command=input1)
button_2 = Button(frame,height=5,width=10,command=input2)
button_3 = Button(frame,height=5,width=10,command=input3)
button_4 = Button(frame,height=5,width=10,command=input4)
button_5 = Button(frame,height=5,width=10,command=input5)
button_6 = Button(frame,height=5,width=10,command=input6)
button_7 = Button(frame,height=5,width=10,command=input7)
button_8 = Button(frame,height=5,width=10,command=input8)

button_0.grid(column=0,row=0)
button_1.grid(column=1,row=0)
button_2.grid(column=2,row=0)
button_3.grid(column=0,row=1)
button_4.grid(column=1,row=1)
button_5.grid(column=2,row=1)
button_6.grid(column=0,row=2)
button_7.grid(column=1,row=2)
button_8.grid(column=2,row=2)

def disable_all():
    update_frame()
    button_0.configure(state=DISABLED)
    button_1.configure(state=DISABLED)
    button_2.configure(state=DISABLED)
    button_3.configure(state=DISABLED)
    button_4.configure(state=DISABLED)
    button_5.configure(state=DISABLED)
    button_6.configure(state=DISABLED)
    button_7.configure(state=DISABLED)
    button_8.configure(state=DISABLED)
    
def enable_all():
    update_frame()
    button_0.configure(text="",height=5,width=10,state=ACTIVE)
    button_1.configure(text="",height=5,width=10,state=ACTIVE)
    button_2.configure(text="",height=5,width=10,state=ACTIVE)
    button_3.configure(text="",height=5,width=10,state=ACTIVE)
    button_4.configure(text="",height=5,width=10,state=ACTIVE)
    button_5.configure(text="",height=5,width=10,state=ACTIVE)
    button_6.configure(text="",height=5,width=10,state=ACTIVE)
    button_7.configure(text="",height=5,width=10,state=ACTIVE)
    button_8.configure(text="",height=5,width=10,state=ACTIVE)
    
def update_frame():
    global once_count
    if state(a) == "continue": frame.configure(text=Symbols[(i+1)%2].upper()+"'s turn")
    elif state(a) == "O" or state(a) == "X": frame.configure(text=state(a).upper()+" is the winner");
    else: frame.configure(text=" It's a draw");       
    if AI_active and once_count == 1: You_are.configure(text="You are "+Symbols[(i+1)%2]);once_count = 0
        
def AI_plays(array):
    position = Bot.return_position(array)
    if position == None: pass
    elif position == 0: input0() 
    elif position == 1: input1() 
    elif position == 2: input2() 
    elif position == 3: input3() 
    elif position == 4: input4() 
    elif position == 5: input5() 
    elif position == 6: input6() 
    elif position == 7: input7() 
    elif position == 8: input8() 
     
             
root.mainloop()




























