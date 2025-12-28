import os

# 1. Tạo thư mục temp_files
os.makedirs("temp_files", exist_ok=True)

# 2. Tạo file file.txt trong temp_files
duong_dan_file = os.path.join("temp_files", "file.txt")
open(duong_dan_file, "w").close()

# 3. Đổi tên file.txt thành new_file.txt
duong_dan_moi = os.path.join("temp_files", "new_file.txt")
os.rename(duong_dan_file, duong_dan_moi)

# 4. Di chuyển new_file.txt ra thư mục hiện tại
dich = "new_file.txt"
os.rename(duong_dan_moi, dich)

# 5. Xóa thư mục temp_files
os.rmdir("temp_files")

print("Hoàn thành tạo, đổi tên, di chuyển và xóa thư mục.")