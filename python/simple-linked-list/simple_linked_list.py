class EmptyListException(Exception):
    pass


class Node(object):
    def __init__(self, value, nxt=None):
        self.__value = value
        self.__next = nxt

    def value(self):
        return self.__value

    def next(self):
        return self.__next


class LinkedList(object):
    def __init__(self, values=[]):
        self.__head = None
        self.__len = 0
        for v in values:
            self.push(v)

    def __len__(self):
        return self.__len

    def __iter__(self):
        cur = self.__head
        while cur:
            yield cur.value()
            cur = cur.next()

    def head(self):
        if not self.__head:
            raise EmptyListException('empty')
        return self.__head

    def push(self, value):
        if not self.__head:
            self.__head = Node(value)
        else:
            self.__head = Node(value, self.__head)
        self.__len += 1

    def pop(self):
        if not self.__head:
            raise EmptyListException('empty')
        n = self.__head
        self.__head = n.next()
        self.__len -= 1
        return n.value()

    def reversed(self):
        return LinkedList(list(self))
