from random import randint
range_,domain_ = 20,100;
rounds_ = 10;
points_ = 0;

x = [0,0];

def set_Int():
    global x;
    while True:
        z_ = randint(1,domain_);
        y_ = randint(1,range_);
        if z_ % y_ == 0 and y_ != 1 and y_ < z_:
            x[0] = z_;
            x[1] = y_;
            break;
        else:
            continue;

def check_():
    z_ = x[0] // x[1];
    return z_;

def iscorrect(v1,v2):
    global points_;
    v1 = str(v1).lstrip().lower();
    v2 = str(v2).lstrip().lower();
    if (v1 == v2):
        print("Correct");
        points_ += 1;
    else:
        print("Wrong");
        print(f"ans is {v2}");

print(f"{rounds_} rounds");

for i in range(1,rounds_+1):
    set_Int();
    ans = check_();
    global points;
    print(f"{x[0]} --divided by-- {x[1]}");
    input_ = input("Ans--");
    iscorrect(input_,ans);

print(f"You got {points_} right out of {rounds_}");