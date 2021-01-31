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
    def divisionOfNumbers(self,a,b):
        try:
            c=a/b
            print(Fore.GREEN)
            print('Answer:', c)
        except ZeroDivisionError:
            print(Fore.YELLOW)
            print('\tChoose other numbers')
    def additionOfNumbers(self,a,b):
        try:
            c=a+b
            print(Fore.GREEN)
            print('Answer:', c)
        except ZeroDivisionError:
            print(Fore.YELLOW)
            print('\tChoose other numbers')
    def subtractionOfNumbers(self,a,b):
        try:
            c=a-b
            print(Fore.GREEN)
            print('Answer:', c)
        except ZeroDivisionError:
            print(Fore.YELLOW)
            print('\tChoose other numbers')


calk = Calk(False)
print(Fore.MAGENTA)
print('\t\t█▀▀█ █░░█ █   █ Made by realyShould')
print('\t\t█░░█ █▄▄█ █▀▄▀█')
print('\t\t█▀▀▀ ▄▄▄█ █░░░█ for test')
def menu(): 
    print(Fore.RED)
    print('\tChoose')
    print(Fore.CYAN,'[1]Calk')
    print(Fore.MAGENTA)
    try:
        
        userInput = int(input('input:'))
        if userInput == 1:
            first = int(input('A:'))
            action = input('Action or q:')
            if action == 'q':
                menu()
            second = int(input('B:'))
            if action == '*':
                calk.productOfNumbers(first,second)
                menu()
            elif action == '/':
                calk.divisionOfNumbers(first,second)
                menu()
            elif action == '-':
                calk.subtractionOfNumbers(first,second)
                menu()
            elif action == '+':
                calk.additionOfNumbers(first,second)
                menu()
            else:
                print(Fore.YELLOW, 'Wrong action')
                menu()
        elif userInput == 0:
            quit()
    except ValueError:
        print(Fore.YELLOW)
        print('\tOnly numbers')
        print(Style.RESET_ALL)
        menu()

menu()