import math


def check_equality():
    print("Enter Co-ordinates of A(x1,y1)")
    x1 = int(input())
    y1 = int(input())
    print("Enter Co-ordinates of B(x2,y2)")
    x2 = int(input())
    y2 = int(input())
    print("Enter Co-ordinates of C(x3,y3)")
    x3 = int(input())
    y3 = int(input())
    print("Enter Co-ordinates of D(x4,y4)")
    x4 = int(input())
    y4 = int(input())
    line1 = math.sqrt(((x2 - x1) ** 2) + ((y2 - y1) ** 2))
    line2 = math.sqrt(((x4 - x3) ** 2) + ((y4 - y3) ** 2))

    if line1 == line2:
        print("Both lines are equal")
    else:
        print("lines are not equal")


if __name__ == '__main__':
    check_equality()
