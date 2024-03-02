
try:
    user_input = int(input("Fraction: "))
    if user_input == 1/4:
        print("25%")
        break
    elif user_input == 1/2:
        print("50")
            break
    elif user_input == 3/4:
        print("75%")
        break
    elif user_input == 4/4:
        print("F")
        break
    elif user_input == 0/1:
            print("E")
            break
        elif user_input.isalpha():
            raise ValueError
    except ValueError :
        print("ValueError")
    except ZeroDivisionError:
        print("ZeroDivisionError")
else:
    user_input = int(input("Fraction:"))

def fuel_fillup():
    user_input = int(input("fraction:" ))
    for fuel in user_input:
         if fuel not in [1/4,1/2,3/4,4/4,0/1]:
              user_input = int(input("Fraction:"))
        if user_input.isalpha() and user_input == decimal:
         raise ValueError




