def calculator():
    num1 = float(input("Select the first numb: "))
    while True:
        operator = input("Type the operator (+, -, *, /): ")

        if operator == 'exit':
            print("Exiting calculator.")
            break

        num2 = float(input("Select the second num: "))

        if operator == '+':
            num1 += num2
        elif operator == '-':
            num1 -= num2
        elif operator == '*':
            num1 *= num2
        elif operator == '/':
             if num2 != 0:
                num1 /= num2
             else:
                print("ERROR")
                continue
        else:
            print("ERROR: Wrong operator")
            continue
        print(f"Current result: {num1}")

calculator()