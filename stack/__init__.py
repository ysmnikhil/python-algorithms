import sys
import os
import importlib

# Add the parent directory to the Python path
sys.path.append(os.path.dirname(os.path.dirname(os.path.abspath(__file__))))

# Now import the module
LinkedList = importlib.import_module('linked-list.single').LinkedList

class Stack:
    def __init__(self):
        self.ll = LinkedList()

    def push(self, value):
        return self.ll.prepend(value)

    def pop(self):
        return self.ll.removeHead()

    def __toString__(self):
        return self.ll.__toString__()

if __name__ == "__main__":
    stack = Stack()
    stack.push('a')
    stack.push('a1')
    stack.push('a2')
    stack.push('a3')
    stack.push('a4')

    print(stack.__toString__())
    print(stack.pop().value)
    print(stack.pop().value)
    stack.push('a5')
    print(stack.__toString__())


