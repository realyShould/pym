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

class QuadraticEquation(object):
    def __init__(self,a,b,c):
        self.a=a
        self.b=b
        self.c=c
    def dis(self,a,b,c):
        d=(b**2)-4*a*c 
        print(Fore.GREEN, 'D=',d)
        if d > 0:
            self.xF(a,b,c,d)
        elif d == 0:
            self.xF2(a,b,c,d)
        elif d < 0:
            print(Fore.RED,'No roots')
    def xF(self,a,b,c,d):
        x1=(-b-math.sqrt(d))/(a*2)
        x2=(-b+math.sqrt(d))/(a*2)
        print(Fore.GREEN, 'x1=',x1)
        print(Fore.GREEN, 'x2=',x2)
    def xF2(self,a,b,c,d):
        x=-((b)(2*a))
        print(Fore.GREEN, 'x=',x)

def squareRoot():
    try:
        print(Fore.RED)
        num = int(input('Enter number:'))
        ans=math.sqrt(num)
        print(Fore.GREEN,'Square root of ', num, ' is ' ,ans)
    except ZeroDivisionError:
        print(Fore.YELLOW,'Error with number')
        squareRoot()
calk = Calk(False)
quadraticEquation=QuadraticEquation(False,False,False)
print(Fore.MAGENTA)
print('\t\t█▀▀█ █░░█ █   █ Made by realyShould')
print('\t\t█░░█ █▄▄█ █▀▄▀█')
print('\t\t█▀▀▀ ▄▄▄█ █░░░█ for test')
def menu(): 
    print(Fore.RED)
    print('\tChoose')
    print(Fore.CYAN,'[1]Calk')
    print(Fore.CYAN,'[2]Quadratic Equation')
    print(Fore.CYAN,'[3]Square root of a number.')
    print(Fore.YELLOW,'[0]Exit')
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
        elif userInput == 2:
            a=int(input('a:'))
            b=int(input('b:'))
            c=int(input('c:'))
            quadraticEquation.dis(a,b,c)
            menu()
        elif userInput == 3:
            squareRoot()
            menu()
        elif userInput == 0:
            quit()
    except ValueError:
        print(Fore.YELLOW)
        print('\tOnly numbers')
        print(Style.RESET_ALL)
        menu()

menu()