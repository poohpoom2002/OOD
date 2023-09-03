class Node:
    def __init__(self, data):
        self.data = data
        self.next = None
        self.previous = None

class DoubleLinkedList:
    def __init__(self):
        self.head = None
        self.tail = None

    def __str__(self):
        if self.isEmpty():
            return ""
        current = self.head
        elements = []
        while current:
            elements.append(str(current.data))
            current = current.next
        return "->".join(elements)

    def str_reverse(self):
        if self.isEmpty():
            return ""
        current = self.tail
        elements = []
        while current:
            elements.append(str(current.data))
            current = current.previous
        return "->".join(elements)

    def isEmpty(self):
        return self.head is None

    def append(self, data):
        new_node = Node(data)
        if self.isEmpty():
            self.head = new_node
            self.tail = new_node
        else:
            new_node.previous = self.tail
            self.tail.next = new_node
            self.tail = new_node

    def insert(self, index, data):
        if index < 0:
            raise ValueError("Index cannot be negative")
        if index == 0:
            new_node = Node(data)
            new_node.next = self.head
            if self.head:
                self.head.previous = new_node
            self.head = new_node
            if not self.tail:
                self.tail = new_node
        else:
            current = self.head
            counter = 0
            while current:
                if counter == index - 1:
                    new_node = Node(data)
                    new_node.next = current.next
                    new_node.previous = current
                    if current.next:
                        current.next.previous = new_node
                    current.next = new_node
                    if not new_node.next:
                        self.tail = new_node
                    break
                current = current.next
                counter += 1

    def find_index(self, data):
        current = self.head
        index = 0
        while current:
            if current.data == data:
                return index
            current = current.next
            index += 1
        return -1

    def remove(self, data):
        current = self.head
        while current:
            if current.data == data:
                index = self.find_index(data)
                if current.previous:
                    current.previous.next = current.next
                else:
                    self.head = current.next

                if current.next:
                    current.next.previous = current.previous
                else:
                    self.tail = current.previous

                return f"removed : {data} from index : {index}"
            current = current.next
        return "Not Found!"
    
    def index_exists(self, index):
        if index == 0:
            return True

        current_node = self.head
        current_index = 0
        while current_node is not None:
            if current_index == index:
                return True
            current_node = current_node.next
            current_index += 1

        return False
    
    def length(self):
        current = self.head
        count = 0
        while current:
            count += 1
            current = current.next
        return count

dll = DoubleLinkedList()
inp = input("Enter Input : ").split(",")
for element in inp:
    if element[0] == ' ':
        element = element[1:]
    x = element.split(" ")
    if x[0] == 'A':
        dll.append(x[1])
    elif x[0] == "Ab":
        dll.insert(0, x[1])
    elif x[0] == 'I':
        data = x[1].split(":")
        if int(data[0]) == dll.length():
            dll.append(data[1])
            print(f"index = {data[0]} and data = {data[1]}")
        elif not dll.index_exists(int(data[0])):
            print("Data cannot be added")
        else:
            dll.insert(int(data[0]), data[1])
            print(f"index = {data[0]} and data = {data[1]}")
    else:
        print(dll.remove(x[1]))
    print(f"linked list : {dll}\nreverse : {dll.str_reverse()}")