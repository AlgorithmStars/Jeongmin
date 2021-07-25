class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next

class Solution:
    def mergeTwoLists(self, l1:ListNode, l2:ListNode):
        def merge(node, left, right):
            if left is not None and right is None:
                node.next = left
                return
            elif right is not None and left is None:
                node.next = right
                return

            if left.val <= right.val:
                node.next = ListNode(left.val)
                return merge(node.next, left.next, right)
            else: #left.val > right.val:
                node.next = ListNode(right.val)
                return merge(node.next, left, right.next)


        if l1 is None:
            return l2
        elif l2 is None:
            return l1

        if l1.val <= l2.val:
            head = ListNode(l1.val)
            merge(head, l1.next, l2)
        else:
            head = ListNode(l2.val)
            merge(head, l1, l2.next)
        return head
