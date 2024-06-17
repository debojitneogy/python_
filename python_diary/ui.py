from file_manager import *
from tkinter import *
from tkinter import messagebox
import time

main_window = Tk();
main_window.title("My Diary");
main_window.geometry("680x550");
main_window.iconphoto(True,PhotoImage(file="assets\\Book_and_Quill_JE1_BE1.png"));

########
cur_page:page_class = None;
cur_page_no = "";

def update_ui():
    global cur_page_no;
    if cur_page != None:
        load_dict();
        name_entry.set(cur_page.name_);
        text_entry.delete('0.0', END);
        text_entry.insert("0.0",cur_page.get_txt());
        time_.set(cur_page.date_);
        #cur_page_no = list(index_.keys())[list(index_.values()).index(cur_page)];
        #print(index_);
        cur_indicator_en.set(f"Editing - {cur_page.name_}");
    else:
        name_entry.set("");
        text_entry.delete('1.0', END);
        cur_indicator_en.set(f"Writing - New");

def save_but():
    global cur_page;
    global cur_page_no;
    load_dict();
    if cur_page == None:
        if name_entry.get() != "":
            a = new_page(name=name_entry.get());
        else:
            a = new_page(name="Untitled");
        write_page(a,text_entry.get("1.0",END));
        save_all();
        cur_page = index_.get(a);
        update_ui();
    else:
        write_page(cur_page_no,text_entry.get("1.0",END));
        rename_page(cur_page_no,name_entry.get());
        save_all();
        #update_ui();

def Open_but(index_no):
    global cur_page;
    global cur_page_no;
    load_dict();
    cur_page = index_.get(str(index_no));
    cur_page_no = index_no;
    update_ui();

def list_but():
    key_ = "";
    load_dict();
    list_window = Toplevel();
    list_window.title("Select page");
    list_window.geometry("200x300");
    scroll_ = Scrollbar(list_window);
    Button(list_window,text="Open",command=lambda: Open_but(list_.curselection()[0]+1)).pack(anchor="nw");
    scroll_.pack(side=RIGHT,fill=Y);
    list_ = Listbox(list_window);
    list_.pack(fill=BOTH,expand=TRUE);
    for k in index_.keys():
        c:page_class = index_.get(k);
        list_.insert(int(k),str(f"{k}-{c.name_}   ({c.date_})"));
    list_.config(height=list_.size(),yscrollcommand=scroll_.set);
    scroll_.config(command=list_.yview);

def new_but():
    global cur_page;
    global cur_page_no;
    cur_page_no = None;
    cur_page = None;
    update_ui();

def on_closing():
    if messagebox.askyesno(title="Save?",message="Save before closing"):
        save_but();
    else:
        main_window.quit();

########
menu_frame = Frame(main_window);
Button(menu_frame,text="New",width=7,command=new_but).grid(row=0,column=0,padx=5);
Button(menu_frame,text="Save",width=7,command=save_but).grid(row=0,column=1,padx=5);
Button(menu_frame,text="Open",width=7,command=list_but).grid(row=0,column=2,padx=5);
menu_frame.pack(anchor="nw",padx=10,pady=10);

cur_indicator_en = StringVar();
cur_indicator_en.set(f"Writing - New");
Label(main_window,textvariable=cur_indicator_en).pack(anchor="ne",padx=20,pady=5);

name_entry = StringVar();
time_ = StringVar();
time_.set(time.ctime(time.time()));
name_frame = Frame(main_window);
Label(name_frame,text="Name-").pack(anchor="nw",pady=10);
Entry(name_frame,textvariable=name_entry,width=(50)).pack(side=LEFT);
Label(name_frame,textvariable=time_).pack(side=LEFT,padx=40);
name_frame.pack(padx=15,pady=5,anchor="nw");

text_entry = StringVar();
entry_frame = Frame(main_window);
Label(entry_frame,text="Entry-").pack(anchor="nw");
text_entry = Text(entry_frame);
text_entry.pack();
entry_frame.pack(padx=15,pady=5,anchor="nw");

main_window.protocol("WM_DELETE_WINDOW", on_closing);

main_window.mainloop();