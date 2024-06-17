a = int(input("enter number of questions-"));
marks = 0;
l = [];
def check_():
    global marks;
    for i in range(1,a+1):
        x = input(f"Q{i}-").lower()
        if x == l[i-1]:
            marks += 4;
        else:
            marks -= 1;
def ans_list():
    for i in range(1,a+1):
        x = input(f"A{i}-").lower();
        if x in ["a","b","c","d"]:
            l.append(x);
        else:
            print("error");
            ans_list();
            break;
ans_list();
check_();
print(marks);