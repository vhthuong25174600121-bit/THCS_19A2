tu = int(input("Nhập tử số: "))
mau = int(input("Nhập mẫu số: "))
uc = 1
for i in range(1, min(abs(tu), abs(mau)) + 1):
    if tu % i == 0 and mau % i == 0:
        uc = i
tu_gon = tu // uc
mau_gon = mau // uc
print("Phân số tối giản là:", tu_gon, "/", mau_gon)
        