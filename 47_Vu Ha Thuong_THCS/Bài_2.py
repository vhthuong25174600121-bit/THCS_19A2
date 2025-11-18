a = int(input("Nhập số thứ nhất: "))
b = int(input("Nhập số thứ hai: "))
min_num = min(a, b)
ucln = 1
for i in range(1, min_num + 1):
    if a % i == 0 and b % i == 0:
        ucln = i
print("UCLN là:", ucln)       