
greeting = input("Greeting: ").lower().strip()

if greeting.startswith("hello"):
    print("$0")
elif greeting.startswith("how you doing?"):
    print("$20")
elif greeting == "What's happening?":
    print("$100")
else:
    print("$100")
