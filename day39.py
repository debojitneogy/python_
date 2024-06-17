def AddOddEven(*values):
    odd,even = 0,0;
    for i in values:
        if int(i) % 2 == 0:
            even += i;
        else:
            odd += i;
    return (odd,even);

a = AddOddEven(15,26,37,10,22,13);

print(f"sum of even- {a[1]}, sum of odd- {a[0]}");