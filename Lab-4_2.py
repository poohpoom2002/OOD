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
    
message = [char for char in input("Enter people : ")]
cashier_0 = Queue()
cashier_1 = Queue()
cashier_2 = Queue()
for x in message:
    cashier_0.enqueue(x)
count = 1
while not cashier_0.is_empty():
    if count % 3 == 1 and not cashier_1.is_empty():
        cashier_1.dequeue()
    if count % 2 == 0 and count >= 10:
        cashier_2.dequeue()
    if cashier_1.size() < 5:
        cashier_1.enqueue(cashier_0.peek())
        cashier_0.dequeue()
    else:
        cashier_2.enqueue(cashier_0.peek())
        cashier_0.dequeue()
    print(count, end=" ")
    print(cashier_0.elements(), end=" ")
    print(cashier_1.elements(), end=" ")
    print(cashier_2.elements())
    count += 1