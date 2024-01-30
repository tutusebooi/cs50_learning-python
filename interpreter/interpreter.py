def math_interpreter(expression):

    components = expression.split()

    x = float(components[0])
    operator = components[1]
    z = float(components[2])


    if operator == '+':
        result = x + z
    elif operator == '-':
        result = x - z
    elif operator == '*':
        result = x * z
    elif operator == '/':
        result = x / z


    print(f'Result: {result:.1f}')

user_input = input("Enter an arithmetic expression (e.g., 1 + 1): ")
math_interpreter(user_input)

