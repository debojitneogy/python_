def palindrone_check(initial):
    final = int(0);
    temp = initial;
    while temp > 0:
        a = int(temp % 10);
        temp = int(temp / 10);
        final = (final * 10) + a;
    if final == initial:
        return final;
    else:
        return 0;

final_list = [];
list_len = int(input("enter list length: "));
for i in range(1,list_len + 1):
    x = palindrone_check(i);
    if x != 0:
        final_list.append(x);

print(final_list);