import re

with open("./datasets/14. LCSM.txt") as FASTA_input:
    sequences = {
        sequence.group(1): sequence.group(2).strip().replace("\n", "") 
        for sequence in re.finditer(">Rosalind_(\d+)\n([\w|\n]+)", FASTA_input.read())
    }

    shortest_sequence_id = min(sequences, key=lambda x: len(sequences[x]))
    shortest_sequence = sequences[shortest_sequence_id]
    del sequences[shortest_sequence_id]
    for size in range(len(shortest_sequence), 0, -1):
        for idx in range(len(shortest_sequence)):
            if (idx + size) > len(shortest_sequence):
                continue
            sub_string = shortest_sequence[idx:idx + size]
            if sub_string == "":
                continue
            sequence_contain_sub = []
            for seq in sequences:
                if sub_string in sequences[seq]:
                    sequence_contain_sub.append(True)
            if len(sequence_contain_sub) == len(sequences):
                print(sub_string)
                import sys
                sys.exit()
                
