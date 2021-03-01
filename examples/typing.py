import time
import sys


words = "This is just a test :P\n"
for char in words:
    sleep(0.2)
    sys.stdout.write(char)
    sys.stdout.flush()



def typingPrint(text):
    for character in text:
        sys.stdout.write(character)
        sys.stdout.flush()
        time.sleep(0.05)


def typingInput(text):
    for character in text:
        sys.stdout.write(character)
        sys.stdout.flush()
        time.sleep(0.05)
    value = input()
    return value
