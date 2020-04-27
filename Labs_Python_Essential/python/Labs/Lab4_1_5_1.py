#create  BMI
'''
BMI=weightin Kg/(height in meters)2



'''
def getBmi(weight=0.0,height=1.0):
    #make sure the donmenitor down;t equal zero to be a valid division
    if(height==0.0):
        return None
    else:
        return weight/(height)**2
    

print(getBmi(2+1,1))

lis=[1,2,3]
def lis(g):
    del lis[2]
    
print(lis(lis))
