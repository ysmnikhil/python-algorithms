'''
[Head]                              [Tail]
[value, next] -> [value1, next1] -> [value2, next2]

** Insert **
append
appendWithTail

** Remove **
remove

** Iterate **
get
__toList__
'''

class Node:
    def __init__(self, value = None, next = None):
        self.value = value
        self.next = next if next else None

class LinkedList:
    def __init__(self, value = None):
        self.head = None
        self.tail = None
        self.length = 0

        if (value):
            node = Node(value)

            self.head = node
            self.tail = node
            self.head.next = self.tail
            self.updateLen()

    def updateLen(self, v = 1):
        self.length = self.length + v

    def appendWithTail(self, value):
        node = Node(value)

        if self.head == None:
            self.head = node
            self.tail = node
            self.updateLen()
            return

        self.tail.next = node
        self.tail = node
        self.updateLen()

    def append(self, value):
        node = Node(value, self.tail)
        self.tail = node

        node = Node(value)

        currentNode = self.head

        while (currentNode):
            if currentNode.next:
                currentNode = currentNode.next
            else:
                currentNode.next = node
                this.tail = node
                self.length += 1
                return

    def get(self, value):
        currentNode = self.head

        while (currentNode):
            if currentNode.value == value:
                return currentNode
            currentNode = currentNode.next
        
        return None

    def remove(self, value):
        if self.head.value == value and self.tail.value == value:
            self.head = None
            self.tail = None
            self.updateLen(-1)
            return

        currentNode = self.head

        while currentNode:
            if currentNode.next.value == value:
                c = currentNode.next
                currentNode.next = currentNode.next.next
                self.updateLen(-1)
                return c
            else:
                currentNode = currentNode.next
        
        return None

    def __toList__ (self):
        currentNode = self.head

        l = []
        while currentNode:
            l.append(currentNode.value)
            currentNode = currentNode.next

        return l


linkedList = LinkedList('a')
linkedList.appendWithTail('b')
linkedList.appendWithTail('c')
linkedList.appendWithTail('c1')
linkedList.appendWithTail('d')

linkedList.remove('b')

print(linkedList.length)
print(linkedList.__toList__())
        