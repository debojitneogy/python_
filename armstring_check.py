def power_to(value,power):
    qf = value ** power;
    return qf;

initial_val = int(input("enter value: "));
temp_val = initial_val;
final_val = 0;
while temp_val > 0:
    a = temp_val % 10;
    temp_val = temp_val // 10;
    final_val += power_to(a,len(str(initial_val)));

if(initial_val == final_val):
    print("armstrong number")
else:
    print("not armstrong number")