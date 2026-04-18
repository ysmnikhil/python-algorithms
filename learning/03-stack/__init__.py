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


