from pyfiglet import Figlet
import random
import sys

figlet = Figlet()

fonts = figlet.getFonts()

if len(sys.argv) == 1:
    f = random.choice(fonts)
elif len(sys.argv) == 3:
    if sys.argv[1] in ["-f", "--font"] and sys.argv[2] in fonts:
        f = sys.argv[2]
    else:
        sys.exit("Invalid arguments.")
else:
    sys.exit("Invalid number of arguments.")

text = input("Input: ")
figlet.setFont(font = f)
print("Output:\n", figlet.renderText(text))
