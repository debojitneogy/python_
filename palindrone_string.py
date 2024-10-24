ini = str(input("enter word: "));
fin = "";
for i in ini:
    fin = i + fin;
if ini == fin:
    print(f"{ini} is palindrone");
else:
    print(f"{ini} is not palindrone");