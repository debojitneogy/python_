W = input("enter word: ");
N = int(input("enter position: "));
def place(W,N):
    out = "";
    for i in range(1,len(W)+1):
        if i%N == 0 :
            out += "_";
        else:
            out += W[i - 1];
    return out;

print(place(W,N));