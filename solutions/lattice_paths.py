def count_paths(n, k):
    MOD = 10**9 + 7
    inv = [0] * (n + 1)
    if n >= 1:
        inv[1] = 1
    for i in range(2, n + 1):
        inv[i] = (MOD - MOD // i) * inv[MOD % i] % MOD
    ans = n
    curr_comb = 1
    for d in range(1, n):
        curr_comb = (curr_comb * (k + d) % MOD) * inv[d] % MOD
        count = 2 * (n - d) % MOD
        ans = (ans + count * curr_comb) % MOD
    return ans