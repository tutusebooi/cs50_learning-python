def main():
    user_input()

def user_input():
    user = input("enter: ")
    if user == "Goodbye :(" :
        x = user.replace(":(" , "🙁")
        print(x)

    elif user == "Hello :)":
        x = user.replace(":)", "🙂")
        print(x)
    else:
        print("Hello🙂 Goodbye🙁")

if __name__ == "__main__":
    main()




