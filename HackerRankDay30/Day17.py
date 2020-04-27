#!/usr/bin/python3

#######################################################################################################
# the challenge is about exception                                                                         
# method of power should take non-negative numbers otherwise,
# it raises an exception
#
#
##############################################################################

class Calculator():
    def __init__(self):
        pass
    # power_methd  has a specific feature to throw the excption if
    #the arguments aren't positive values and show a message:
    #(n and p shoould be non-negative )
    def Power_method(self,base,power):
        if base<0 or power<0:
            raise Exception("n and p should be non-negative")
        return int(pow(base,power))
        


obj=Calculator()

T=int(input())
for i in range(T):
    n,p = map(int, input().split())
    try:
        ans=obj.Power_method(n,p)
        print(ans)
    except Exception as e:
        print(e) 
#print(Power_method(3,2))
