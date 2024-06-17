print("press 1: for pattern 1 || press 2: for pattern 2");
a = int(input("enter choice: "));

if a == 1:
    for i in range(3,0,-1):
        for j in range(i):
            print((j+1),end="");
        print();
elif a == 2:
    for i in range(3,0,-1):
        for j in range(i):
            print(i,end="");
        print();
else:
    print("invalid input");