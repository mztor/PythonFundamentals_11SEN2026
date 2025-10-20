def convert(val):
    new = val.replace(":)", "🙂")
    new = new.replace(":(", "🙁")
    return new


def main():
    sentence = input("What's your sentence? ")
    print(convert(sentence))


main()
