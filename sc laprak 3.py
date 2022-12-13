class Stack:
    def __init__(self):
        self._data = []

    def __len__(self):
        return len(self._data)

    def _is_empty(self):
        return len(self._data) == 0

    def push(self, e):
        self._data.append(e)

    def top(self):

        if self._is_empty():
            print("Empty!")
        return self._data[-1]

    def pop(self):
        if self._is_empty():
            print("Empty!")
        return self._data.pop()

    def printAll(self):
        for i in range(len(self)):
            print(self._data[i], end=" ")
        print()



class Tree_Mondstadt:
    def __init__(self, data, parent):
        self._data = data
        self._children = Stack()
        self._parent = parent

    def addChild(self, data):
        self._children.push((data.operator()))
    def operator(self):
        return self._data

    def parent(self):
        return self._parent

    def children(self):
        return self._children

    def isRoot(self):
        return self._parent is None

    def isExternal(self):
        return len(self._children) == 0

class Tree_Liyue:
    def __init__(self, data, parent):
        self._data = data
        self._children = Stack()
        self._parent = parent

    def addChild(self, data):
        self._children.push((data.operator()))
    def operator(self):
        return self._data

    def parent(self):
        return self._parent

    def children(self):
        return self._children

    def isRoot(self):
        return self._parent is None

    def isExternal(self):
        return len(self._children) == 0


class Tree_Inazuma:
    def __init__(self, data, parent):
        self._data = data
        self._children = Stack()
        self._parent = parent

    def addChild(self, data):
        self._children.push((data.operator()))
    def operator(self):
        return self._data

    def parent(self):
        return self._parent

    def children(self):
        return self._children

    def isRoot(self):
        return self._parent is None

    def isExternal(self):
        return len(self._children) == 0



class Tree_Sumeru:
    def __init__(self, data, parent):
        self._data = data
        self._children = Stack()
        self._parent = parent

    def addChild(self, data):
        self._children.push((data.operator()))
    def operator(self):
        return self._data

    def parent(self):
        return self._parent

    def children(self):
        return self._children

    def isRoot(self):
        return self._parent is None

    def isExternal(self):
        return len(self._children) == 0


class Tree_Fontaine:
    def __init__(self, data, parent):
        self._data = data
        self._children = Stack()
        self._parent = parent

    def addChild(self, data):
        self._children.push((data.operator()))
    def operator(self):
        return self._data

    def parent(self):
        return self._parent

    def children(self):
        return self._children

    def isRoot(self):
        return self._parent is None

    def isExternal(self):
        return len(self._children) == 0



class Tree_Natlan:
    def __init__(self, data, parent):
        self._data = data
        self._children = Stack()
        self._parent = parent

    def addChild(self, data):
        self._children.push((data.operator()))
    def operator(self):
        return self._data

    def parent(self):
        return self._parent

    def children(self):
        return self._children

    def isRoot(self):
        return self._parent is None

    def isExternal(self):
        return len(self._children) == 0



class Tree_Snezhnaya:
    def __init__(self, data, parent):
        self._data = data
        self._children = Stack()
        self._parent = parent

    def addChild(self, data):
        self._children.push((data.operator()))
    def operator(self):
        return self._data

    def parent(self):
        return self._parent

    def children(self):
        return self._children

    def isRoot(self):
        return self._parent is None

    def isExternal(self):
        return len(self._children) == 0


class Node:
	
	def __init__(self, data):
		self.data = data
		self.next = None
		self.prev = None
class DoubleLinkedList:

    def __init__(self):
            self.head = None

    def tambah_data(self, data):

        new_node = Node(data)

        new_node.next = self.head

        if self.head is not None:
            self.head.prev = new_node

        self.head = new_node

    def reverse(self):
        temp = None
        current = self.head
 

        while current is not None:
            temp = current.prev
            current.prev = current.next
            current.next = temp
            current = current.prev
 

        if temp is not None:
            self.head = temp.prev

 

root_monstadt=Tree_Mondstadt("Venti",None)
root_monstadt.addChild(Tree_Mondstadt("Diluc",root_monstadt))
root_monstadt.addChild(Tree_Mondstadt("Jean",root_monstadt))
root_monstadt.addChild(Tree_Mondstadt("Eula",root_monstadt))

root_liyue=Tree_Liyue("Zhongli",None)
root_liyue.addChild(Tree_Liyue("Keqing",root_liyue))
root_liyue.addChild(Tree_Liyue("Xiao",root_liyue))

root_inazuma=Tree_Inazuma("Raiden",None)
root_inazuma.addChild(Tree_Inazuma("Ayaka",root_inazuma))

root_sumeru=Tree_Sumeru("Nahida",None)
root_sumeru.addChild(Tree_Sumeru("Cyno",root_sumeru))
root_sumeru.addChild(Tree_Sumeru("Nilou",root_sumeru))

ddl=DoubleLinkedList()
ddl.tambah_data(root_monstadt)
ddl.tambah_data(root_liyue)
ddl.tambah_data(root_inazuma)
ddl.tambah_data(root_sumeru)



ddl.reverse()
print("==============================")
print(ddl.head.data.operator(),end="\n\n")
ddl.head.data.children().printAll()
print("==============================")
print()

print("==============================")
print(ddl.head.next.data.operator(),end="\n\n")
ddl.head.next.data.children().printAll()
print("==============================")
print()

print("==============================")
print(ddl.head.next.next.data.operator(),end="\n\n")
ddl.head.next.next.data.children().printAll()
print("==============================")
print()

print("==============================")
print(ddl.head.next.next.next.data.operator(),end="\n\n")
ddl.head.next.next.next.data.children().printAll()
print("==============================")
print()




