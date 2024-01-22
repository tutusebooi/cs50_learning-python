user = input("File name: ").strip().lower()
if user.endswith("gif"):
    print("image/gif")
elif user.endswith("jpg"):
    print("image/jpg")
if user.endswith("jpeg"):
    print("image/jpeg")
elif user.endswith("png"):
    print("image/png")
elif user.endswith("pdf"):
    print("application/pdf")
