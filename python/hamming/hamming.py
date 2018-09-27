

def distance(strand_a, strand_b):
    if len(strand_a) != len(strand_b):
        raise ValueError(
            'Cannot compute Hamming distance with two unequal length strands'
        )
    return len([1 for i, j in zip(strand_a, strand_b) if i != j])
