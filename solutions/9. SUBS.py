with open("./datasets/9. SUBS.txt") as DNA_input:
    sequence, sub_seq = DNA_input.read().split("\n")
    matches = []
    for idx in range(0, len(sequence) - len(sub_seq) + 2):
        if sequence[idx::].startswith(sub_seq):
            matches.append(str(idx + 1))
    print(' '.join(matches))
