N = int(input())
command = []
A = []

for _ in range(N):
    line = input().split()
    command.append(line[0])
    if line[0] in ["push_front", "push_back"]:
        A.append(int(line[1]))
    else:
        A.append(0)

# Please write your code here.
class Node:
    def __init__(self, data):
        self.data = data
        self.next = None
        self.prev = None

class DoublyLinkedList:
    def __init__(self):
        self.head = None
        self.tail = None
        self.node_num = 0

    def push_front(self, new_data):
        new_node = Node(new_data)
        new_node.next = self.head

        if self.head != None:
            self.head.prev = new_node
            self.head = new_node
            new_node.prev = None
        else:
            self.head = new_node
            self.tail = new_node
            new_node.prev = None

        self.node_num += 1
    
    def push_back(self, new_data):
        new_node = Node(new_data)
        new_node.prev = self.tail
        if self.tail == None:
            self.head = new_node
            self.tail = new_node
        else:
            self.tail.next =new_node
            self.tail = new_node

        new_node.next = None
        self.node_num += 1

    def pop_front(self):
        if (self.head == None):
            print("List is empty")
        elif(self.head.next == None):
            print(self.head.data)
            self.head = None
            self.tail = None
            self.node_num = 0
        else:
            print(self.head.data)
            self.head = self.head.next
            self.head.prev = None
            self.node_num -= 1
        
    def pop_back(self):
        if self.tail == None:
            print("List is empty")
        elif (self.tail.prev == None):
            print(self.tail.data)
            self.head = None
            self.tail = None
            self.node_num = 0
        else:
            print(self.tail.data)
            self.tail = self.tail.prev
            self.tail.next = None
            self.node_num -= 1
    
    def size(self):
        print(self.node_num)
    
    def empty(self):
        if self.node_num == 0:
            print(1)
        else:
            print(0)
        
    def front(self):
        print(self.head.data)

    def back(self):
        print(self.tail.data)

DLL = DoublyLinkedList()
for i in range(N):
    if command[i] == "push_front":
        DLL.push_front(A[i])
    elif command[i] == "push_back":
        DLL.push_back(A[i])
    elif command[i] == "pop_front":
        DLL.pop_front()
    elif command[i] == "pop_back":
        DLL.pop_back()
    elif command[i] == "size":
        DLL.size()
    elif command[i] == "empty":
        DLL.empty()
    elif command[i] == "front":
        DLL.front()
    elif command[i] == "back":
        DLL.back()