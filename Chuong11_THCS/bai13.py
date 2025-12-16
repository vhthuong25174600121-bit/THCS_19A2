n = int(input("Nhập n: "))
a = []

for i in range(n):
    a.append(list(map(int, input().split())))

la_don_vi = True
for i in range(n):
    for j in range(n):
        if i == j and a [i][j] != 1:
            la_don_vi = False
        if i != j and a[i][j] != 0:
            la_don_vi = False

print(la_don_vi)