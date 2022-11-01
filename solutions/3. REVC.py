with open("./datasets/3. REVC.txt") as DNA_input:
    nucleotide_mapping = {"A": "T", "C": "G", "G": "C", "T": "A"}
    print(''.join([nucleotide_mapping[base] for base in DNA_input.read().strip()][::-1]))
