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

    count1 = 0
    count2 = 0
    
    for nucleotide in dna1:
        count1 += 1
    for nucleotide in dna2:
        count2 += 1
    
    return count1 > count2


def count_nucleotides(dna, nucleotide):
    """ (str, str) -> int

    Return the number of occurrences of nucleotide in the DNA sequence dna.

    >>> count_nucleotides('ATCGGC', 'G')
    2
    >>> count_nucleotides('ATCTA', 'G')
    0
    """

    count_nucleotide = 0
    
    for nucleo in dna:
        if nucleo == nucleotide:
            count_nucleotide += 1

    return count_nucleotide

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

def is_valid_sequence(dna_sequence):
    """ (str) -> bool
    
    Return True if and only if dna_sequence contais no characters other than 'A', 'T', 'C' and 'G'.
    A string is not a valid DNA sequence if it contais lowecase letters.
    
    >>> is_valid_sequence('ATCGAC')
    True
    >>> is_valid_sequence('BEKBOS')
    False
    """
    
    valid_nucleotides =  'ATCG'
    status = True
    for nucleotide in dna_sequence:
        if not nucleotide in valid_nucleotides:
            status = False
    
    return status

def insert_sequence(dna_sequence1, dna_sequence2, index):
    """ (str, str, int) -> str
    
    Return the DNA sequence obtained by inserting the second DNA sequence into the first DNA sequence at the given index (assuming the index is valid).
    
    >>> insert_sequence('CCGG', 'AT', 2)
    'CCATGG'
    """
    
    return dna_sequence1[:index] + dna_sequence2 + dna_sequence1[index:]

def get_complement(nucleotide):
    """ (str) -> str
    
    Return the nucleotide's complement
    
    >>> get_complement('A')
    'T'
    >>> get_complement('C')
    'G'
    """
    
    if nucleotide == 'A':
        return 'T'
    elif nucleotide == 'T':
        return 'A'
    elif nucleotide == 'C':
        return 'G'
    elif nucleotide == 'G':
        return 'C'

def get_complementary_sequence(dna_sequence):
    """ (str) -> str
    
    Return the DNA sequence that is complementary to the given DNA sequence
    
    >>> get_complementary_sequence('AT')
    'TA'
    """
    
    complementary_sequence = ''
    
    for nucleotide in dna_sequence:
        if nucleotide == 'A':
            complementary_sequence += 'T'
        elif nucleotide == 'T':
            complementary_sequence += 'A'
        elif nucleotide == 'C':
            complementary_sequence += 'G'
        elif nucleotide == 'G':
            complementary_sequence += 'C'
    
    return complementary_sequence

