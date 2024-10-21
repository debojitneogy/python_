class DisClass():
    def display(self):
        for i in range(1,6):
            for j in range(1,i+1):
                print(j,end="");
            print();
    def sqrt_display(self,n):
        while n > 0:
            a = n%10;
            n //= 10;
            print(a**(0.5));
ob = DisClass();
ob.display();
ob.sqrt_display(4329);