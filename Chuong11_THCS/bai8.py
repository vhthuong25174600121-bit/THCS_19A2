a = list(map(int, input("Nhập danh sách: ").split()))
k = int(input("Nhập k: "))

n = len(a)
k = k % n
b = [0]*n

for i in range(n):
    b[(i + k) % n] = a[i]

print(b)