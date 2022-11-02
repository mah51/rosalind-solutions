with open("./datasets/13. IEV.txt") as IEV_data:
    a, b, c, d, e, f = [int(i) for i in IEV_data.read().strip().split()]
    print((a + b + c + (0.75*d) + (0.5*e))*2)
