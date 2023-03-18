while True:
    a = float(input("input first number: "))

    operators = input("Please choice operator: +,-,/,*,^  ---->>> ")

    b = float(input("input second number: "))

    if operators == "+":
        print(a+b)
    elif operators == "-":
        print(a-b)
    elif operators == "/":
        if b !=0: # cannot divide by zero
            print(a/b)
    elif operators == "*":
        print(a*b)
    elif operators == "^":
        print(a**b)
    else:
        print("your choice incorrect")
        quit()
