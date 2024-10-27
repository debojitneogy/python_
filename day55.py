a = input("enter string: ");
V = [];
for i in a:
    if i in "aeiou":
        V.append(i);
print(sorted(V));