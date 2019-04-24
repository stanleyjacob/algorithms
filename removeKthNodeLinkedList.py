def removeKthNodeFromEnd(head, k):
    count = 0
    curr_node = head
    while curr_node != None:
      curr_node = curr_node.next
      count += 1

    if k == count:
      head.value = head.next.value
      head.next = head.next.next
      return head
    if k == 0:
      return head

    total_nodes = count
    count = 0
    curr_node = head
    prev_node = None
    while curr_node != None:
      if count == (total_nodes - k):
        prev_node.next = curr_node.next
      prev_node = curr_node
      curr_node = curr_node.next
      count += 1

    return head
