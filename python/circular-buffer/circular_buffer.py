from queue import Queue


class BufferFullException(Exception):
    pass


class BufferEmptyException(Exception):
    pass


class CircularBuffer(object):
    def __init__(self, capacity):
        self.buf = Queue(capacity)

    def write(self, el):
        if self.buf.full():
            raise BufferFullException('full...')
        self.buf.put(el)

    def read(self):
        if self.buf.empty():
            raise BufferEmptyException("empty...")
        return self.buf.get()

    def overwrite(self, el):
        if self.buf.full():
            self.buf.get()
        self.write(el)

    def clear(self):
        while not self.buf.empty():
            self.buf.get()
