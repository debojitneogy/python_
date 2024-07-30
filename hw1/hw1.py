#Read a file and count how many vowel,words,consonants, digits and special charecters.

vowel_c,cons_c,dig_c,special_c = 0,0,0,0;

def isvowel(value):
    vowels = "aeiou";
    if value in vowels:
        return  True;
    else:
        return False;

def isconsonant(value):
    vowels = "aeiou";
    if value not in vowels:
        return True;
    else:
        return False;

def isspecial(value):
    specials = "!@#$%^&*()_|{}]['?/>,<:;=+-";
    if value in specials:
        return True;
    else:
        return False;

wrd_ls = [];
with open("./examle.txt","r") as file_:
    a = file_.read();
    wrd_ls = (a.split(" "));

for i in wrd_ls:
    for j in i:
        if isvowel(j):
            vowel_c += 1;
        if isconsonant(j):
            cons_c += 1;
        if j.isdigit():
            dig_c += 1;
        if isspecial(j):
            special_c += 1;

print(f"words: {len(wrd_ls)}\n"
      f"vowels: {vowel_c}\n"
      f"consonants: {cons_c}\n"
      f"digits: {dig_c}\n"
      f"special charecters: {special_c}\n");