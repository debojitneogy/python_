from tkinter import *
equation = "";
root_ = Tk();
root_.title("calculator");

#####
def enter_(value):
    global equation;
    global eq_field;
    equation += str(value);
    eq_field.set(equation);

def equal_():
    global equation;
    global eq_field;
    try:
        equation = str(eval(equation));
    except SyntaxError:
        equation = "error";
    eq_field.set(equation);

def clear():
    global equation;
    global eq_field;
    equation = "";
    eq_field.set(equation);

#####
eq_field = StringVar();
eq_field.set("000000");
Label(root_,textvariable=eq_field,height=2,font=("Terminal",20,"bold")).grid(row=0,column=0,columnspan=4);

#####
b1 = Button(root_,text="1",command=lambda: enter_("1"),height="4",width="9");
b1.grid(row=3,column=0);

b2 = Button(root_,text="2",command=lambda: enter_("2"),height="4",width="9");
b2.grid(row=3,column=1);

b3 = Button(root_,text="3",command=lambda: enter_("3"),height="4",width="9");
b3.grid(row=3,column=2);

b4 = Button(root_,text="4",command=lambda: enter_("4"),height="4",width="9");
b4.grid(row=2,column=0);

b5 = Button(root_,text="5",command=lambda: enter_("5"),height="4",width="9");
b5.grid(row=2,column=1);

b6 = Button(root_,text="6",command=lambda: enter_("6"),height="4",width="9");
b6.grid(row=2,column=2);

b7 = Button(root_,text="7",command=lambda: enter_("7"),height="4",width="9");
b7.grid(row=1,column=0);

b8 = Button(root_,text="8",command=lambda: enter_("8"),height="4",width="9");
b8.grid(row=1,column=1);

b9 = Button(root_,text="9",command=lambda: enter_("9"),height="4",width="9");
b9.grid(row=1,column=2);

b0 = Button(root_,text="0",command=lambda: enter_("0"),height="4",width="9");
b0.grid(row=4,column=0);

####
b_clear = Button(root_,text="<X",command=clear,height="3",width="7",font="bold");
b_clear.grid(row=4,column=1);

b_plus = Button(root_,text="+",command=lambda: enter_("+"),height="3",width="7",font="bold");
b_plus.grid(row=1,column=3);

b_subs = Button(root_,text="-",command=lambda: enter_("-"),height="3",width="7",font="bold");
b_subs.grid(row=2,column=3);

b_multyply = Button(root_,text="*",command=lambda: enter_("*"),height="3",width="7",font="bold");
b_multyply.grid(row=3,column=3);

b_division = Button(root_,text="/",command=lambda: enter_("/"),height="3",width="7",font="bold");
b_division.grid(row=4,column=3);

b_equal = Button(root_,text="=",command=equal_,height="3",width="7",font="bold");
b_equal.grid(row=4,column=2);
#####

def one(event):
    enter_("1");

def two(event):
    enter_("2");

def three(event):
    enter_("3");

def four(event):
    enter_("4");

def five(event):
    enter_("5");

def six(event):
    enter_("6");

def seven(event):
    enter_("7");

def eight(event):
    enter_("8");

def nine(event):
    enter_("9");

def plus(event):
    enter_("+");

def minus(event):
    enter_("-");

def multiply(event):
    enter_("*");

def divide(event):
    enter_("/");

def zero(event):
    enter_("0");

def decimal(event):
    enter_(".");

def equal__(event):
    equal_();

def clear__(event):
    clear();
####

root_.bind('1',one);
root_.bind('2',two);
root_.bind('3',three);
root_.bind('4',four);
root_.bind('5',five);
root_.bind('6',six);
root_.bind('7',seven);
root_.bind('8',eight);
root_.bind('9',nine);
root_.bind('<plus>',plus);
root_.bind('<minus>',minus);
root_.bind('<asterisk>',multiply);
root_.bind('<slash>',divide);
root_.bind('0',zero);
root_.bind('<Insert>',zero);
root_.bind('<Return>',equal__);
root_.bind('<period>',decimal);
root_.bind('<Delete>',decimal);
root_.bind('<BackSpace>',clear__);

root_.mainloop();