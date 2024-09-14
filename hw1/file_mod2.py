#f1=open("a.txt","x")
#f1.close();
f1=open("a.txt","a")
for i in range(0,5):
  c=input("enter the words:")+" ";
  f1.write(c)
f1.close();
f1=open("a.txt","r+");
d=f1.read();

c=0
for i in range(0,len(d)):
  if(d[i]==" "):
   c=c+1
   if(c==2):
    index=i+1;
f1.seek(index)
f1.write("apple");
f1.close()