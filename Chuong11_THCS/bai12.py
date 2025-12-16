m = int(input("Nhập m: "))
n = int(input("Nhập n: "))
p = int(input("Nhập p: "))

A = []
B = []

for i in range(m):
    A.append(list(map(int, input().split())))

for i in range(n):
    B.append(list(map(int, input().split())))

C = [[0]*p for _ in range(m)]

for i in range(m):
    for j in range(p):
        for k in range(n):
            C[i][j] += A[i][k] * B[k][j]

for row in C:
    print(row)