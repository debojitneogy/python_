def HowMany(Id,Val):
    c = 0;
    for i in Id:
        if i == Val:
            c += 1;
    return c;

a = [115,122,137,110,122,113];
print(HowMany(a,122));