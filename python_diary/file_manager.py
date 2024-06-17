import shelve
from page import page_class

notebook = "nootbook";
index_:dict = {};#index of all pages
page_no_list:list = list(index_.keys());#list of page numbers
page_no_list.append("0");

def new_page(name):# creates a new page
    global page_no_list;
    y = 0;
    try:
        y = int(max(page_no_list));
    except ValueError:
        y = 0;
    a = {f"{y+1}":page_class(name=name)};
    index_.update(a);
    page_no_list.append(f"{y+1}");
    page_no_list.sort();
    return f"{y+1}";

def write_page(page_no,text):#writes to a page
    page_no = str(page_no);
    if page_no in page_no_list:
        x:page_class = index_.get(page_no);
        x.save_txt(text=text);
        save_dict();
    else:
        print("page does not exist");

def open_page(page_no):
    page_no = str(page_no);
    load_dict();
    if page_no in page_no_list:
        a:page_class = index_.get(page_no);
        return a;
    else:
        print("page does not exist");

def delete_page(page_no):
    page_no = str(page_no);
    load_dict();
    if page_no in page_no_list:
        with shelve.open(notebook) as notebook_:
            notebook_.pop(page_no);
        index_.pop(page_no);
        load_dict();
    else:
        print("page does not exist");

def rename_page(page_no,new_name):
    page_no = str(page_no);
    new_name = str(new_name);
    load_dict();
    if page_no in page_no_list:
        c:page_class = index_.get(page_no);
        c.rename_(new_name_=new_name);
        a = {page_no:c};
        index_.update(a);
        save_dict();
    else:
        print("page does not exist");

def page_list():
    load_dict();
    update_page_no_list();
    a = {};
    for i in index_.keys():
        b:page_class = index_.get(i);
        a.update({i:b.name_});
    return a;

def save_dict():
    with shelve.open(notebook) as notebook_:
        notebook_.update(index_);

def load_dict():
    with shelve.open(notebook) as notebook_:
        index_.update(dict(notebook_));
        update_page_no_list();

def save_all():
    save_dict();

def update_page_no_list():
    global page_no_list;
    page_no_list = list(index_.keys());