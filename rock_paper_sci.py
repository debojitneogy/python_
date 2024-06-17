import random
score_AI = int();
score_p = int();
items_L = ["ROCK","PAPER","SCISSORS"];

def announce(win,a_,x_):
    global score_p
    global score_AI
    print(f"player {win}s with {a_} against {x_}");
    if win == "WIN":
        score_p += 1;
    elif win == "LOOSE":
        score_AI += 1;

print("Best of 5 rounds");
print("0-ROCK,1-PAPER,2-SCISSORS");
for i in range(5):
    try:
        a = items_L[int(input("enter value: "))];
    except IndexError:
        print("enter with in 0-2");
    except ValueError:
        print("enter numbers only")
        continue;
    x = items_L[random.randint(0,2)];
    if a == "ROCK":
        if x == "ROCK":
            announce("DRAW",a,x);
        elif x == "PAPER":
            announce("LOOSE",a,x);
        elif x == "SCISSORS":
            announce("WIN",a,x);
    elif a == "PAPER":
        if x == "ROCK":
            announce("WIN",a,x);
        elif x == "PAPER":
            announce("DRAW",a,x);
        elif x == "SCISSORS":
            announce("LOOSE",a,x);
    elif a == "SCISSORS":
        if x == "ROCK":
            announce("LOOSE",a,x);
        elif x == "PAPER":
            announce("WIN",a,x);
        elif x == "SCISSORS":
            announce("DRAW",a,x);

if score_p > score_AI:
    print(f"player wins with {score_p} score against AI {score_AI} score");
elif score_p < score_AI:
    print(f"player looses with {score_p} score against AI {score_AI} score");
elif score_p == score_AI:
    print(f"player draws with {score_p} score against AI {score_AI} score");