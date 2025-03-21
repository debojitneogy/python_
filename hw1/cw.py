import csv
def read_csv(N):
    f = open(f"{N}.csv","r");
    c = csv.reader(f);
    l = [i for i in c];
    return l;

def new_csv(c,N):
    try:
        f = open(f"{N}.csv","a");
    except:
        with open(f"{N}.csv","x"):
            pass;
        f = open(f"{N}.csv","a");
    C = csv.writer(f,delimiter=":");
    C.writerows(c);
    f.close();

new_csv(read_csv("a"),"b");