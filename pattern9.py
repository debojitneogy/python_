for i in range(5):
    for k in range(i):
        print(" ",end='');
    for j in range(10-(i*2)):
        if j % 2 != 0:
            print("*",end='');
        else:
            print(" ",end='');
    print();
for i in range(3,-1,-1):
    for k in range(i):
        print(" ",end='');
    for j in range(10-(i*2)):
        if j % 2 != 0:
            print("*",end='');
        else:
            print(" ",end='');
    print();