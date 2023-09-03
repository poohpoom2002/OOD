class Node:
    def __init__(self, data):
        self.data = data
        self.next = None

class LinkedList:
    def __init__(self):
        self.head = None
    
    def append(self, data):
        new_node = Node(data)
        if not self.head:
            self.head = new_node
            return
        current = self.head
        while current.next:
            current = current.next
        current.next = new_node
    
    def size(self):
        cur, cnt = self.head, 0
        while cur != None:
            cur, cnt = cur.next, cnt + 1
        return cnt

    def process_and_display(self, divisor):
        if divisor > self.size():
            print("Over length")
        else:
            current = self.head
            index = 0
            while current:
                if index % divisor == 0:
                    print(f"Now index {index} value is {current.data}", end=" ")
                    if current.next:
                        print(f"next value is {current.next.data}")
                    else:
                        print("next value is -1")
                index += 1
                current = current.next

numbers = input("Input : ").split("/")
linked_list = LinkedList()
for num in numbers[0].split(" "):
    linked_list.append(int(num))
linked_list.process_and_display(int(numbers[1]))