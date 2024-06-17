l = [1,2,1,2,6,5,4,8,2,3,4,1,2,3,5];
count_ = [];
for i in l:
    count_.append(l.count(i));
max_ = max(count_);
for i in l:
    if l.count(i) == max_:
        print(f"The element {i} has the most frequency of {max_}");
        break;