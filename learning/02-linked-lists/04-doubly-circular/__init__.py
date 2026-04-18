'''
[Head]                                
[prev, value, next] <-> [prev1, value1, next1] <-> [prev2, value2, next2] -- | 
    ^                                                                        |
    | ------------------------------------------------------------------------

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
    def __init__(self, value = None, next = None, prev = None):
        self.value = value
        self.prev = prev if prev else None
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
                node.prev = currentNode
                self.length += 1
                return
    
    def prepend(self, value):
        node = Node(value, self.head)

        currentNode = self.head

        while (currentNode):
            if currentNode.next and currentNode.next != self.head:
                currentNode = currentNode.next
            else:
                currentNode.next = node
                self.head.prev = node
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
            if self.head.next:
                self.head.next.prev = None
                self.head = self.head.next
            else:
                self.head = None
            self.updateLen(-1)
            return

        currentNode = self.head

        while currentNode:
            if currentNode.next and currentNode.next.value == value:
                c = currentNode.next
                currentNode.next.next.prev = currentNode
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
            currentNode = currentNode.next

        return l

    def __toString__ (self):
        currentNode = self.head

        l = ''
        while currentNode:
            prev = currentNode.prev.value if currentNode.prev else 'None'
            next = currentNode.next.value if currentNode.next else 'None'
            l += 'prev: ' + prev + ' value: ' + currentNode.value + ' next: ' + next + '\n'
            currentNode = currentNode.next

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
        