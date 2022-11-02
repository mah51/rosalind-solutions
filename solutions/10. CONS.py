import re

profile = {"A": [],  "C": [], "G": [], "T": []}

with open("./datasets/10. CONS.txt") as FASTA_input:
    sequences = [sequence.group(2).strip().replace("\n", "") for sequence in re.finditer(">Rosalind_(\d+)\n([\w|\n]+)", FASTA_input.read())]
    consensus = ""
    for idx in range(len(sequences[0])):
        bases = {"A":0,"C":0,"G":0,"T":0}
        for seq in sequences:
            bases[seq[idx]] += 1
        for base in profile:
            profile[base].append(bases[base])
        consensus += max(bases, key=bases.get)
    print(consensus)
    for base in profile:
        print(f"{base}: {' '.join([str(i) for i in profile[base]])}")


    

