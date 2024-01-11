def main():
    user_input()

def user_input():
    user = input("enter: ")
    if user == "Goodbye :(" :
        x = user.replace(":(" , "🙁")
        print(x)

    if user == "Hello :)":
        x = user.replace(":)", "🙂")
        print(x)

if __name__ == "__main__":
    main()




