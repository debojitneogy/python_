import mysql.connector

db = mysql.connector.connect(
    host = "localhost",
    user = "root",
    password = "123456789",
    port = "3306"
);

DbCursur = db.cursor();
#DbCursur.execute('create table db.student (name varchar(50), class varchar(5) , sec varchar(20) ,roll int(100) primary key,addres varchar(100));')
#db.commit()

def add_student(name,class_,roll,adress,sec):
    DbCursur.execute(f'insert into db.student value("{name}","{class_}","{sec}",{int(roll)},"{adress}");');
    db.commit();

#add_student('debojit','xi',1,'dubai','c')
def sel_view(a = "*"):
    DbCursur.execute(f'select {a} from db.student;');
    for i in DbCursur:
        print(i);


sel_view();