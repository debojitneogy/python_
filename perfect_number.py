a = int(input("enter value:"));
b = 0;
for i in range(1,(a//2)+1):
    if a % i == 0:
        b += i;
if a == b:
    print("perfect number");
else:
    print("not perfect number");