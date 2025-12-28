import csv

# Bước 1 + 2: tạo file CSV và ghi dữ liệu
with open("nhan_vien.csv", "w", newline="", encoding="utf-8") as f:
    writer = csv.writer(f)
    writer.writerow(["ID", "Tên", "Lương"])
    writer.writerow([1, "An", 45000])
    writer.writerow([2, "Bình", 60000])
    writer.writerow([3, "Chi", 52000])
    writer.writerow([4, "Dũng", 40000])

# Bước 3 + 4: đọc file bằng DictReader
with open("nhan_vien.csv", "r", encoding="utf-8") as f:
    reader = csv.DictReader(f)

    print("Nhân viên có lương trên 50000:")
    for dong in reader:
        if int(dong["Lương"]) > 50000:
            print(f"ID: {dong['ID']}, Tên: {dong['Tên']}, Lương: {dong['Lương']}")