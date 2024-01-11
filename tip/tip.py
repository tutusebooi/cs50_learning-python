def main():
    dollars = dollars_to_float(input("How much was the meal? "))
    percent = percent_to_float(input("What percentage would you like to tip? "))
    tip = int(dollars) * float(percent)
    print(f"Leave ${tip:.2f}")


def dollars_to_float(dollars):
    # TODO
    return float(dollars)


def percent_to_float(percent):
    # TODO
    if "%" in percent:
        x = percent.replace("%","")
        x = (percent / 100)*dollar
        return x


main()

