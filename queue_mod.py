class queue():
    que = [];
    size = 0;
    def queue(self,size):
        self.size = size;

    def enqueue(self,obj):
        if len(self.que) < self.size:
            self.que.append(obj);
        else:
            print("Overflow error");

    def dequeue(self):
        if len(self.que) > 0:
            return self.que.pop(0);
        else:
            print("underflow error");

    def front(self):
        return (self.que[0]);

    def rear(self):
        return (self.que[-1]);