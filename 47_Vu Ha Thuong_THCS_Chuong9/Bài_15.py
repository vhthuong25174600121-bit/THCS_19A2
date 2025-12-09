def la_so_nguyen_to(n):
    if n < 2:
        return False
    for i in range(2, int(n**0.5) + 1):
        if n % i == 0:
            return False
    return True

n = 29
print(la_so_nguyen_to(n))

ds = [x for x in range(100, 501) if la_so_nguyen_to(x)]
print(ds)