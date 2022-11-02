from Bio.Data import CodonTable

with open("./datasets/8. PROT.txt") as DNA_input:
    DNA_string = DNA_input.read().strip()
    rna_table = CodonTable.standard_rna_table
    codon_table, stop_codons = rna_table.forward_table, rna_table.stop_codons
    protein = ""
    for idx in range(0, len(DNA_string), 3):
        codon = DNA_string[idx:idx + 3]
        if codon in stop_codons:
            break
        protein += codon_table[codon]
    print(protein)
