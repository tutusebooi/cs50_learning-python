
greeting = input("Greeting: ").lower().strip()

if greeting.startswith("hello"):
    print("$0")
elif greeting == "Howyoudoing?":
    print("$20")
elif greeting == "What's happening?":
    print("$100")

