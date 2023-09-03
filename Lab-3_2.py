class Stack:
    def __init__(self):
        self.items = []

    def push(self, item):
        self.items.append(item)

    def pop(self):
        if not self.isEmpty():
            return self.items.pop()

    def isEmpty(self):
        return len(self.items) == 0

    def size(self):
        return len(self.items)

def check_parentheses(expression):
    stack = Stack()
    opening_parentheses = ['(', '[', '{']
    closing_parentheses = [')', ']', '}']
    pairs = {
        ')': '(',
        ']': '[',
        '}': '{'
    }
    for char in expression:
        if char in opening_parentheses:
            stack.push(char)
        elif char in closing_parentheses:
            if stack.isEmpty():
                return f"{expression} close paren excess"
            elif stack.pop() != pairs[char]:
                return f"{expression} Unmatch open-close"
    if not stack.isEmpty():
        if stack.size() == 1:
            return f"{expression} open paren excess   1 : {stack.items[0]}"
        else:
            return f"{expression} open paren excess   {stack.size()} : {''.join(stack.items)}"
    return f"{expression} MATCH"

print(check_parentheses(input("Enter expresion : ")))