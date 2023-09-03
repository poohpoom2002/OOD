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
    
    def __str__(self):
        return str(self.queue)
    
    def __iter__(self):
        self.current = 0
        return self

    def __next__(self):
        if self.current < len(self.queue):
            item = self.queue[self.current]
            self.current += 1
            return item
        else:
            raise StopIteration
    
def input_is_valid(item):
    for x in item[2].split(","):
        if len(x) != int(item[0]):
            return False
    if len(item) != 3 or len(item[2].split(",")) != int(item[1]):
        return False
    return True

def bfs(maze, start, count):
    directions = [(0, -1), (1, 0), (0, 1), (-1, 0)]
    queue = Queue()
    visited = Queue()
    queue.enqueue(start)
    visited.enqueue(start)
    print(f"Queue: {queue}")
    while True:
        for x, y in directions:
            if queue.peek()[1] + y < 0 or queue.peek()[1] + y > len(maze) - 1 or queue.peek()[0] + x < 0 or queue.peek()[0] + x > len(maze[0]) - 1:
                continue
            elif maze[queue.peek()[1] + y][queue.peek()[0] + x] == '_' and (queue.peek()[0] + x, queue.peek()[1] + y) not in visited:
                visited.enqueue((queue.peek()[0] + x, queue.peek()[1] + y))
                queue.enqueue((queue.peek()[0] + x, queue.peek()[1] + y))
            elif maze[queue.peek()[1] + y][queue.peek()[0] + x] == 'O':
                return "Found the exit portal."
        queue.dequeue()
        if queue.is_empty():
            break
        print(f"Queue: {queue}")
    return "Cannot reach the exit portal."

inp = input("Enter width, height, and room: ").split(" ")
if input_is_valid(inp):
    maze = inp[2].split(",")
    count = 0
    start = 0
    for i in range(len(maze)):
        for j in range(len(maze[0])):
            if maze[i][j] == 'F':
                start = (j, i)
                count += 1
            elif maze[i][j] == '_':
                count += 1
    if start == 0:
        print("Invalid map input.")
    else:
        print(bfs(maze, start, count))
else:
    print("Invalid map input.")