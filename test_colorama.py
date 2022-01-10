import sys
from time import sleep
from colorama import init, Fore, Back, Style
init()

def tprint(words):
    for char in words:
        sleep(0.25)
        sys.stdout.write(char)
        sys.stdout.flush()

red_string = Fore.RED + "This is a red string\n" + Fore.RESET

tprint(red_string)

tprint(Fore.RED + "Hi there hhhhhh\n" + Fore.RESET)