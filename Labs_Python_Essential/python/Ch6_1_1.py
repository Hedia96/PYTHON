#! /usr/bin/python3

'''
create an object from simple class in python
'''
"""
class SimpleClass:
    pass

obj_simple_class=SimpleClass()
"""
###########################################################
'''
create stack:
    __ private attribute can't be called from the class's user
    Methods in class take at least one paremeter self

'''
class Stack:
    def __init__(self):
        self.__stackList = []

    def push(self, val):
        self.__stackList.append(val)

    def pop(self):
        val = self.__stackList[-1]
        del self.__stackList[-1]
        return val


class ChildStack(Stack):
    test=0
    def __init__(self):
        # difference in assignment of variable (especially when we call them afterthat)depends on its type:
        #class var => access it as <<<Class_name.class var>>>
        #instance var=>          <<<self.instancevr>>>
        #local var in a method=>    var
         test=1
         self.test=3
         Stack.__init__(self)
         print("in local method",test)
         self.__sum=0
    def push(self,v):
        self.__sum+=v
        Stack.push(self,v)
        
    def pop(self):
        self.__sum-=v
        Stack.pop(self)
      # __sum is a private attribute so we need a method to make it available
      #for class 's user
    def GetSumOfStack(self):
        return self.__sum
        
stackObject = Stack()

mod_stack_obj=ChildStack()
print("in class var",ChildStack.test,"instance var",mod_stack_obj.test)
for index in range(4):
    mod_stack_obj.push(index)
    print(mod_stack_obj.GetSumOfStack())
    
print(stackObject.__dict__)
'''
stackObject.push(3)
stackObject.push(2)
stackObject.push(1)

print(stackObject.pop())
print(stackObject.pop())
print(stackObject.pop())
###########
littlestack=Stack()
anotherstack=Stack()
funnystack=Stack()

littlestack.push(1)
anotherstack.push(littlestack.pop()+1)
funnystack.push(anotherstack.pop()-2)
print(funnystack.pop())


'''

class ExampleClass:
    def __init__(self, val):
        if val % 2 != 0:
            self.a = 1
        else:
            self.b = 1

exampleObject = ExampleClass(1)
print(exampleObject.a)

print(hasattr(exampleObject,'b'))
try:
    print(exampleObject.b)
except AttributeError:
    pass
    #print("ther is no b attribute")
