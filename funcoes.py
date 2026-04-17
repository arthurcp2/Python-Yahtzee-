import random
def rolar_dados(n):
    l = []
    for i in range(n):
        l.append(random.randint(1, 6))
    return l