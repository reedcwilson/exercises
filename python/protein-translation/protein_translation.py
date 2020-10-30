pairs = [
    (['AUG'], 'Methionine'),
    (['UGG'], 'Tryptophan'),
    (['UUA', 'UUG'], 'Leucine'),
    (['UAU', 'UAC'], 'Tyrosine'),
    (['UGU', 'UGC'], 'Cysteine'),
    (['UUU', 'UUC'], 'Phenylalanine'),
    (['UCU', 'UCC', 'UCA', 'UCG'], 'Serine'),
]


def proteins(strand):
    codons = [strand[i:i+3] for i in range(0, len(strand), 3)]
    res = []
    for codon in codons:
        if codon in ['UAA', 'UAG', 'UGA']:
            break
        pair = [p for c, p in pairs if codon in c]
        if len(pair) > 0:
            res.append(pair[0])
    return res
