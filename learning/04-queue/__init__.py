import sys
import os
import importlib
import importlib.util

# Load linked list module from filesystem path (folder names contain hyphens)
BASE_DIR = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
LINKED_LIST_PATH = os.path.join(BASE_DIR, "02-linked-lists", "01-single", "__init__.py")
SPEC = importlib.util.spec_from_file_location("single_linked_list", LINKED_LIST_PATH)
linked_list_module = importlib.util.module_from_spec(SPEC)
SPEC.loader.exec_module(linked_list_module)
LinkedList = linked_list_module.LinkedList

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


