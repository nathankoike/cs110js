def function1():
    pass
    expr = input("Enter an expression: ")
    val = eval(expr)
    print(expr, "is", val, "with type", type(val).__name__)

def function2():
    pass
    print("  .   ")
    print(" / \  ")
    print("/   \ ")
    print("+---+ ")
    print("|   | ")
    print("+---+ ")

def function3():
    yards = int(input("Enter field length in yards: "))
    print("The field is ", yards * 36,  "inches long.")
if __name__ == "__main__":
    function3()
