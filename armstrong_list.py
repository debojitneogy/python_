def power_to(value,power):
    qf = value ** power;
    return qf;

def isarmstrong_(initial_val ):
    temp_val = initial_val;
    final_val = 0;
    while temp_val > 0:
        a = temp_val % 10;
        temp_val = temp_val // 10;
        final_val += power_to(a,len(str(initial_val)));
    
    if(initial_val == final_val):
        return final_val
    else:
        return 0;

output_list = [];

list_len = int(input("enter list length: "));
for i in range(1,list_len + 1):
    x = isarmstrong_(i);
    if x != 0:
        output_list.append(x);

print(output_list);