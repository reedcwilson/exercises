class Node(object):
    def __init__(self, v):
        self.v = v
        self.n = None
        self.p = None


class LinkedList(object):
    def __init__(self):
        self.h = None
        self.t = None
        self.s = 0

    def __len__(self):
        return self.s

    def __iter__(self):
        cur = self.h
        while cur:
            yield cur.v
            cur = cur.n

    def push(self, v):
        n = Node(v)
        if not self.t:
            self.h = self.t = n
        else:
            n.p = self.t
            self.t.n = self.t = n
        self.s += 1

    def pop(self):
        n = self.t
        if self.t:
            self.t = n.p
            if self.t:
                self.t.n = None
        self.s -= 1
        return n.v

    def unshift(self, v):
        n = Node(v)
        if not self.h:
            self.h = self.t = n
        else:
            n.n = self.h
            self.h.p = self.h = n
        self.s += 1

    def shift(self):
        n = self.h
        if self.h:
            self.h = n.n
            if self.h:
                self.h.p = None
        self.s -= 1
        return n.v
