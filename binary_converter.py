a = int(input("enter decimal number: "));
def to_bin(value):
    bin_ = ""
    while value > 0:
        if value % 2 == 0:
            bin_ += "0";
            value //= 2;
        else:
            bin_ += "1";
            value = (value-1) // 2;
    bin_ = bin_[::-1];
    return bin_;

print(to_bin(a));