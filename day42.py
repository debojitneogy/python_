a = int(input("enter value-"));
def REVERSAR(Number):
    num = '';
    while Number >= 1:
        num += str(Number % 10);
        Number //= 10;
    return num;

print(REVERSAR(a));