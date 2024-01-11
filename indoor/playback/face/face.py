def main():
    user_input()

def user_input():
    user = input("enter: ")
    if user == "Goodbye :( ":
        print("Goodbye 🙁")
    elif user == "Hello :)":
        return "Hello 🙂"
    else:
        return "Hello🙂 Goodbye🙁"

if__name__ == "__main__":
    main()




