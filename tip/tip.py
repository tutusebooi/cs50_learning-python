def main():
    dollars = dollars_to_float(input("How much was the meal? "))
    percent = percent_to_float(input("What percentage would you like to tip? "))
    tip = dollars * percent
    print(f"Leave ${tip:.2f}")


def dollars_to_float(dollars):
    # TODO
    dollars = dollars.replace("$","")
    return float(dollars)


def percent_to_float(percent):
    # TODO
   #if "%" in percent:
        percent = percent.replace("%","")
        percent = int(percent) / 100
        return percent


main()

