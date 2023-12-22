def sum_eo(n, t):
    if t == "e":
        return sum(range(0, n, 2))
    elif t == "o":
        return sum(range(1, n, 2))
    else:
        return -1


x = sum_eo(10, "e")
print(x)
