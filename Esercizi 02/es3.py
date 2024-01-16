def potenze(base, maxexp):
    ret = []
    for i in range(1, maxexp + 1):
        ret.append(base**i)
    return ret

def potenzev2(base, maxexp):
    ret = []
    for i in range(1, maxexp + 1):
        ret.extend([base**i])
    return ret

def potenzev3(base, maxexp):
    ret = []
    for i in range(1, maxexp + 1):
        ret += [base**i]
    return ret

print(potenze(2, 10))
print(potenzev2(2, 10))
print(potenzev3(2, 10))
