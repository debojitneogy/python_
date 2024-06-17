def dis_two(L):    
    print(f"Sum of two digits: {L} = {sum(L)}");

def dis_one(L):    
    print(f"Sum of one digit: {L} = {sum(L)}");

def filter_digit(L):
    one,two = [],[];
    for i in L:
        if len(str(i)) > 1 and len(str(i)) < 3:
            two.append(i);
        else:
            one.append(i);
    dis_one(one);
    dis_two(two);

a = [2,12,4,9,18,25,3,32,20,1];
filter_digit(a);