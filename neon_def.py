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
        print("is neon");
    else:
        print("is not neon");

display(calneon(int(input("enter value-"))));