class queue():
    que = [];
    size = 0;
    f,r = -1,-1;
    def __init__(self,size):
        self.size = size;

    def enqueue(self,obj):
        if len(self.que) < self.size:
            self.que.append(obj);
            if self.f == -1 and self.r == -1:
                self.f += 1;
                self.r += 1;
            else:
                self.r += 1;
        else:
            print("Overflow error");

    def dequeue(self):
        if len(self.que) > 0:
            return self.que.pop(0);
            if self.f == 0 and self.r == 0:
                f -= 1;
                r -= 1;
            else:
                r -= 1;
        else:
            print("underflow error");

    def front(self):
        return (self.que[0]);

    def rear(self):
        return (self.que[-1]);