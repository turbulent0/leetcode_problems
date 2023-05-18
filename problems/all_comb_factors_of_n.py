
def getFactors(n):
    todo, combis = [(n, 2, [])], []
    while todo:
        n, idx, combi = todo.pop()
        while idx * idx <= n:
            if n % idx == 0:
                quotient = n/idx
                combis += combi + [idx, quotient],
                rest = combi+[idx]
                todo += (quotient, idx, rest),
            idx += 1
    return combis
getFactors(12)

def getFactors(n):
    def factorRec(n, i, combi, combis):
        while i * i <= n:
            if n % i == 0:
                combis += combi + [i, n/i],
                factorRec(n/i, i, combi+[i], combis)
            i += 1
        return combis
    return factorRec(n, 2, [], [])



