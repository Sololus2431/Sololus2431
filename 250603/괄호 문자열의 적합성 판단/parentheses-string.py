import sys
str = input()

# Please write your code here.
class Stack:
    def __init__(self):
        self.items = []
    
    def size(self):
        return len(self.items)
    
    def empty(self):
        return not self.items
    
    def push(self, item):
        self.items.append(item)
    
    def pop(self):
        if self.empty():
            return
        else:
            self.items.pop()
    
    def top(self):
        if self.empty():
            return None
        else:
            return self.items[-1]


s = Stack()
for i in str:
    if i == '(':
        s.push("(")
    else:
        if s.empty():
            print("No")
            sys.exit()
        else:
            s.pop()

if s.empty():
    print("Yes")
else:
    print("No")