# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
import heapq
class ListNode:
    def __init__(self, val = 0, next = None):
        self.val = val
        self.next = next
    
    def __lt__(self, other):
        return self.val < other.val # needed for heapq to compare nodes

class Solution:
    def mergeKLists(self, lists: List[Optional[ListNode]]) -> Optional[ListNode]:
        heap = []

        # Push thea head of each list into the heap
        for i, node in enumerate(lists):
            if node:
                heapq.heappush(heap, (node.val, i, node)) # i ensures uniqueness for duplicate values
        
        dummy = ListNode(0)
        curr = dummy

        while heap:
            val, i, node = heapq.heappop(heap)
            curr.next = node
            curr = curr.next
            if node.next:
                heapq.heappush(heap, (node.next.val, i, node.next))

        return dummy.next

        