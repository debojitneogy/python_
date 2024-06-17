n = int(input("enter value-"));
prime_digit_sum = 0;
digit_sum = 0;
k = n;

for i in range(1,n):# check if factor
    is_prime = False;
    if n % i == 0:
        if i == 2:
            is_prime = True;
        for j in range(2,i):#check if prime factor
            if i % j != 0:
                is_prime = True;
            else:
                is_prime = False;
                break;
        if is_prime:
            m = i;
            while m > 0:# sum of digits of prime factor
                a = m % 10;
                m = m // 10;
                prime_digit_sum += a;

while k > 0:# sum of digits
    a = k % 10;
    k = k // 10;
    digit_sum += a;

if prime_digit_sum == digit_sum:
    print("Is smith number");
else:
    print("Is not smith number");