#!/bin/python3

#####################################################################################
# check if the word is aplaindorm or no by
# comparing the traverse the data from two different data container
#(stack , queue) by pop and dequeue ,if they are the same till the containers become
# empty , so the word is a plaindrom otherwise the traverse aren't equal so the word isnot
# plaindorme
######################################################################################

class Solution():
    stack=[]
    queue=[]
    def __init__(self):
        pass      
    def popCharacter(self):
        return self.stack.pop()
    def pushCharacter(self,ch):
        self.stack.append(ch)        
        return
    def enqueueCharacter(self,ch):
        self.queue.append(ch)
        return
    def dequeueCharacter(self):
        return self.queue.pop(0)
    

    
def main():
    
    s=input()
    obj=Solution()
    l=len(s)
    # push/enqueue all the characters of string s to stack
    for i in range(l):
        obj.pushCharacter(s[i])
        obj.enqueueCharacter(s[i])
        
    isPalindrome=True
    #print(obj.queue)

    '''
    pop the top character from stack
    dequeue the first character from queue
    compare both the characters
    '''
    
    for i in range(l // 2):
        if obj.popCharacter()!=obj.dequeueCharacter():
            isPalindrome=False
            break
    #finally print whether string s is palindrome or not.
    if isPalindrome:
        print("The word, "+s+", is a palindrome.")
    else:
        print("The word, "+s+", is not a palindrome.")    






if __name__=="__main__":
    main()
    
