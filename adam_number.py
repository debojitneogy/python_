a,b = int(input("enter value: ")),0;
a_sq,b_sq = (a * a),0;
i = a;
while i > 0:
    b = (b * 10) + (i % 10);
    i = i // 10;
b_sq = b * b;
bsq_r,i = 0,b_sq;
while i > 0:
    bsq_r = (bsq_r * 10) + (i % 10);
    i = i // 10;
if a_sq == bsq_r:
    print("is adam number");
else:
    print("is not adam number");
