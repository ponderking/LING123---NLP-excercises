
var1 = "eple"
var2 = "eple"


if var1 == var2:
    print("Both words are identical")


if len(var1) > len(var2):
    print("First words is longer")
elif len(var1) < len(var2):
    print("Second word is longer")
else:
    print("The words have the same length")


if var1 > var2:
    print("VAR1 follows VAR2 alphabetically")

elif var1 < var2:
    print("VAR1 precedes VAR2 alphabetically")
else:
    print("Both words have the same alphabetical position")

