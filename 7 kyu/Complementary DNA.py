def DNA_strand(dna):
    # code here
    
    dict = {
        "A":"T",
        "T":"A",
        "C":"G",
        "G":"C"
    }
    
    return ''.join(dict[a] for a in dna)
