def main():
    print(convert(input()))

def convert(s):
    s = s.replace(":)","🙂")
    s = s.replace(":(","🙁")

    return s



