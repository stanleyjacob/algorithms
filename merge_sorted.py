
import random
import pdb

# Definition for singly-linked list.
class ListNode:
    def __init__(self, x):
        self.val = x
        self.next = None

    """
    :type l1: ListNode
    :type l2: ListNode
    :rtype: ListNode
    """
    @staticmethod
    def mergeTwoLists(l1, l2):

        def helper(curr_val, previous_node, root_node):
            current_node = ListNode(curr_val)
            if previous_node != None:
                previous_node.next = current_node
                previous_node = current_node

            if root_node == None:
                root_node = current_node
                previous_node = current_node
            
        root_node = None
        previous_node = None

        while True:
            if (l1 == None or l1.val == None) and \
                (l2 == None or l2.val == None):
                break

            elif (l1 == None or l1.val == None) and (l2 != None or l2.val != None):
                
                current_node = ListNode(l2.val)
                if previous_node != None:
                    previous_node.next = current_node
                    previous_node = current_node
                
                if root_node == None:
                    root_node = current_node
                    previous_node = current_node

                l2 = l2.next
                continue
            
            elif (l2 == None or l2.val == None) and (l1 != None or l1.val != None):
                
                current_node = ListNode(l1.val)
                if previous_node != None:
                    previous_node.next = current_node
                    previous_node = current_node
                
                if root_node == None:
                    root_node = current_node
                    previous_node = current_node

                l1 = l1.next
                continue
            
            current_node = None
            if l1.val < l2.val:
                current_node = ListNode(l1.val)
                l1 = l1.next
            
            elif l2.val <= l1.val:
                current_node = ListNode(l2.val)
                l2 = l2.next

            if previous_node == None:
                root_node = current_node
                previous_node = current_node
            else:
                previous_node.next = current_node
                previous_node = current_node
            
        return root_node

def input_integers(num_integers):
    print('Enter %d ordered numbers' %num_integers)
    start = True
    result = None
    root = None
    for i in range(num_integers):
        x = input()
        # while True:
        #     x = random.randint(0, 100)
        #     if result == None or x >= result.val:
        #         break
        if start:
            start = False
            result = ListNode(x)
            root = result
        else:
            current_node = ListNode(x)
            result.next = current_node
            result = result.next
    return root

def print_linked_list(list_node):
    while True:
        if list_node == None:
            break
        print(list_node.val, end = ' ')
        list_node = list_node.next
    print('\n')

num_integers = 1
l1 = input_integers(num_integers)
num_integers = 0
l2 = input_integers(num_integers)
print_linked_list(l1)
print_linked_list(l2)
merged = ListNode.mergeTwoLists(l1, l2)
print_linked_list(merged)
