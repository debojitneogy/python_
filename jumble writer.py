import time

letters = ['A', 'B', 'C', 'D',
           'E', 'F', 'G', 'H',
           'I', 'J', 'K', 'L',
           'M', 'N', 'O', 'P',
           'Q', 'R', 'S', 'T',
           'U', 'V', 'W', 'X',
           'Y', 'Z',
           'a', 'b', 'c', 'd',
           'e', 'f', 'g', 'h',
           'i', 'j', 'k', 'l',
           'm', 'n', 'o', 'p',
           'q', 'r', 's', 't',
           'u', 'v', 'w', 'x',
           'y', 'z', ' ',
           '1', '2', '3', '4',
           '5', '6', '7', '8',
           '9', '0', '.', '_',
           '-',
           ]
a = str(input("enter sentence: "));
b = int(input('time to display: '));
c = (len(a)*b)/10000;
senten_ = "";
for i in a:
    for j in letters:
        temp = senten_ + j;
        print(f"\r{temp}",end="\r");
        time.sleep(c);
        if i == j:
            senten_ = senten_ + j;
            break;

print(senten_);