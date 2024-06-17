def case_count(value):
    x = value
    if x.islower():
        return False;
    elif x.isupper():
        return True;

up_,low_ = 0,0;

input_ = input("enter string-");

for i in input_:
    b = case_count(i);
    if b:
        up_ += 1;
    elif b == False:
        low_ += 1;

print(f"{up_} upper letters, {low_} lower letters");