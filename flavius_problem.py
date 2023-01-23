def flavius_problem(n, k):
    inp = list(range(1, n+1))
    i = k-1
    while len(inp) > 2: # edit for k > 4
        inp.extend(inp[:i])
        inp = inp[i+1:]
    return inp[k%2] # edit for k > 4
flavius_problem(41,3)