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
    
    def checkPop(self):
        if self.items[-1] == self.items[-2] and self.items[-2] == self.items[-3]:
            return True
        return False

def process_game(input_string):
    stack = Stack()
    temp = 0
    combo_count = 0
    for char in input_string:
        stack.push(char)
        if stack.size() >= 3:
            if stack.checkPop():
                for i in range(3):
                    stack.pop()
                combo_count += 1
                if temp == 2 :
                    temp = 1
                else:
                    temp += 1
            else:
                if temp < 2:
                    temp += 1
                else:
                    temp = 0
    return stack.size(), stack.elements(), combo_count

input_str = input("Enter Input : ").split(" ")
count, result, combo = process_game(input_str)
print(count)
if count == 0:
    print("Empty", end='')
else:
    for i in range(len(result)):
        print(result[-i - 1], end='')
if combo > 1:
    print(f"\nCombo : {combo} ! ! !")