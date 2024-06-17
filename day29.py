def circle(radius):
    a = 3.14 * (radius**2);
    return a;

def triangle(side):
    a = 0.433 * (side**2);
    return a;

def rectangle(breadth,height):
    a = breadth * height;
    return a;

def square(side):
    a = side ** 2;
    return a;

print(circle(1));
print(triangle(2.236));
print(rectangle(2,2));
print(square(2));