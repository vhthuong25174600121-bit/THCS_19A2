# Mở và đọc nội dung file
with open("van_ban.txt", "r", encoding="utf-8") as f:
    noi_dung = f.read()

# Tách các từ (đưa về chữ thường)
cac_tu = noi_dung.lower().split()

# Tạo từ điển đếm tần suất
tan_suat = {}

# Duyệt từng từ và cập nhật từ điển
for tu in cac_tu:
    # loại bỏ dấu câu cơ bản
    tu = tu.strip(".,!?:;")

    if tu in tan_suat:
        tan_suat[tu] += 1
    else:
        tan_suat[tu] = 1

# In kết quả
print("Tần suất xuất hiện của các từ:\n")
for tu, so_lan in tan_suat.items():
    print(f"{tu}: {so_lan}")