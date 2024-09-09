import sys
import os
import importlib

# Add the parent directory to the Python path
sys.path.append(os.path.dirname(os.path.dirname(os.path.abspath(__file__))))

# Now import the module
LinkedList = importlib.import_module('linked-list.single').LinkedList

class Queue:
    def __init__(self):
        self.ll = LinkedList()

    def enqueue(self, value):
        return self.ll.append(value)

    def dequeue(self):
        return self.ll.removeHead()

    def __toString__(self):
        return self.ll.__toString__()

if __name__ == "__main__":
    queue = Queue()
    queue.enqueue('a')
    queue.enqueue('a1')
    queue.enqueue('a2')
    queue.enqueue('a3')
    queue.enqueue('a4')

    print(queue.__toString__())
    print(queue.dequeue().value)
    print(queue.dequeue().value)
    queue.enqueue('a5')
    print(queue.__toString__())


