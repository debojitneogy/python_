def sort_list(sorted_list):
    list = sorted_list;
    for j in range(len(list)-1):
        for i in range(len(list)-1):
            if(list[i] > list[i+1]):
               a = list[i+1];
               list[i+1] = list[i];
               list[i] = a;
               #print(list);
    return list;


def isspecial_(input_,check):
    lbool = bool();
    for i in input_:
        if(str(i) == str(check)):
            lbool = True;
            break;
        else:
            lbool = False;
            continue;
    return lbool;    

print("press(.) to stop");

main_list = [];

while True:
    a = input("value: ");
    if(isspecial_(a,".") == True):
        break;
    else:
        main_list.append(a);
        continue;
    
print(sort_list(main_list),"final");