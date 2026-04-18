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

class Hash:
    length = 26

    def __init__(self):
        self.hl = [LinkedList() for _ in range(self.length)]

    def hash(self, value):
        hash_value = 0
        for char in str(value):
            hash_value = (hash_value * 31 + ord(char)) % self.length
        return hash_value

    def add(self, value):
        return self.hl[self.hash(value)].append(value)

    def find(self, value):
        return self.hl[self.hash(value)].find(value)

    def delete(self, value):
        return self.hl[self.hash(value)].remove(value)

    def __toString__(self):
        l = ''
        for key, ll in enumerate(self.hl):
            if ll.__toString__():
                l += 'key: ' + str(key) + ' \n' + ll.__toString__() + '\n'

        return l

if __name__ == "__main__":
    hash = Hash()
    hash.add('a')
    hash.add('a1')
    hash.add('a2')
    hash.add('a3')
    hash.add('a4')
    hash.add('a')
    hash.add('My name is Nikhil')
    hash.add('My name is Nikhil Malik')
    hash.add('My name is Nikhil Chaudhary')
    hash.add('My name is Nikka')

    print(hash.find('a6'))

    print(hash.delete('a4'))

    print(hash.__toString__())
