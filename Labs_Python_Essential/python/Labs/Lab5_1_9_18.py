#! /usr/bin/pytohn3

"""
Module:mysplit function  as builtin python functions but using other function
Arguments: string
Return: list of words
"""

def mysplit(string):
    l=list(string)
    l_sp=['']
    ###l_sp=[]
    word=0
    #print(l)
    # for ch in string:
    #    print(ch)
    for index in range(len(l)):
        if(l[index]!=' '):
            #print(word,index)
            #print(l_sp)
            l_sp[word]+=l[index]
           ### l_sp.append(l[index])
        else:
             word+=1
             l_sp.append('')
            
    return l_sp                  




#mysplit("edv abs fd esq")

print(mysplit("To be or not to be, that is the question"))
print(mysplit("To be or not to be,that is the question"))
print(mysplit("   "))
print(mysplit(" abc "))
print(mysplit(""))

