initial = int(input("enter value: "));
final = int(0);
temp = initial;
while temp > 0:
    a = int(temp % 10);
    temp = int(temp / 10);
    final = (final * 10) + a;
if final == initial:
    print("is palindrone");
else:
    print("is not palindrone");