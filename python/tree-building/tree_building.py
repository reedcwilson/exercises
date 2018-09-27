class Record():
    def __init__(self, record_id, parent_id):
        self.record_id = record_id
        self.parent_id = parent_id


class Node():
    def __init__(self, node_id):
        self.node_id = node_id
        self.children = []


def ensure_valid(rec):
    equal = rec.record_id == rec.parent_id
    if (
        (equal and rec.record_id != 0) or
        (not equal and not rec.record_id > rec.parent_id)
    ):
        raise ValueError("Invalid record")


def get_parts(records):
    parents = {}
    nodes = {}
    for r in records:
        ensure_valid(r)
        nodes[r.record_id] = Node(r.record_id)
        parents[r.record_id] = r.parent_id
    return parents, nodes


def BuildTree(records):
    head_id = 0
    head = None
    parents, nodes = get_parts(records)
    for i, rid in enumerate(sorted(r.record_id for r in records)):
        if rid != i:
            raise ValueError("Invalid record_id")
        if rid == head_id:
            head = nodes[rid]
        else:
            nodes[parents[rid]].children.append(nodes[rid])
    return head
