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

my_queue = Queue()
your_queue = Queue()
score = 0
inp = input("Enter Input : ").split(",")
for item in inp:
    value = item.split(" ")
    my_queue.enqueue(value[0])
    your_queue.enqueue(value[1])
myQueue = [item.replace("'", "") for item in my_queue.elements()]
yourQueue = [item.replace("'", "") for item in your_queue.elements()]
print("My   Queue =", ", ".join(myQueue))
print("Your Queue =", ", ".join(yourQueue))
print("My   Activity:Location = ", end="")
for item in myQueue:
    word = item.split(":")
    if word[0] == '0':
        word[0] = 'Eat'
    elif word[0] == '1':
        word[0] = 'Game'
    elif word[0] == '2':
        word[0] = 'Learn'
    else:
        word[0] = 'Movie'
    if word[1] == '0':
        word[1] = 'Res.'
    elif word[1] == '1':
        word[1] = 'ClassR.'
    elif word[1] == '2':
        word[1] = 'SuperM.'
    else:
        word[1] = 'Home'
    print(':'.join(word), end="")
    if item != myQueue[-1]:
        print(",", end=" ")
print("\nYour Activity:Location = ", end="")
for item in yourQueue:
    word = item.split(":")
    if word[0] == '0':
        word[0] = 'Eat'
    elif word[0] == '1':
        word[0] = 'Game'
    elif word[0] == '2':
        word[0] = 'Learn'
    else:
        word[0] = 'Movie'
    if word[1] == '0':
        word[1] = 'Res.'
    elif word[1] == '1':
        word[1] = 'ClassR.'
    elif word[1] == '2':
        word[1] = 'SuperM.'
    else:
        word[1] = 'Home'
    print(':'.join(word), end="")
    if item != yourQueue[-1]:
        print(",", end=" ")
for i in range(my_queue.size()):
    me = my_queue.peek().split(":")
    you = your_queue.peek().split(":")
    if me[0] == you[0] and me[1] == you[1]:
        score += 4
    elif me[1] == you[1]:
        score += 2
    elif me[0] == you[0]:
        score += 1
    else:
        score -= 5
    my_queue.dequeue()
    your_queue.dequeue()
if score >= 7:
    print(f"\nYes! You're my love! : Score is {score}.")
elif score > 0:
    print(f"\nUmm.. It's complicated relationship! : Score is {score}.")
else:
    print(f"\nNo! We're just friends. : Score is {score}.")