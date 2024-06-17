def factorial(num):
    temp = 1;
    for i in range(1,num+1):
        temp = temp * i;
    return temp;

a = int(input("enter a number: "));
i = a;
b = 0;

while i > 0:
    c = i % 10;
    i = i // 10;
    c = factorial(c);
    b += c;

if a == b:
    print("is strong number");
else:
    print("is not strong number");