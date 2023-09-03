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

queue = Queue()
inp = input("Enter Input : ").split(",")
for item in inp:
    values = item.split(' ')
    if values[0] == 'E':
        queue.enqueue(values[1])
        print(f"Add {values[1]} index is {queue.size() - 1}")
    else:
        if queue.is_empty():
            print(-1)
        else:
            print(f"Pop {queue.peek()} size in queue is {queue.size() - 1}")
            queue.dequeue()
if queue.is_empty():
    print("Empty")
else:
    print(f"Number in Queue is :  {queue.elements()}")