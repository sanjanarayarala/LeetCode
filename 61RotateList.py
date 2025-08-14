# Definition for singly-linked list.
# class ListNode(object):
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution(object):
    def rotateRight(self, head, k):
        """
        :type head: Optional[ListNode]
        :type k: int
        :rtype: Optional[ListNode]
        """
        # if head==None or head.next==None or k==0:
        #     return head
        # start= head
        # end=None
        # count=0

        
        
        # while count<k:
        #     count+=1
        #     if count>1:
        #         head=head2
        #     #start= head
        #     while head.next is not None:
        #         #print(head.val)
        #         end= head
        #         head= head.next
                
        #     end.next=None
        #     #print('end: ', end.val)
        #     # print(head.val)
        #     head.next= start
        #     start= head
        #     head2=head
        #     while head.next is not None:
        #         #print(head.val)
        #         head=head.next
        #     #print(head.val)
        #     #print('break')
        # return head2
        if head==None or head.next==None:
            return head
            
        head2=head
        length=1

        while head.next is not None:
            length+=1
            head= head.next
        print(length)
        k=k%length
        head=head2
        if k==0:
            return head


        begin=head
        end=head
        start=head

        count=0
        print(length-k)
        while count<(length-k):
            print(head.val)
            end=head
            head=head.next
            start=head
            count+=1
        
        end.next=None

        
        if head.next is None:
            head.next= begin
        else:
            while head.next is not None:
                head= head.next
            
            head.next=begin
        return start




            
            

        


