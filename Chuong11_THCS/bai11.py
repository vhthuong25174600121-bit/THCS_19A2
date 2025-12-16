n = int(input("Nhập n: "))
a = []

for i in range(n):
    a.append(list(map(int, input().split())))

doi_xung = True
for i in range(n):
    for j in range(n):
        if a[i][j] != a[j][i]:
            doi_xung = False

print(doi_xung)