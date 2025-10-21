def main():
    dollars = dollars_to_float(input("How much was the meal? "))
    percent = percent_to_float(input("What percentage would you like to tip? "))
    tip = dollars * percent
    print(f"Leave ${tip:.2f}")


def dollars_to_float(d):
    # ignore dollar sign, convert cost to float and return it
    converted = float(d[1:])
    print(converted)
    return converted


def percent_to_float(p):
    # ignore the percent sign, convert to percentage value and return
    converted = float(p[:-1]) / 100
    print(converted)
    return converted


main()
