with open("./datasets/2. RNA.txt") as RNA_input:
    RNA = RNA_input.read()
    print(RNA.replace("T", "U"))
