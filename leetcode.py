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



# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    
    
    def mergeTwoLists(self, l1: Optional[ListNode], l2: Optional[ListNode]) -> Optional[ListNode]:
        merged = ListNode()
        tail = merged   
        
        #if both None return None
        if l1 is None and l2 is None:
            return None
        
        while l1 and l2:
            if l1.val < l2.val:
                tail.next = l1
                l1 = l1.next
            else:
                tail.next = l2
                l2 = l2.next
            tail = tail.next

        #if l1 not None
        if l1:
            tail.next = l1
        elif l2:
            tail.next = l2 
 
        return merged.next

https://leetcode.com/problems/climbing-stairs/
    class Solution:
    def climbStairs(self, n: int) -> int:
        #distinct ways of climbing too the top either using 1 or 2 steps
        #take all steps of 1
        #take all steps of 2 then 1 if needed
        #take first step of 2 then steps of 1
        # 
        #this is a combination problem
        ###2 solutions...store previous steps result in hastable and if there add to it....or
        #calculate the permutations...
        
        #first way
        #ways =0
        #if n==1:
        #    ways = 1
        #elif n==2:
        #    ways = 2
        #elif n==3:
        #    ways = 3
        #else:
        #    ways = self.climbStairs(n-1)+self.climbStairs(n-2)
            
        #return ways




        #The idea is that the number of 2-steps that we can take
        #is limited by the total steps of the stairs. Hence, we
        #can find out the total number of 2-steps we can make via
        #int(n/2)
        #For example, if the total steps of the stairs is 5,
        #we can only take 2-steps twice and
        #remaining 1-step - (2steps + 2steps + 1step)
        #note that this is just one combination. We
        #need #to find out the permutation for this set of steps,
        #which is calculated using:

        #factorial(max no. of 1-step + max no. of 2-step) /
        #( factorial(max no. of 1-step) * factorial(max no. of 2-step) )

        #Once we know the total number of 2-steps we can make,
        #the number of 1-step is easily obtained via

        #n - 2 * (max no. of 2-steps)
        #And we loop through the possibilities of no. of 2-steps:
        def factorial(n):
            if n == 0:
                return 1
            else:
                return n * factorial(n-1)

        counter = 0
        for i in range(0, int(n/2) + 1):
            # i represents the current number of 2-steps
            # int(n/2) is the max. no. of 2-steps
            num_2steps = i
            num_1steps = n - 2*i
            total_climbs = num_1steps + num_2steps
            counter += factorial(total_climbs) / ( factorial(num_1steps) * factorial(num_2steps) )

        return int(counter)

#nice teams
when match i+2
else j+1
Sort the array in ascending order.
for ex: n=8; rating=[14,18,30,45,43,2,8,3]; minDiff=4;
After sorting [2,3,8,14,18,30,43,45]
Answer is in bold: [2,3,8,14,18,30,43,45]

It can be solved with greedy approach
Pseudo Code:
Array is sorted in ascending order.
int i=0; int Pairs=0;
while(i+1 < n)
{
if(abs(A[i]-A[i+1]) <= minDiff)
Pairs++; i+=2;
else
i++;

https://www.hackerrank.com/challenges/minimum-absolute-difference-in-an-array
def minimumAbsoluteDifference(arr):
    # Write your code here

    cache = []
    arr=sorted(arr)
    minabs=abs(max(arr)-min(arr))
    print(arr)
    n=len(arr)
    i=0
    for i in range(n-1):
        differ=abs(arr[i+1]-arr[i])
        cache.append(differ)

        if differ<minabs :
            minabs = differ
    return min(cache)


https://www.hackerrank.com/challenges/luck-balance
def luckBalance(k, contests):
    # Write your code here
    bal=0
    luck=0
    imp=-1
    #sort to have highest value first
    #if impor is 0 then 
    contests.sort(reverse=True)
    for cont in contests:
        luck=cont[0]
        imp=cont[1]
        print(k,luck,imp)
        #num to lose do imp =0 first
        if imp ==0:
            bal = bal+luck
        elif k>0:
            bal = bal+luck
            k=k-1
        else:
            bal = bal-luck
    return bal


    https://www.hackerrank.com/challenges/greedy-florist/problem
def getMinimumCost(k, c):
    mincost=0
    c.sort(reverse=True)
    l = len(c)
    #last person buys most expensive flower
    for i in range(l):
        print(mincost,(int(i/k)+1)*c[i] )
        mincost=mincost + (int(i/k)+1)*c[i]

    return mincost


https://leetcode.com/problems/pascals-triangle/
class Solution:
    def generate(self, numRows: int) -> List[List[int]]:
        tri = []

        #create a 2D array for the result
        for i in range(numRows):
            tri.append([1]*(i+1))

        #do the sums by looking at each row starting at 2
        #sum the m and m+1 from previous to make the value
        for k in range(2,len(tri)):
            print(tri[k])
            temp= tri[k-1]
            for m in range(len(temp)-1):
                tri[k][m+1]=temp[m]+temp[m+1]

        return tri

