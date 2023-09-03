class Stack:
    def __init__(self):
        self.items = []

    def push(self, item):
        self.items.append(item)

    def pop(self):
        if not self.isEmpty():
            return self.items.pop()

    def peek(self):
        if not self.isEmpty():
            return self.items[-1]

    def isEmpty(self):
        return self.size() == 0

    def size(self):
        return len(self.items)
    
    def elements(self):
        return self.items
    
    def treePop(self, height):
        for i in range(len(self.elements()) - 1, -1, -1):
            if height >= self.items[i]:
                self.pop()
    
def lookAtTree(treeHeights):
    stack = Stack()
    for tree in treeHeights:
        if not stack.isEmpty():
            if tree >= stack.peek():
                stack.treePop(tree)
        stack.push(tree)
    return stack.size()
    
inp = input('Enter Input : ').split(',')
converted_values = []
for item in inp:
    values = item.split(' ')
    if values[0] == 'A':
        converted_values.append(int(values[1]))
    else:
        print(lookAtTree(converted_values))