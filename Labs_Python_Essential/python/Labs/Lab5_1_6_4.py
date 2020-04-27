#module 5
'''
userip=(input())
convert=int(userip)
print(type(convert))

print(type(userip))
'''
def readint(prompt, min, max):
    var =None
    try:
         var=int(input(prompt))     
    except ValueError:
        print("Error: wrong input")
    try:
        (var<=max and var>=min)
    except:
        print("Error: the value is not within permitted range (min..max)")
    return var    
#
# put your code here
#1

userip=input()
print("\n")
v=readint(userip,-10,10)
print("The number is:", v)
