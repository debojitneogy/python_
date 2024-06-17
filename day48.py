import random;
print(f"press 1: for odd ");
print(f"press 2: for even");
choice = int(input("enter choice:"));
if choice == 1:
    a = 0;
    while True:
        b = random.randint(1,100);
        if b % 2 != 0:
            a = b;
            break;
    print(a);

elif choice == 2:
    a = 0;
    while True:
        b = random.randint(1,100);
        if b % 2 == 0:
            a = b;
            break;
    print(a);

else:
    print("invalid choice");