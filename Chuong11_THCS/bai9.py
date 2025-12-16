n = int(input("Nhập n: "))
a = []

for i in range(n):
    row = list(map(int, input().split()))
    a.append(row)

tong = 0
for i in range(n):
    tong += a[i][n - 1 - i]

print("Tổng:", tong)