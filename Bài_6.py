def la_so_nguyen_to(n):
    if n < 2:
        return False
    for i in range(2, int(n**0.5) + 1):
        if n % i == 0:
            return False
    return True


def in_so_nguyen_to_trong_khoang(a, b):
    ds = []
    for x in range(a, b + 1):
        if la_so_nguyen_to(x):
            ds.append(x)
    return ds

print(la_so_nguyen_to(17))
print(in_so_nguyen_to_trong_khoang(10, 30))

