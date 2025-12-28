# Tạo danh sách số nguyên
ds_so = [1, 3, 5, 7, 9, 11, 13]

# Mở file để ghi
with open("so_nguyen.txt", "w", encoding="utf-8") as f:
    for so in ds_so:
        f.write(str(so) + "\n")