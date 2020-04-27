#!/usr/bin/python3

l_leds=["""###\n# #\n# #\n# #\n###""",
        "#\n#\n#\n#\n#",
        "###\n  #\n###\n#\n###""",
        "###\n  #\n###\n  #\n###",
        "# #\n# #\n###\n  #\n  #",
        "###\n#\n###\n  #\n###",
        "###\n#\n###\n# #\n###",
        "###\n  #\n  #\n  #\n  #\n  #\n",
        "###\n# #\n###\n# #\n###",
        "###\n# #\n###\n  #\n###"      
        
        ]

def Fun(num):
    '''
    for i in range(len(l_leds)):
        print()
        print(l_leds[i])
'''
    l_digits=[]
    while(num>0):
        l_digits.append(num%10)        
        num=num//10 ## it is important because get it as float and get the list 's length
        #much more than expecteds
       # print(num)        
     #   l_digits.reverse()
    for index in range(len(l_digits)):
       
        print(l_leds[l_digits[len(l_digits)-1-index]],   end=" ")
        
Fun(9053)
