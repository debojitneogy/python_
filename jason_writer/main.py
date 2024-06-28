def create_json(dict,name):
    with open(f"{name}.json","w") as file_:
        file_.write("{\n");
        for i in dict.keys():
            a = list(dict.keys());
            if i != a[-1]:
                file_.write(f'  "{i}": {dict[i]},\n');
            else:
                file_.write(f'  "{i}": {dict[i]}\n');
        file_.write("}");


def read_json(path):
    dict_ = {};
    f_dict = {};
    temp = "";
    with open(path,"r+") as file_:
        temp = file_.read();
    temp = temp[1:-2];
    temp = temp.split(",");
    for i in temp:
        t = i.strip();
        t = t.split(":");
        a = (t[0].strip());
        try:
            b = int(t[1].strip());
        except:
            b = t[1].strip();
        t = {a:b};
        dict_.update(t);
    for i in dict_.keys():
        a = str(i).replace('"','');
        try:
            b = int(dict_[i]);
        except:
            b = str(dict_[i]).replace('"', '');
        f_dict.update({a:b});
    return  f_dict;

def create_list_jason(dict_list,name):
    with open(f"{name}.json", "a") as file_:
        file_.write("{\n");
        file_.write(f' "{name}": [\n');
    for dict in dict_list:
        with open(f"{name}.json", "a") as file_:
            file_.write("    {\n");
            for i in dict.keys():
                a = list(dict.keys());
                b = dict[i];
                if isinstance(b,int):
                    if i != a[-1]:
                        file_.write(f'       "{i}": {b},\n');
                    else:
                        file_.write(f'       "{i}": {b}\n');
                else:
                    if i != a[-1]:
                        file_.write(f'       "{i}": "{b}",\n');
                    else:
                        file_.write(f'       "{i}": "{b}"\n');
            if dict != dict_list[-1]:
                file_.write("    },\n");
            else:
                file_.write("    }\n");
    with open(f"{name}.json", "a") as file_:
        file_.write(" ]\n}");

a = [
    {"abc":123,123:"abc"},
    {"abc":1123, 123:"abcc"},
    {"abc": 11233, 123: "abcec"}
];

create_list_jason(a,"sample");