
x = input('what is the answer to the Great Question of Life, the Universe, and Everything? ')
y = x.strip()
if y == "42" or y == "forty-two" or y == "forty two".lower():
    print("Yes")
elif y == "FoRty TwO":
    print("Yes")
else:
    print("No")
