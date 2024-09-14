file = input("enter file location: ");
f = open(file,"r+");
contents = f.read();
for i in range(len(contents)):
    if contents[i] == " ":
        f.seek(i);
        f.write("*");
f.close()