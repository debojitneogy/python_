a = int(input("enter value"));
pre,post = 0,1;
print(pre);
print(post);
for i in range(a):
    f = pre + post;
    pre = post;
    post = f;
    print(f);