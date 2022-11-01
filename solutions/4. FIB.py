with open("./datasets/4. FIB.txt") as FIB_input:
    n, k = FIB_input.readline().strip().split()
    total_rabbit_pairs = 1
    f1, f2 = 1,1
    for i in range(2, int(n)):
        total_rabbit_pairs = f1 + (f2 * int(k))
        f2 = f1
        f1 = total_rabbit_pairs

    print(total_rabbit_pairs)
