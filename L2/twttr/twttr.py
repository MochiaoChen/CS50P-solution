input = input("Input: ")
output = ""


for c in input:
    if c in ["a", "e", "i", "o", "u"]:
        output += ""
    else:
        output += c


print("Output:",output)
