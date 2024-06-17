def Scroller(Lineup):
    Lineup.insert(0,Lineup[-1]);
    Lineup.pop(-1);
    return Lineup;

a =[25,30,90,110,16];
print(Scroller(a));