def tim_so_le_lon_nhat(a, b, c):
    le = [x for x in (a, b, c) if x % 2 != 0]
    return max(le) if le else -1

print(tim_so_le_lon_nhat(2, 7, 10))
print(tim_so_le_lon_nhat(2, 4, 6))