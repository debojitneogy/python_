class animal:
    count = 0;

    def __init__(self,name,age):
        self.name_ = name;
        self.age_ = age;
        animal.count += 1;

    @classmethod
    def get_count(cls):
        return animal.count;

lion = animal("lion",24);
cat = animal("cat",100);

print(animal.get_count());
