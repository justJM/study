#%% Node
class Node:
    def __init__(self, contents=None, next=None):
        self.contents = contents
        self.next= next

    def getContent(self):
        return self.contents

    def __str__(self):
        return str(self.contents)
    
def print_list(node):
    while node:
        print(node.getContent())
        node=node.next
    print()

def testList():
    node1=Node('car')
    node2=Node('bus')
    node3=Node('lorry')
    node1.next=node2
    node2.next=node3
    print_list(node1)
        
testList()

#%% class Stack 
class Stack:
    def __init__(self):
        self.items =[]
    
    def push(self, item):
        self.items.append(item)

    def pop(self):
        return self.items.pop()

    def isEmpty(self):
        return self.items ==[]

    def peek(self):
        return self.items[len(self.items)-1]

mystack = Stack()
mystack.push('john')
mystack.push('kim')
#%% class Stack 
mystack.peek()
#%% class Stack 
mystack.pop()
#%% class Stack 
mystack.items

#%% class Quene
class Queue:
    def __init__(self):
        self.items =[]

    def add(self,item):
        self.items.append(item)

    def delete(self):
        itemTodel = self.items[0]
        del self.items[0]
        return itemTodel

    def size(self):
        return len(self.items)

    def report(self):
        return self.items

Q = Queue()
Q.add('bob')
Q.add('bro')
Q.add('car')
Q.add('tan')
print(Q.size())
print(Q.report())
print(Q.delete())
print(Q.report())

#%% Queue 모듈 사용. 
import queue

a = queue.Queue()
b = queue.LifoQueue()



