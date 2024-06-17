a = int(input("enter value: "));
has_zero,i = False,a;
while i > 0:
    if i % 10 == 0:
        has_zero = True;
        break;
    i = i // 10;
if has_zero:
    print("duck number");
else:
    print("not duck number");