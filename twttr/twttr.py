

def translate(phrase):
    translate = ""
    for latter in phrase:
        if latter.lower() in "aeiou":
            translate = translate + ""
        else:
            translate = translate + latter
    return translate
print(translate(input("input: ")))
