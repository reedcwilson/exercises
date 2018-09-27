from math import ceil, sqrt


def _get_chunks(text, size):
    chunks = []
    chunk = []
    for i in range(len(text)):
        if i > 0 and i % size == 0:
            chunks.append(chunk)
            chunk = []
        chunk.append(text[i])
    if len(chunk) > 0:
        chunk.extend([' '] * (size - len(chunk)))
        chunks.append(chunk)
    return chunks


def encode(text):
    text = ''.join(c for c in text if c.isalnum()).lower()
    size = int(ceil(sqrt(len(text))))
    return ' '.join([''.join(l) for l in zip(*_get_chunks(text, size))])
