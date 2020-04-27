# main2.py

#from module import suml, prodl
from sys import path
path.append('C:\\Users\\AyetAllah\\Desktop\\NTI_SC\\python\\package')
import extra.iota
print(extra.iota.FunI())
import extra.good.alpha

print(extra.good.alpha.FunA())

import extra.good.best.sigma 
print(extra.good.best.sigma.FunS())
print("in main:",__name__)


'''
from sys import path
path.append ('C:\\Users\\AyetAllah\\Desktop\\NTI_SC\\python\\package')
import extra.good.best.sigma 
print(extra.good.best.sigma.FunS())
'''
'''
try:
    x = int(input("Enter a number: "))
    y = 1 / x
    print(y)
except ZeroDivisionError:
    print("You cannot divide by zero, sorry.")
except ValueError:
    print("You must enter an integer value.")
except:
    print("Oh dear, something went wrong...")

print("THE END.")
'''
