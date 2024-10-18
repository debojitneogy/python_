def c_words():
    U,L = 0,0;
    f = open("words.txt","r");
    d = f.read().strip();
    f.close();
    for i in d:
        if i.isupper():
            U += 1;
        elif i.lower():
            L += 1;
    print(f"upper case- {U},lower case- {L}");

c_words();