user = input("File name: ").strip().lower()
if user.endswith("gif"):
    print("image/gif")
elif user.endswith("jpeg"):
   print("image/jpeg")
if user.endswith("jpg"):
    print("image/jpeg")
elif user.endswith("png"):
    print("image/png")
elif user.endswith("pdf"):
    print("application/pdf")
elif user.endswith("zip"):
    print("application/zip")
elif user.endswith("txt"):
    print("text/plain")
elif user.endswith("bin"):
    print("application/octet-stream")
elif user.isalpha:
    print("application/octet-stream")
