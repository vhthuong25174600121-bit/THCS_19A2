# Đường dẫn file nguồn và file đích
nguon = "tep_nguon.bin"
dich = "tep_dich.bin"

# Mở file bằng chế độ nhị phân
with open(nguon, "rb") as f_nguon, open(dich, "wb") as f_dich:
    while True:
        du_lieu = f_nguon.read(1024)   # đọc 1024 byte
        if not du_lieu:
            break
        f_dich.write(du_lieu)

print("Sao chép tập tin thành công!")