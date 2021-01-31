import math
import random
import colorama
from colorama import Fore, Style, Back
class Calk(object):
    def __init__(self, somethink):
        self.somethink=somethink
    def productOfNumbers(self,a,b):
        try:
            c=a*b
            print(Fore.GREEN)
            print('Answer:',c)
        except ZeroDivisionError:
            print(Fore.YELLOW)
            print('\tChoose other numbers')

calk = Calk(False)
            
def menu():
    print(Fore.MAGENTA)
    print('\t\t█▀▀█ █░░█ █   █ Made by realyShould')
    print('\t\t█░░█ █▄▄█ █▀▄▀█')
    print('\t\t█▀▀▀ ▄▄▄█ █░░░█ for test')
    print(Fore.RED)
    print('\tChoose')
    print(Fore.CYAN,'[1]Calk')
    print(Fore.RED)
    try:
        
        userInput = int(input('input:'))
        if userInput == 1:
            first = int(input('A:'))
            action = input('Action:')
            second = int(input('B:'))
            if action == '*':
                calk.productOfNumbers(first,second)
                menu()

    except ValueError:
        print(Back.RED, Fore.YELLOW)
        print('\tOnly numbers')
        print(Style.RESET_ALL)
        menu()

menu()