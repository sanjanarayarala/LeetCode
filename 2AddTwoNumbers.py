# Definition for singly-linked list.
# class ListNode(object):
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution(object):
    def addTwoNumbers(self, l1, l2):
        """
        :type l1: Optional[ListNode]
        :type l2: Optional[ListNode]
        :rtype: Optional[ListNode]
        """

        head1= l1
        head2= l2

        str1=""
        str2=""
        
        while l1.next!=None:
            str1+=str(l1.val)
            l1=l1.next
        str1+=str(l1.val)
        str1=str1[::-1]

        print(str1)

        while l2.next!=None:
            str2+=str(l2.val)
            l2=l2.next
        str2+=str(l2.val)
        str2=str2[::-1]

        print(str2)

        res=int(str1)+int(str2)
        print(res)
        res= str(res)
        res= res[::-1]
        print(res)

        prevobj=ListNode()
        start=ListNode()
        count=0
        for i in res:
            llobj= ListNode()
            llobj.val=int(i)
            llobj.next=None
            if count==0:
                prevobj=llobj
                start=prevobj
            else:
                prevobj.next=llobj
                prevobj=llobj
            count+=1
        
        return start



        