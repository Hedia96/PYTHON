'''
class A:
    A=1
    def __init__(self):
        self.a=0

class F(A):
    pass

class C(F):
    pass
class D(A,F):
    pass
#print(isinstance(C,A))
print(issubclass(C,A)and issubclass(D,A)and issubclass(D,F))
'''
'''
print(hasattr(A,'A'))        
'''
'''
#Q8
t=(1,)
t=t[0]+t[0]
print(t)

'''
'''
t=(1,2,3,4)
t=t[-2:-1]
t=t[-1]
print(t)
'''
#q10,13
'''
#x="""
#"""
x = "\"
print(len(x))
'''

'''
def fun(d,k,v):
    d[k]=v
    return d
    
dc={}
print(fun(dc,'1','v'))

'''

'''

d={}
d['2']=[1,2]
d['1']=[3,4]
for x in d.keys():
    print(d[x][1])
    


'''
'''
ls=[1,2,3,4]
ls=list(map(lambda x: 2*x,1))
print(ls)
'''

class T:
    def __init__(self,v):
        self._a=v+1


a=T(0)
print(a._a)
        






