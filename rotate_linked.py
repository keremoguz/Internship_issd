class Node:
    def __init__(self,data):
        self.data = data
        self.next = None
    
class Linkedlist:
    def __init__(self):
        self.head = None
    
    def append(self, data):
        new_node = Node(data)
        if self.head is None:
            self.head = new_node
            return
        last_node = self.head
        while last_node.next:
            last_node = last_node.next
        last_node.next = new_node

    def print_linked_l(self):
        curr_node = self.head
        while curr_node:
            print(curr_node.data)
            curr_node = curr_node.next

    def rotate(self,k):
        
        p = self.head # to keep kth node
        q = self.head # to keep last node
        count = 1
        len_list = 1
        if not q:
            return
        while q.next:
            q = q.next
            len_list +=1

        if len_list< k:
            print("k is bigger than the lenghth of the list")
            return
        k = len_list - k # changes k to the index of the node

        while p and count < k:
            """
            when it reaches to k it stops.
            if k is bigger than the lenght of the list, loop terminates by p becoming None
            """
            p = p.next
            count += 1

        while q.next:
            q = q.next
            len_list +=1
        if len_list< k:
            print("k is bigger than the lenghth of the list")
            return
        q.next = self.head # bounds q to the head of the list
        self.head = p.next # changes head to the next element of p
        p.next = None # bounds p to null to make it the last node
        
l = Linkedlist()
l.append(1)
l.append(2)
l.append(3)
l.append(4)
l.append(5)
l.rotate(2)
l.print_linked_l()




