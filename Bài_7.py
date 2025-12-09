def la_so_hoan_hao(n):
    tong = 0
    for i in range(1, n):
        if n % i == 0:
            tong += i
    return tong == n


def tinh_tong_so_hoan_hao(a, b):
    tong = 0
    for x in range(a, b + 1):
        if la_so_hoan_hao(x):
            tong += x
    return tong

print([x for x in range(1, 1000) if la_so_hoan_hao(x)])
print(tinh_tong_so_hoan_hao(1, 1000))