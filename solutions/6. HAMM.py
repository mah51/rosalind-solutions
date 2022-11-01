with open("./datasets/6. HAMM.txt") as sequences:
    sequence1, sequence2 = sequences.readline().strip(), sequences.readline().strip()
    if len(sequence1) != len(sequence2):
        raise Exception("Sequences are not the same length")
    HAMM_count = 0
    for idx in range(0, len(sequence1)):
        if sequence1[idx] != sequence2[idx]:
            HAMM_count += 1

    print(HAMM_count)
