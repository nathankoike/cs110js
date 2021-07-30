"""
Lab 5 code
"""

# 1. The following are statements to consider regarding tuples. Type these
#    into your python3 interactive interpreter.
'''
x = 5
y = 9
p1 = (x, y)
print(p1)
print(("hi", "earth")) # Note: 2 pairs of parentheses
p2 = (x + 1, y - 1)
print(p2)
print(type(p2))
p1[0] = 3   # ERROR

somePairs = [(37, 'small'), (39, 'medium'),
             (42, 'large'), (44, 'xlarge')]
for pair in somePairs:
    print(pair[0], pair[1])

a, b = p1   # Using a tuple to assign multiple variables at once
print(a)
print(b)
'''


def main():
    """Use this function to test out code"""
    lists = []
    for _ in range(10):
        


def mystery(n):
    """n should be an integer"""
    result = []
    for i in range(n):
        result.append([])
        for j in range(n):
            result[-1].append((i, j))
    return result


def animals():
    print("tiger.", end="grr")
    print("cow.", end="moo")
    print("fox.")
    print("What does the fox say?")


def prints_something(last_number):
    """last_number should be an integer. Try integers
    greater than 50, and greater than 100."""
    for x in range(1, last_number + 1):
        x = str(x)
        for i in range(len(str(last_number))):
            if len(x) < len(str(last_number)):
                x = ' ' + x
        if int(x) % 10 == 0:
            print(x)
        else:
            print(x, end=" ")
    print()


def print_lists(lists):
    """Prints a list of lists"""
    for row in lists:
        print(row)


def works_with_lists():
    tenThings = list(range(10))
    lists = []
    for _ in range(8):
        lists.append(tenThings)

    print_lists(lists)

    print("------------------------------")
    lists[5][5] = 100
    print_lists(lists)


def also_works_with_lists():
    lists = []
    for _ in range(8):
        lists.append(list(range(10)))

    print_lists(lists)

    print("------------------------------")
    lists[5][5] = 100
    print_lists(lists)


def copy_list(things):
    """Copies a list of things into a new list of things."""
    result = []
    for thing in things:
        result.append(thing)
    return result


main()
