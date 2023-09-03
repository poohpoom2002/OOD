class Queue:
    def __init__(self):
        self.queue = []

    def enqueue(self, item):
        self.queue.append(item)

    def dequeue(self):
        if self.is_empty():
            raise IndexError("Queue is empty")
        return self.queue.pop(0)

    def is_empty(self):
        return len(self.queue) == 0

    def size(self):
        return len(self.queue)

    def peek(self):
        if self.is_empty():
            raise IndexError("Queue is empty")
        return self.queue[0]
    
    def elements(self):
        return self.queue
    
    def sort(self):
        return self.queue.sort()
    
    def is_duplicate(self):
        self.sort()
        for i in range(self.size() - 1):
            if self.queue[i] == self.queue[i + 1]:
                return True
        return False
    
queue = Queue()
inp = input("Enter Input : ").split("/")
for element in inp[0].split(" "):
    queue.enqueue(element)
for item in inp[1].split(","):
    value = item.split(" ")
    if value[0] == 'E':
        queue.enqueue(value[1])
    else:
        queue.dequeue()
if queue.is_duplicate():
    print("Duplicate")
else:
    print("NO Duplicate")