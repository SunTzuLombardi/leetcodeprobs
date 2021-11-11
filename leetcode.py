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


https://leetcode.com/problems/merge-two-sorted-lists/
# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:


    def mergeTwoLists(self, l1: Optional[ListNode], l2: Optional[ListNode]) -> Optional[ListNode]:
        def insert(root, item):
            temp = ListNode(item)

            if (root == None):
                root = temp
            else :
                ptr = root
                while (ptr.next != None):
                    ptr = ptr.next
                    ptr.next = temp

            return root

        merged = ListNode()

        #if both None return None
        if l1 is None and l2 is None:
            return None
        elif (l1 or l2) is None:
            #if either is None return the other
            print('l1 is none')
            merged = l1 if l2 is None else l2
        else:
            #idea make two lists from traversing the nodes combine then create ListNode
            first = []
            while l1 is not None:
                first.append(l1.val)
                l1 = l1.next

            sec = []
            while l2 is not None:
                sec.append(l2.val)
                l2 = l2.next

            first += sec
            first = sorted(first)
            print(first)

            for i in range(0,len(first)):
                merged = insert(merged, first[i])


        return merged
