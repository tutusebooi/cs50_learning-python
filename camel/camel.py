def camel_to_snake(variable_name):
    snake_case_name = ''
    for char in variable_name:
        if char.isupper():
            snake_case_name += '_' + char.lower()
        else:
            snake_case_name += char
    return snake_case_name.lstrip('_')

def main():
    camel_case_name = input("Enter a variable name in camel case: ")
    snake_case_name = camel_to_snake(camel_case_name)
    print("Snake case name:", snake_case_name)

if __name__ == "__main__":
    main()
