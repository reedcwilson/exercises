
def _flatten(iterable):
    for element in iterable:
        if isinstance(element, (tuple, list)):
            for item in _flatten(element):
                if item is not None:
                    yield item
        else:
            if element is not None:
                yield element


def flatten(iterable):
    return list(_flatten(iterable))
