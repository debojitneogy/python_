a = [1,1,22,33,22,33,44,55,66,77,22];
a.sort();

for i in a:
    b = a.count(i);
    if b > 1:
        for j in range(b):
            c = a.index(i) + j;
            a.pop(c)

print(a);