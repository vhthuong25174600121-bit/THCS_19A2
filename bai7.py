import os

# Tạo thư mục gốc
thu_muc_goc = "du_an_mau"

# Tạo các thư mục con
os.makedirs(os.path.join(thu_muc_goc, "du_lieu"), exist_ok=True)
os.makedirs(os.path.join(thu_muc_goc, "ma_nguon"), exist_ok=True)

# Tạo các file rỗng
open(os.path.join(thu_muc_goc, "README.txt"), "w").close()
open(os.path.join(thu_muc_goc, "ma_nguon", "main.py"), "w").close()
open(os.path.join(thu_muc_goc, "du_lieu", "data.txt"), "w").close()

# In cấu trúc thư mục
print("Cấu trúc thư mục đã tạo:\n")

for muc in os.listdir(thu_muc_goc):
    duong_dan = os.path.join(thu_muc_goc, muc)
    if os.path.isdir(duong_dan):
        print(f"[Thư mục] {muc}")
        for tep in os.listdir(duong_dan):
            print("   -", tep)
    else:
        print("[Tập tin]", muc)