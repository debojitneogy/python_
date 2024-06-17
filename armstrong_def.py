def input_():
    anum = int(input("enter value-"));
    return anum;

def arm_calculate(anum):
    rem = anum;
    cnum =0;
    while rem>0:
        k = rem%10;
        rem = rem//10;
        cnum += k**(len(str(anum)));
    return (anum,cnum);

def display(inputs):
    if inputs[0] == inputs[1]:
        print("armstrong number");
    else:
        print("not armstrong number");

display(arm_calculate(input_()));