with open("./datasets/11. FIBD.txt") as FIBD_input:
    months, lifespan = [int(i) for i in FIBD_input.read().strip().split()]
    rabbits_ages = [0 for _ in range(1, lifespan+1)]
    rabbits_ages[0] = 1

    for i in range(months - 1):
        rabbits_ages = [sum(rabbits_ages[1:]),] + rabbits_ages[:-1]
    print(sum(rabbits_ages))
