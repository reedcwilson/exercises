#!/usr/bin/env python
import os


class SinglyLinkedListNode:
    def __init__(self, node_data):
        self.data = node_data
        self.next = None


class SinglyLinkedList:
    def __init__(self):
        self.head = None
        self.tail = None

    def insert_node(self, node_data):
        node = SinglyLinkedListNode(node_data)

        if not self.head:
            self.head = node
        else:
            self.tail.next = node

        self.tail = node


def print_singly_linked_list(node, sep, fptr):
    while node:
        fptr.write(str(node.data))

        node = node.next

        if node:
            fptr.write(sep)


# ### start user code section ###


def getNumber(node):
    # Write your code here
    string = ''
    while node:
        string += str(node.data)
        node = node.next
    num = 0
    for i, n in enumerate(reversed(string)):
        num += int(n) << i
    return num


# ### end user code section ###


if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')

    binary_count = int(input().strip())

    binary = SinglyLinkedList()

    for _ in range(binary_count):
        binary_item = int(input().strip())
        binary.insert_node(binary_item)

    result = getNumber(binary.head)

    fptr.write(str(result) + '\n')
    print(str(result))

    fptr.close()
