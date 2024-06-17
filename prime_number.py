a = int(input("enter value: "));
b = bool;
for i in range(2,a):
    if a % i == 0:
        b = False;
        break;
    else:
        b = True;

if b:
    print("is prime");
else:
    print("not prime");