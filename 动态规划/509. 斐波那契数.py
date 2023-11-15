def fib(n: int) -> int:
    res = [0, 1]
    if n <= 1:
        return n
    else:
        for i in range(2, n + 1):
            res.append(res[i - 1] + res[i - 2])
    return res[n]


if __name__ == "__main__":
    print(fib(4))
