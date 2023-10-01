import pandas as pd
import numpy as np
import numba
df = pd.DataFrame(
    {
        "a": np.random.randn(1000000),
        "b": np.random.randn(1000000),
        "N": np.random.randint(100, 1000, (1000000)),
        "x": "x",
    }
)


@numba.jit(nopython=True)
def f_plain(x):
    return x * (x - 1)


@numba.jit(nopython=True)
def integrate_f_numba(a, b, N):
    s = 0
    dx = (b - a) / N
    for i in range(N):
        s += f_plain(a + i * dx)
    return s * dx


@numba.jit(nopython=True)
def apply_integrate_f_numba(col_a, col_b, col_N):
    n = len(col_N)
    result = np.empty(n, dtype="float64")
    assert len(col_a) == len(col_b) == n
    for i in range(n):
        result[i] = integrate_f_numba(col_a[i], col_b[i], col_N[i])
    return result


def compute_numba(df):
    result = apply_integrate_f_numba(
        df["a"].to_numpy(), df["b"].to_numpy(), df["N"].to_numpy()
    )
    return pd.Series(result, index=df.index, name="result")

print(compute_numba(df)[:10])