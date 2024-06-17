def iscomposite(N):
    k = 0;
    while N > 1:
        for i in range(2,N+1):
            if N%i == 0:
                k += 1;
                N //= i;
        if k >= 2:
            return True;
            break;
        
a = int(input("enter value-"));
l = [];
for i in range(4,a+1):
    if iscomposite(i):
        l.append(i);

print(l);