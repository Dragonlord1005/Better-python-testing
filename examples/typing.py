import sys

from time import sleep

words = "This is just a test :P\n"
for char in words:
    sleep(0.2)
    sys.stdout.write(char)
    sys.stdout.flush()
