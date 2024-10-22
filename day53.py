def second(a,b,c):
    if (a>c and a<b) or (a<c and a>b):
        return a;
    elif (b>c and b<a) or (b<c and b>a):
        return b;
    elif (c>b and c<a) or (c<b and c>a):
        return c;

l = []
for i in range(1,4):
    try:
        a = int(input(f"enter {i} value: "));
    except:
        a = int(input("only enter int value: "));
    l.append(a);

print(second(l[0],l[1],l[2]));