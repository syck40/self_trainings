# chap 7, linked list stack

class LinkedStack:
    class _Node:
        __slots__ = '_element', '_next'
        def __init__(self, element, next):
            self._element = element
            self._next = next
    
    def __init__(self):
        self._head = None
        self._size = 0

    def __len__(self):
        return self._size

    def is_empty(self):
        return self._size == 0

    def push(self, e):
        self._head = self._Node(e, self._head)
        self._size += 1

    def top(self):
        if self._head:
            return self._head._element

    def pop(self):
        if self._head:
            head = self._head
            self._head = self._head._next
            self._size -= 1
            return head

# ab = LinkedStack()
# ab.push(5)
# ab.push(6)
# print(ab.top(), ab.is_empty())
# print(ab.pop())
# print(ab.top(), len(ab))

# chap 7 linkedQueue
class LinkedQueue:
    class _Node:
        def __init__(self, element, next):
            self._element = element
            self._next = next

    def __init__(self, e):
        self._head = self._Node(e, None)
        self._size = 1
        self._tail = self._head
    
    def is_empty(self):
        return self._size == 0

    def enqueue(self, e):
        self._head._next = self._Node(e, None)
        self._tail = self._head._next
        self._size += 1

    def dequeue(self):
        if self._head._next:
            answer = self._head
            self._head = self._head._next
            self._size -= 1
            return answer._element
# bb = LinkedQueue(5)
# bb.enqueue(6)
# print(bb.dequeue())

# Chap 8 Trees
# position object = node has p.element()
# Tree: T.root(), T.is_root(p), T.parent(p), T.num_children(p), T.children(p)
# T.is_leaf(p), len(T), T.is_empty(), T.positions(), iter(T)

class Tree:
    """tree adt"""
    class Position:
        """node adt"""
        def element(self):
            raise NotImplementedError
        def __eq__(self, other):
            raise NotImplementedError
        def __ne__(self, other):
            return not self == other

    def root(self):
        raise NotImplementedError
    def parent(self, p):
        raise NotImplementedError
    def num_children(self, p):
        raise NotImplementedError
    def children(self, p):
        raise NotImplementedError
    def __len__(self):
        raise NotImplementedError
    def is_root(self, p):
        return self.root() == p
    def is_leaf(self, p):
        return self.num_children(p) == 0
    def is_empty(self):
        return len(self) == 0
    def depth(self, p):
        if self.is_root(p):
            return 0
        else:
            return 1 + self.depth(self.parent(p))
    def height(self, p=None):
        if not p:
            return self.root()

        if self.is_leaf(p):
            return 0
        else:
            return 1 + max(self.height(i) for i in self.children(p))
    def __iter__(self):
        for p in self.positions():
            yield p.element()
    def preorder(self):
        if not self.is_empty():
            for p in self._subtree_preorder(self.root()):
                yield p
    def _subtree_prorder(self, p):
        yield p
        for c in self.children(p):
            for other in self._subtree_prorder(c):
                yield other
    def positions(self):
        return self.preorder()

    def postorder(self):
        if not self.is_empty():
            for p in self._subtree_postorder(self.root()):
                yield p
    def _subtree_postorder(self, p):
        for c in self.children(p):
            for other in self._subtree_postorder(c):
                yield other
        yield p
    def breadthfirst(self):
        if not self.is_empty():
            fringe = LinkedQueue(1)
            fringe.enqueue(self.root())
            while not fringe.is_empty():
                p = fringe.dequeue()
                yield p
                for c in self.children(p):
                    fringe.enqueue(c)
# BinaryTree ADT
# T.left(p): return the position
# T.right(p):
# T.sibling(p): 
class BinaryTree(Tree):
    def left(self, p):
        raise NotImplementedError
    def right(self, p):
        raise NotImplementedError
    def sibling(self, p):
        parent = self.parent(p)
        if not parent:
            return None
        if self.left(parent) == p:
            return self.right(parent)
        else:
            return self.left(parent)
    def children(self, p):
        if self.left(p):
            yield self.left(p)
        if self.right(p):
            yield self.right(p)

# LinkedBinaryTree
# T.add_root(e)
# T.add_left(p, e)
# T.add_right(p, e)
# T.replace(p, e)
# T.delete(p): error if has 2 children
# T.attach(p, T1, T2): error if p is not a leaf

class LinkedBinaryTree(BinaryTree):
    class _Node:
        __slots__ = '_element', '_parent', '_left', '_right'
        def __init__(self, element, parent=None, left=None, right=None):
            self._element = element
            self._parent = parent
            self._left = left
            self._right = right

    class Position(BinaryTree.Position):
        def __init__(self, container, node):
            self._container = container
            self._node = node

        def element(self):
            return self._node._element
        
        def __eq__(self, other):
            return type(other) is type(self) and other._node is self._node
    
    def _validate(self, p):
        if not isinstance(p, self.Position):
            raise TypeError
        if p._container is not self:
            raise ValueError
        if p._node._parent is p._node:
            raise ValueError
        return p._node
    
    def _make_position(self, node):
        return self.Position(self, node) if node is not None else None

    def __init__(self):
        self._root = None
        self._size = 0
    
    def __len__(self):
        return self._size

    def root(self):
        return self._make_position(self._root)
    
    def parent(self, p):
        node = self._validate(p)
        return self._make_position(node._parent)

    def left(self, p):
        node = self._validate(p)
        return self._make_position(node._left)

    def right(self, p):
        node = self._validate(p)
        return self._make_position(node._right)

    def num_children(self, p):
        node = self._validate(p)
        count = 0
        if node._left:
            count += 1
        elif node._right:
            count += 1
        return count

    def _add_root(self, e):
        if self._root:
            raise ValueError
        self._size = 1
        self._root = self._Node(e)
        return self._make_position(self._root)

    def _add_left(self, p, e):
        node = self._validate(p)
        if node._left:
            raise ValueError
        self._size += 1
        node._left = self._Node(e, node)
        return self._make_position(node._left)

    def _delete(self, p):
        node = self._validate(p)
        if self.num_children(p) == 2:
            raise ValueError
        child = node._left if node._left else node._right
        if child:
            child._parent = node._parent
        if node is self._root:
            self._root = child
        else:
            parent = node._parent
            if node is parent._left:
                parent._left = child
            else:
                parent._right = child
        self._size -= 1
        node._parent = node
        return node._element

# preorder traversal
