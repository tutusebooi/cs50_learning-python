def main():
    plate = input("Plate: ")
    if is_valid(plate):
        print("Valid")
    else:
        print("Invalid")


def is_valid(s):
    for s in plates:
        if s[0:].isalpha() and s[-1].isdigit()


main()
