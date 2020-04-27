#module 4.1.6.13 project
'''
30-60 minutes

Level of difficulty
Medium/Hard

Objectives
perfecting the student's skills in using Python for solving complex problems,
integration of programming techniques in one program consisting of many various parts.
Scenario
Your task is to write a simple program which pretends to play tic-tac-toe with the user. To make it all easier for you, we've decided to simplify the game. Here are our assumptions:

the computer (i.e., your program) should play the game using 'X's;
the user (e.g., you) should play the game using 'O's;
the first move belongs to the computer - it always puts its first 'X' in the middle of the board;
all the squares are numbered row by row starting with 1 (see the example session below for reference)
the user inputs their move by entering the number of the square they choose - the number must be valid, i.e., it must be an integer, it must be greater than 0 and less than 10, and it cannot point to a field which is already occupied;
the program checks if the game is over - there are four possible verdicts: the game should continue, or the game ends with a tie, your win, or the computer's win;
the computer responds with its move and the check is repeated;
don't implement any form of artificial intelligence - a random field choice made by the computer is good enough for the game.
'''
'''
def fun(x):
    global y
    y=x*x
    return y
fun(2)
print(y)
'''
'''
dct={}
lst=['a','b','c','d']
for i in range(len(lst)-1):
    dct[lst[i]]=(lst[i],)
print(dct,lst)    
for i in sorted(dct.keys()):
    print(i)
    k=dct[i]
    print(k)
    print(k[0])
'''
'''
t=(1,2,3,4)
t=t[1:-1]
t=t[0]
#error t[0]=44
print(t)
'''
'''
def fu():
    print(var +1,end='')
var=1
fu()
print(var)

'''



'''
def fun(x):
    if x==0:
        return 0
    return x +fun(x-1)

print(fun(3))

'''
#########################3sumaary lab############
'''
def fun(x,y):
    if x==y:
        return x
    else:
        return fun(x,y-1)

print(fun(0,3))    


'''
'''
z=0
y=10
x=y<z and z>y or y>z and z<y
print(x)
'''
'''
listt=[x*x for x in range(5)]
del listt[listt[2]]

listt.insert(-1,listt[0])
print(listt)
'''


'''

dct={'one':'two','three':'one','two':'three'}
v=dct['three']
for k in range (len(dct)):
    v=dct[v]
print(v)


'''
'''
n=[1,2,3]
v=n
del v[:]
'''

'''
x=1
y=2
x,y,z=x,x,y
z,y,z=x,y,z
print(x,y,z)







l=[i for i in range(-1,-2)]
print(l)

'''
l=[[x for x in range(3)] for y in range(3)]
print(l)





















