# Bước 1: tạo file san_pham.txt
with open("san_pham.txt", "w", encoding="utf-8") as f:
    f.write("ID, Tên sản phẩm, Giá\n")
    f.write("1, Laptop, 1200\n")
    f.write("2, Chuột máy tính, 25\n")
    f.write("3, Bàn phím, 75\n")

# Bước 2: nhập ID cần cập nhật
id_can_sua = input("Nhập ID sản phẩm cần cập nhật giá: ")

# Bước 3: nhập giá mới
gia_moi = input("Nhập giá mới: ")

# Bước 4: đọc file và cập nhật dữ liệu
danh_sach_moi = []

with open("san_pham.txt", "r", encoding="utf-8") as f:
    for dong in f:
        dong = dong.strip()

        # giữ nguyên dòng tiêu đề
        if dong.startswith("ID"):
            danh_sach_moi.append(dong)
            continue

        phan = dong.split(", ")

        if phan[0] == id_can_sua:
            dong_moi = f"{phan[0]}, {phan[1]}, {gia_moi}"
            danh_sach_moi.append(dong_moi)
        else:
            danh_sach_moi.append(dong)

# Bước 5: ghi đè lại file
with open("san_pham.txt", "w", encoding="utf-8") as f:
    for dong in danh_sach_moi:
        f.write(dong + "\n")

print("Đã cập nhật giá sản phẩm thành công!")