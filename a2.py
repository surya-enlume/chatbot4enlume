def get_length(dna):
    """ (str) -> int

    Return the length of the DNA sequence dna.

    >>> get_length('ATCGAT')
    6
    >>> get_length('ATCG')
    4
    """
    return len(dna)

def is_longer(dna1, dna2):
    """ (str, str) -> bool

    Return True if and only if DNA sequence dna1 is longer than DNA sequence
    dna2.

    >>> is_longer('ATCG', 'AT')
    True
    >>> is_longer('ATCG', 'ATCGGA')
    False
    """
    return len(dna1)>len(dna2)

def count_nucleotides(dna, nucleotide):
    """ (str, str) -> int

    Return the number of occurrences of nucleotide in the DNA sequence dna.

    >>> count_nucleotides('ATCGGC', 'G')
    2
    >>> count_nucleotides('ATCTA', 'G')
    0
    """
    return dna.count(nucleotide)

def contains_sequence(dna1, dna2):
    """ (str, str) -> bool

    Return True if and only if DNA sequence dna2 occurs in the DNA sequence
    dna1.

    >>> contains_sequence('ATCGGC', 'GG')
    True
    >>> contains_sequence('ATCGGC', 'GT')
    False

    """
    return dna2 in dna1

def is_valid_sequence(dna):
    """(str) -> bool

    Return true if it contains only 'A','C','G','T' in the sequence

    """

    valid = True
    chars = ['A','C','T','G']
    for char in dna:
        if char not in chars:
            valid = False
    return valid

def insert_sequence(dna1, dna2, given):
    """(str,str,int) -> str

    Return true if it contains only 'A','C','G','T' in the sequence

    >>> insert_sequence('CCGG','AT',2)
    CCATGG
    """
    return dna1[:given]+dna2+dna1[given:]

def get_complement(dna):
    """(str) -> str

    Return complement string

    >>>get_complement('ATCG')
    TAGC
    """

    if dna is 'A':
        return 'T'
    elif dna is 'T':
        return 'A'
    elif dna is 'C':
        return 'G'
    elif dna is 'G':
        return 'C'
    else :
        return None
    
    
def get_complementary_sequence(dna):
    """(str) -> str

    Return complement string

    >>>get_complementary_sequence('ATCG')
    TAGC
    """
    s = list(dna)
    for idx, char in enumerate(s):
        if char is 'A':
            s[idx] = 'T'
        elif char is 'T':
            s[idx] = 'A'
        elif char is 'C':
            s[idx] = 'G'
        elif char is 'G':
            s[idx] = 'C'

    return "".join(s)
            
    





