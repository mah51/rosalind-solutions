import re


def check_overlap(a, b):
    if b[:3] == a[-3:]:
        return True
    return False

with open("./datasets/12. GRPH.txt") as FASTA_input:
    sequences = {
        sequence.group(1): sequence.group(2).strip().replace("\n", "") 
        for sequence in re.finditer(">Rosalind_(\d+)\n([\w|\n]+)", FASTA_input.read())
    }

    with open("./output.txt", "w") as output:
        for seq_a in sequences:
            for seq_b in sequences:
                if sequences[seq_a] == sequences[seq_b]:
                    continue
                if check_overlap(sequences[seq_a], sequences[seq_b]):
                    output.write(f"Rosalind_{seq_a} Rosalind_{seq_b}\n")
    


    