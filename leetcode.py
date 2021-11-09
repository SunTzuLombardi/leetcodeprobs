https://leetcode.com/problems/palindrome-number/solution/
class Solution:
    def isPalindrome(self, x: int) -> bool:
        #store a copy of this number
        temp=x
        #calculate reverse of this number
        reverse_num=0
        while(x>0):
            #extract last digit of this number
            digit=x%10
            #append this digit in reveresed number
            reverse_num=reverse_num*10+digit
            #floor divide the number leave out the last digit from number
            x=x//10
        #compare reverse to original number
        if(temp==reverse_num):
            return True
        else:
            return False

https://leetcode.com/problems/length-of-last-word
class Solution:
    def lengthOfLastWord(self, s: str) -> int:
        #Split by spaces
        words = s.split()
        #get last word
        #-1 means the last element of the list
        lword = words[-1]
        #return length of last word
        #splitting the string
        return len(lword)
