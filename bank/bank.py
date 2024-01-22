
greeting = input("Greeting: ").lower().strip()

if greeting.startswith("hello"):
    print("$0")
elif greeting == "How you doing?":
    print("$20")
else:
    print("$100")

