import re

with open("./datasets/5. GC.txt") as FASTA_input:
    matches = re.finditer(">Rosalind_(\d{4})\n([\w|\n]+)", FASTA_input.read())
    results = {}
    for i in matches:
        id, sequence = i.groups()
        sequence = sequence.replace("\n", "")
        results[id] = ((sequence.count("G") + sequence.count("C")) / len(sequence)) * 100
    max_id = max(results, key=results.get)
    print(f"Rosalind_{max_id}\n{results[max_id]}")
