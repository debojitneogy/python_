import mysql.connector

db = mysql.connector.connect(
    host = "localhost",
    user = "root",
    password = "root",
    port = "3306"
);

DbCursur = db.cursor();

def enter_student(fname,lname,roll,class_):
    DbCursur.execute(f'insert into db.students (fname,lname,roll,class) values ("{fname.title()}","{lname.title()}",{int(roll)},{int(class_)});');
    db.commit();

def show_students():
    DbCursur.execute("select class,roll,fname,lname from db.students;");
    for i in DbCursur:
        print(f"class:{i[0]} | roll:{i[1]} | name:{i[2]} {i[3]}.");

def enter_book(book_name):
    DbCursur.execute(f'insert into db.inventory (bname,available) values ("{book_name}",1);');
    db.commit();

def mark_availability(book_name,int_):
    DbCursur.execute(f'update db.inventory set available = {int_} where bname like "%{book_name}%";');
    db.commit();

def show_books():
    DbCursur.execute("select bname, available from db.inventory;");
    for i in DbCursur:
        print(f'book name:{i[0]} | availability:{"true" if i[1] == 1 else "false"}');

def place_order(std_roll,book):
    bookid = f'select book_id from db.inventory where bname like "%{book}%"';
    std_id = f'select std_id from db.students where roll = {int(std_roll)}';
    DbCursur.execute(f'insert into db.orders (book_id,std_id,issue_date) values (({bookid}),({std_id}),now());');
    mark_availability(book,0);
    db.commit();

def show_orders():
    DbCursur.execute("select book_id,std_id,issue_date from db.orders;");
    for i in DbCursur:
        print(f'book id:{i[0]} | student id:{i[1]} | issue date:{i[2]}');

a = int(input("1-student||2-inventory||3-oders:"));
match a:
    case 1:
        b = int(input("1-enter a student||2-get student list:"));
        match b:
            case 1:
                fname = input("enter first name: ");
                lname = input("enter last name: ");
                roll = int(input("enter roll number: "));
                class_ = int(input("enter class number: "));
                enter_student(fname,lname,roll,class_);
            case 2:
                show_students();
    case 2:
        b = int(input("1-enter a book||2-get book list:"));
        match b:
            case 1:
                bname = input("enter book name: ");
                enter_book(bname);
            case 2:
                show_books();
    case 3:
        b = int(input("1-register3 a order||2-get order list:"));
        match b:
            case 1:
                roll = input("enter student roll number: ");
                book = input("enter book name: ")
                place_order(roll,book);
            case 2:
                show_orders();