def rectangle(length, width):
    def area():
        return length * width

    def perimeter():
        return 2 * (length + width)

    if not isinstance(width, int) or not isinstance(length, int):
        return "Enter valid values!"

    return f"""Rectangle area: {area()}
Rectangle perimeter: {perimeter()}"""

print(rectangle(2, 10))
print(rectangle('2', 10))


# -----------------------2 way--------------------------
def rectangle_area(args):
    return args[0] * args[1]


def rectangle_perimeter(args):
    return (args[0] + args[1]) * 2


def are_arguments_valid(args):
    for el in args:
        if not isinstance(el, int):
            return False
    return True


def rectangle(*args):
    if are_arguments_valid(args):
        return f'Rectangle area: {rectangle_area(args)}\nRectangle perimeter: {rectangle_perimeter(args)}'
    else:
        return 'Enter valid values!'

