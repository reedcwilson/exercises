

translations = {
    'g': 'c',
    'c': 'g',
    't': 'a',
    'a': 'u',
}


def translate(nucleotide):
    n = nucleotide.lower()
    if n not in translations:
        raise ValueError('Unknown chemical found {}'.format(nucleotide))
    return translations[n].upper()


def to_rna(dna_strand):
    return "".join([translate(n) for n in dna_strand])


def to_rna_translate(dna_strand):
    if any([n.upper() not in 'ATGC' for n in dna_strand]):
        raise ValueError('Unknown chemical found: {}'.format(dna_strand))
    return dna_strand.upper().translate(str.maketrans('ATGC', 'UACG'))
