import sys
import os
import importlib

# Add the parent directory to the Python path
sys.path.append(os.path.dirname(os.path.dirname(os.path.abspath(__file__))))

# Now import the module
LinkedList = importlib.import_module('linked-list.single').LinkedList

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

    print(hash.find('a6'))

    print(hash.delete('a4'))

    print(hash.__toString__())
