def binary_search(sorted_l,s):
    mid_i,mid = len(sorted_l)//2,sorted_l[len(sorted_l)//2];
    while mid != s:
        if mid > s:
            sorted_l = sorted_l[::mid_i-1];
        elif mid < s:
            sorted_l = sorted_l[mid_i+1::];
        mid_i, mid = len(sorted_l) // 2, sorted_l[len(sorted_l) // 2];
    return mid_i;

print(binary_search([1,2,3,4,5,6,7,8,9],4));