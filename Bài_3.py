def kiem_tra_so_armstrong(n):
    s = str(n)
    tong = sum(int(ch) ** 3 for ch in s)
    return tong == n

print(kiem_tra_so_armstrong(153))
print(kiem_tra_so_armstrong(123))
