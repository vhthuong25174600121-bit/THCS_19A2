a = list(map(int, input("Nhập danh sách: ").split()))
b = []

for x in a:
    da_ton_tai = False
    for y in b:
        if x == y:
            da_ton_tai = True
            break
    if not da_ton_tai:
        b.append(x)

print(b)