from random import randint

lbound, ubound = int(input("enter lower bound-")), int(input("enter upper bound-"));

number_ = randint(lbound,ubound);
did_guess = False;
print("you only have 7 chances to guess the integer");

for i in range(7):
    try:
        a = int(input("enter guess-"));
    except ValueError:
        print("only integers");
        a = int(input("enter guess-"));
    if a > number_:
        print("too high");
    elif a < number_:
        print("too low");
    elif a == number_:
        did_guess = True;
        break;

if did_guess == False:
    print("you failed to guess the number");
elif did_guess:
    print("you have correctly guessed the number");