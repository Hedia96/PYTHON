'''
import re

#create user-defined Exception,BadString is derived class from parent class Exception

class BadString(Exception):
    pass


while True:
    s = input()
   # obj=re.match(r'[a-z,0-9]',s)

    try:
        if(1<=len(s) and 6>=(len(s))):
            print("ok")
        else: # raise the exception you created 
            raise BadString
    except BadString:
        print("Bad String")
        #finally clauses execute whatever try, except block finds error or not
        #but when the block try,except exits 
        
    finally:
        print("Bye......")




#__name__='main'
'''
#sol:
'''
import sys

S = input().strip()

try:
    i = int(S)
    print(i)
except ValueError:
    print("Bad String")


,,,
