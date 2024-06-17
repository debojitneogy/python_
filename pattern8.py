for i in range(6):
    if i % 2 != 0:
        for j in range(65,(i+65)):
            print(chr(j),end='');
        print();
    else:
        for j in range(1,(i+1)):
            print(j,end='');
        print();