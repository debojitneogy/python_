vowel = ["a","e","i","o","u"];
v,c,s,n = 0,0,0,0;
a = str(input("enter value: "));

def check(value):
    x = str(value).lower();
    global v;
    global c;
    global s;
    global n;
    if x.isalpha():
        if x in vowel:
            v += 1;
        else:
            c += 1;
    elif x.isdigit():
        n += 1;
    else:
        s += 1;

for i in a:
    check(i);

print(f"vowel = {v}");
print(f"consonants = {c}");
print(f"number = {n}");
print(f"special charecter = {s}");
