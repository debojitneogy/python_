from multiprocessing import Process
def write_num(num):
    with open("a.txt","a") as f:
        for i in range(num):
            f.write(str(i*i));



if __name__ == "__main__":
    a = int(input("enter num: "));
    num = (a // 4);
    a = Process(target=write_num,args=(num,));
    b = Process(target=write_num,args=(num,));
    c = Process(target=write_num,args=(num,));
    d = Process(target=write_num,args=(num,));
    a.start();
    b.start();
    c.start();
    d.start();
    a.join();
    b.join();
    c.join();
    d.join();