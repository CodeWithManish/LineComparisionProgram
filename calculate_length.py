import math


def calculate_length():
    """
    :return: length of the lines
    """
    print("Enter value of (x1, y1)")
    x1 = int(input())
    y1 = int(input())
    print("Enter value of (x2, y2)")
    x2 = int(input())
    y2 = int(input())

    length = math.sqrt(((x2 - x1) ** 2) + ((y2 - y1) ** 2))
    return length


if __name__ == '__main__':
    result = calculate_length()
    print("Length is: ", result)