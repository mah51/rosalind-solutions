with open("./datasets/1. DNA.txt") as DNA_input:
    DNA = DNA_input.read()
    print(DNA.count("A"), DNA.count("C"), DNA.count("G"), DNA.count("T"))
