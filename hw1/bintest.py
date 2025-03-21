import pickle

d1 = {"N":"debojit","age":11};
d2 = {"N":"dead","age":0};
L = [d1,d2];

f = open("a.dat","b+r");
c = pickle.load(f);
print(c);