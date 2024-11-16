def palindrone_check(initial):
    final = int(0);
    temp = initial;
    while temp > 0:
        a = int(temp % 10);
        temp = int(temp / 10);
        final = (final * 10) + a;
    if final == initial:
        return True;
    else:
        return False;

def power_to(value,power):
    qf = value ** power;
    return qf;
def isarmstrong_(initial_val):
    temp_val = initial_val;
    final_val = 0;
    while temp_val > 0:
        a = temp_val % 10;
        temp_val = temp_val // 10;
        final_val += power_to(a, len(str(initial_val)));

    if (initial_val == final_val):
        return True
    else:
        return False;

def calneon(num):
    i = num**2;
    cnum = 0;
    while i>0:
        k = i%10;
        i = i//10;
        cnum += k;
    return (num,cnum);

def display(nums):
    if (nums[1]) == nums[0]:
        return True;
    else:
        return False;
def isneon(n):
    return display(calneon(int(n)));

a = (1,2,3,4,5,6,7,8,9,12,11,68,98,66);
nc,ac,pc = 0,0,0;
for i in a:
    if isneon(i):
        nc += 1;
    if isarmstrong_(i):
        ac += 1;
    if palindrone_check(i):
        pc += 1;
print(f"palindrone-{pc},armstrong-{ac},neon-{pc}");