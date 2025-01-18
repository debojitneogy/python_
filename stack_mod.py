class stack():
    list_ = []
    overflow = 0
    tops = -1
    def __init__(self,overflow):
        self.overflow = overflow
    def push(self,element):
        if len(self.list_) < self.overflow:
            self.list_.append(element)
            self.tops += 1
        else:
            raise OverflowError("stack already full")
    def pop_(self):
        if len(self.list_) > 0:
            a = self.list_.pop()
            self.tops -= 1
            return a

        else:
            raise OverflowError("stack is empty")
    def peek(self):
        if len(self.list_) == 0:
            return None
        else:
            return self.list_[-1]