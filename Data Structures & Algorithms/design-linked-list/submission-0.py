class ListNode:
    def __init__(self, val):
        self.val = val
        self.next = None

class MyLinkedList:

    def __init__(self):
        self.head = ListNode(-1)
        

    def get(self, index: int) -> int:

        point = self.head.next

        counter = 0

        while point:

            if counter == index:
                return point.val
            
            counter += 1
            point = point.next
        
        return -1
                 
    def addAtHead(self, val: int) -> None:

        newNode = ListNode(val)

        newNode.next = self.head.next
        self.head.next = newNode

        return
        

    def addAtTail(self, val: int) -> None:

        newNode = ListNode(val)

        point = self.head

        while point.next:
            point = point.next
            
        
        point.next = newNode

        return

    def addAtIndex(self, index: int, val: int) -> None:

        newNode = ListNode(val)

        point = self.head

        counter = 0

        while point:

            if counter == index:
                newNode.next = point.next
                point.next = newNode
                return
            
            counter += 1
            point = point.next
        
        return


        

    def deleteAtIndex(self, index: int) -> None:

        point = self.head

        counter = 0

        while point:

            if counter == index:
                if point.next:
                    point.next = point.next.next
                return
            
            counter += 1
            point = point.next
        
        return
        


# Your MyLinkedList object will be instantiated and called as such:
# obj = MyLinkedList()
# param_1 = obj.get(index)
# obj.addAtHead(val)
# obj.addAtTail(val)
# obj.addAtIndex(index,val)
# obj.deleteAtIndex(index)