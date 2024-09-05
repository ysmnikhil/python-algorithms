'''
[Head]
[value, next] -> [value1, next1] -> [value2, next2] -- | 
    ^                                                  |
    | --------------------------------------------------
** Insert **
prepend
append

** Remove **
remove
removeHead?

** Iterate **
find
__toList__
__toString__
'''

class Node:
    def __init__(self, value = None, next = None):
        self.value = value
        self.next = next if next else None

class LinkedList:
    def __init__(self, value = None):
        self.head = None
        self.length = 0

        if (value):
            node = Node(value)

            self.head = node
            self.updateLen()

    def updateLen(self, v = 1):
        self.length = self.length + v

    def append(self, value):
        node = Node(value, self.head)

        currentNode = self.head

        while (currentNode):
            if currentNode.next and currentNode.next != self.head:
                currentNode = currentNode.next
            else:
                currentNode.next = node
                self.updateLen()
                return
    
    def prepend(self, value):
        node = Node(value, self.head)

        currentNode = self.head

        while (currentNode):
            if currentNode.next and currentNode.next != self.head:
                currentNode = currentNode.next
            else:
                currentNode.next = node
                self.head = node
                self.updateLen()
                return

    def find(self, value):
        currentNode = self.head

        while (currentNode):
            if currentNode.value == value:
                return currentNode
            if currentNode.next != self.head:
                currentNode = currentNode.next
            else:
                currentNode = None
        
        return None

    def removeHead(self):
        return self.remove(self.head.value)

    def remove(self, value):
        if self.head.value == value:
            self.updateLen(-1)

            if self.head.next:
                currentNode = self.head

                while currentNode:
                    if currentNode.next and currentNode.next == self.head:
                        currentNode.next = self.head.next
                        currentNode = None
                    else:
                        currentNode = currentNode.next

                self.head = self.head.next
            else:
                self.head = None
            
            return

        currentNode = self.head

        while currentNode:
            if currentNode.next and currentNode.next.value == value:
                c = currentNode.next
                currentNode.next = currentNode.next.next
                self.updateLen(-1)
                return c
            elif currentNode.next != self.head:
                currentNode = currentNode.next
            else :
                currentNode = None

        return None

    def __toList__ (self):
        currentNode = self.head

        l = []
        while currentNode:
            l.append(currentNode.value)
            if currentNode.next != self.head:
                currentNode = currentNode.next
            else:
                currentNode = None

        return l

    def __toString__ (self):
        currentNode = self.head

        l = ''
        while currentNode:
            next = currentNode.next.value if currentNode.next else 'None'
            l += ' value: ' + currentNode.value + ' next: ' + next + '\n'
            if currentNode.next != self.head:
                currentNode = currentNode.next
            else:
                currentNode = None

        return l

linkedList = LinkedList('a')
linkedList.append('b')
linkedList.append('c')
linkedList.append('c1')
linkedList.append('d')

linkedList.append('a1')
linkedList.prepend('a2')
linkedList.prepend('a1')

linkedList.remove('b')
linkedList.removeHead()

print(linkedList.find('b'))
print(linkedList.length)
print(linkedList.__toList__())
print(linkedList.__toString__())
        