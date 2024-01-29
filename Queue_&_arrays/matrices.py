def matrix_chain_order(p: list) -> tuple:
    n = len(p) - 1
    m = [[0 for _ in range(n)] for _ in range(n)]
    s = [[0 for _ in range(n)] for _ in range(n)]
    for l in range(2, n + 1):
        for i in range(1, n - l + 2):
            j = i + l - 1
            m[i - 1][j - 1] = float("inf")
            for k in range(i, j):
                q = m[i - 1][k - 1] + m[k][j - 1] + p[i - 1] * p[k] * p[j]
                if q < m[i - 1][j - 1]:
                    m[i - 1][j - 1] = q
                    s[i - 1][j - 1] = k
    return m, s


def matrix_chain_order_recursive(p: list, i: int, j: int) -> tuple:
    if i == j:
        return 0
    m = float("inf")
    for k in range(i, j):
        q = matrix_chain_order_recursive(p, i, k) + matrix_chain_order_recursive(p, k + 1, j) + p[i - 1] * p[k] * p[j]
        if q < m:
            m = q
    return m


def main():
    def print_optimal_parens(s: list, i: int, j: int):
        if i == j:
            print("A", end="")
        else:
            print("(", end="")
            print_optimal_parens(s, i, s[i - 1][j - 1])
            print_optimal_parens(s, s[i - 1][j - 1] + 1, j)
            print(")", end="")

    print("Test cases for matrix iterative")
    p1 = [30, 35, 15, 5, 10, 20, 25]
    p2 = [5, 10, 3, 12, 5, 50, 6]
    p3 = [10, 20, 30, 40, 30]
    p4 = [10, 20, 30]
    for p in [p1, p2, p3, p4]:
        print("p: ", p)
        m, s = matrix_chain_order(p)
        print(m)
        print(s)
        print()
        print_optimal_parens(s, 1, len(p) - 1)
        print()

    print("Test cases for matrix recursive")
    p1 = [30, 35, 15, 5, 10, 20, 25]
    p2 = [5, 10, 3, 12, 5, 50, 6]
    p3 = [10, 20, 30, 40, 30]
    p4 = [10, 20, 30]
    for p in [p1, p2, p3, p4]:
        print("p: ", p)
        print(matrix_chain_order_recursive(p, 1, len(p) - 1))
        print()


main()
