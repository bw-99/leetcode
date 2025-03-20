# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def addTwoNumbers(self, l1: Optional[ListNode], l2: Optional[ListNode]) -> Optional[ListNode]:
        answer_lst = ListNode()
        head = answer_lst

        add = 0
        while l1 or l2:
            sum_num = add
            if l1:
                sum_num += l1.val
                l1 = l1.next
            if l2:
                sum_num += l2.val
                l2 = l2.next
            
            head.val = sum_num % 10
            add = sum_num // 10

            if (l1 == None) and (l2 == None) and (add > 0):
                head.next = ListNode(val=add, next=None)
            elif (l1 == None) and (l2 == None):
                pass
            else:
                head.next = ListNode(val=add, next=None)

            head = head.next

        return answer_lst