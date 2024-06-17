from tkinter import *
from random import *
x=[0,0]
domain_,range_ = 100,10;#range of devident and divident
points_ = 0;#no. of correct answers
i = -1;#no. of questions given
root = Tk();#root window

Q_field = StringVar();
A_field = StringVar();
result_field = StringVar();
i_f = StringVar();
Q_field.set("Division Game");

def iscorrect(v1,v2):#check if ans is correct
    v1 = str(v1).lstrip().lower();
    v2 = str(v2).lstrip().lower();
    if (v1 == v2):#is correct
        result_field.set("Correct")
        return True;
    else:
        return False;

def summit(ans):#summit answer
    global points_;
    if Q_field.get() != "Division Game":
        b1['state'] = NORMAL;
        correct_ = False;
        try:#check for non-int values
            correct_ = iscorrect(get_A(),int(ans));
        except ValueError:#if non-int value
            Q_field.set("only enter integers");
        if correct_:#if ans is correct
            points_ += 1;
            result_field.set("Correct");
        else:
            result_field.set(f"Wrong answer is-- {get_A()}");
    else:
        next_();

def get_Q():#get question
    global x;
    while True:
        z_ = randint(1,domain_);
        y_ = randint(1,range_);
        if z_ % y_ == 0 and y_ != 1 and y_ < z_:
            x[0] = z_;
            x[1] = y_;
            break;
        else:
            continue;

def get_A():#get answer
    z_ = 0;
    try:
        z_ = x[0] // x[1];
    except ZeroDivisionError:
        next_();
    return z_;

def next_():# for next question
    global i;
    get_Q();
    Q_field.set(f"{x[0]} --divided by-- {x[1]}");
    if Q_field.get() != "Division Game":
        i += 1;
    i_f.set(f"{points_} correct out of {i}");
    A_field.set("");
    result_field.set("");
    b1['state'] = DISABLED;

def summit__(event):
    summit(A_field.get());

#ui-----
Label(root,textvariable=i_f).pack();#number label

f1 = Frame(root,relief="raised");
f1.pack();

Label(f1,textvariable=Q_field,font=("terminal",20,"bold")).pack(side="top",padx=10,pady=10);#question label

Entry(f1,textvariable=A_field,font=("terminal",15)).pack();#answer entry

Label(f1,textvariable=result_field).pack();#result label

Button(f1,text="SUMMIT",command=lambda: summit(A_field.get()),font=("calibri",10,"bold")).pack();#summit button

b1 = Button(root,text="NEXT",command=next_,font=("calibri",12,"bold"));#next button
b1.pack(pady=15);

#keyboard--

root.bind('<Return>',summit__);

root.mainloop();