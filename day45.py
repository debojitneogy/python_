def  INDEX_LIST(L):
    r = [];
    for i in range(len(L)):
        if int(L[i]) != 0:
           r.append(i);
    return r;

a = [12,4,0,11,0,6];
print(INDEX_LIST(a));  