def numberOfWays(n: int, x: int) -> int:
    p = 10**9+7
    d = [0 for j in range(n+1)]
    d[0] = 1 
    for new_max in range(1, n+1):
        new_d = [d[i] for i in range(n+1)]
        m = new_max**x 
        for j in range(n+1):
            if j+m <= n:
                new_d[j+m] = (new_d[j+m]+d[j]) % p 
        d = new_d 
    return d[n]


# def numberOfWays2(n: int, x: int) -> int:
#         dp, k = [1] + [0] * n, 1
#         for i in range(1, n + 1):
#             power = i ** x
#             for j in range(n, power - 1, -1):
#                 dp[j] += dp[j - power]
#                 dp[j] %= 10 ** 9 + 7
#         return dp[n]

print(numberOfWays(9, 2))

