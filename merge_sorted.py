# Definition for singly-linked list.
class ListNode:
    def __init__(self, x):
        self.val = x
        self.next = None

    @staticmethod
    def mergeTwoLists(l1, l2):
        """
        :type l1: ListNode
        :type l2: ListNode
        :rtype: ListNode
        """
        if l1 == None:
            return l2
        elif l2 == None:
            return l1
        
        return_linked_list = None
        if l1.val < l2.val:
            return_linked_list = ListNode(l1.val)
            l1 = l1.next
        elif l2.val <= l1.val:
            return_linked_list = ListNode(l2.val)
            l2 = l2.next
        root_node = ListNode(return_linked_list.val)
        start_node = True
        
        while True:
            if (l1 == None or l1.val == None) and l2 != None:
                return_linked_list.next = ListNode(l2)
                return_linked_list = return_linked_list.next
                l2 = l2.next
                continue
                
            elif (l2 == None or l2.val == None) and l1 != None:
                return_linked_list.next = ListNode(l1)
                return_linked_list = return_linked_list.next
                l1 = l1.next
                continue
            
            else:
                break
            
            new_node = None
            if l1.val < l2.val:
                new_node = ListNode(l1.val)
                l1 = l1.next
                
            elif l2.val <= l1.val:
                new_node = ListNode(l2.val)
                l2 = l2.next
            
            return_linked_list.next = new_node
            if start_node:
                root_node.next = return_linked_list
                start_node = False
            return_linked_list = return_linked_list.next
            
        return root_node
            
