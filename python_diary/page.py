import time

class page_class:
    name_ = "";
    text_ = "";
    def __init__(self,name):
        self.date_ = time.ctime(time.time());
        self.name_ = name;
    
    def save_txt(self,text):
        self.text_ = text;
        self.modified_ = time.ctime(time.time());
    
    def get_txt(self):
        return self.text_;
    
    def rename_(self,new_name_):
        self.name_ = new_name_;