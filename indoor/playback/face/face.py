def main():
    user_input()

def user_input():
    user = input("enter: ")
    if user == "Goodbye :( ":
        return "Goodbye 🙁"
    elif user == "Hello :)":
        return "Hello 🙂"
    else:
        return "Hello🙂 Goodbye🙁"

main()




