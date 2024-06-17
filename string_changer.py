a = input("value-");

def check_(val):
    if "ing" in a:
        return True;
    elif "ly" in a:
        return False;
    else:
        return True;

def set_(bool_,val):
    if bool_ == False:
        val = val[0:-3] + "ing";
    elif bool_ == True:
        val = val[0:-2] + "ly";
    return val;

if len(a) >= 3:
    print(set_(check_(a),a));
else:
    print("string too short");