

def user_input():
    user = input("enter: ")
    '''if user == "Goodbye :( ":
        return "Goodbye 🙁"
    elif user == "Hello :)":
        return "Hello 🙂"
    else:
        return "Hello🙂 Goodbye🙁"'''

    if user == "Hello :)":
        x = user.replace(":)", "🙂")
        return x
print(user_input())





