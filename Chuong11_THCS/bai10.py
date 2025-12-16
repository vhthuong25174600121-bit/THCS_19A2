m = int(input("Nhập số hàng: "))
n = int(input("Nhập số cột: "))
a = []

for i in range(m):
    a.append(list(map(int, input().split())))

max_sum = None
hang = 0

for i in range(m):
    tong = 0
    for j in range(n):
        tong += a[i][j]
    if max_sum is None or tong > max_sum:
        max_sum = tong
        hang = i

print("Hàng có tổng lớn nhất:", hang)