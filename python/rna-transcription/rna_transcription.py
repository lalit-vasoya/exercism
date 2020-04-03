def to_rna(dna_strand):
    DNA = {'G':'C','C':'G','T':'A','A':'U'}
    rna = ''
    for i in dna_strand:
        rna+=DNA[i]
    return rna