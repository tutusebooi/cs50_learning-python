user = input("File name: ")
if user.endswith("gif"):
    print("image/gif")
if user.endswith("jpg"):
    print("image/jpg")
if user.endswith("jpeg"):
    print("image/jpeg")
elif user.endswith("png"):
    print("image/png")
elif user.endswith(""):
    print("")
