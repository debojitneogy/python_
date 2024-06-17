for i in range(3):
    for j in range(1,7):
        if j == 3-i:
            print("*",end="");
        else:
            print(" ",end="");
        if j == 3+i:
            print("*",end="");
    print();

for i in range(2,-1,-1):
    for j in range(1,7):
        if j == 3-i:
            print("*",end="");
        else:
            print(" ",end="");
        if j == 3+i:
            print("*",end="");
    print();