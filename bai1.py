with open("van_ban.txt", "w", encoding="utf-8") as f:
    f.write(
        "Python là một ngôn ngữ lập trình mạnh mẽ, dễ học và có nhiều ứng dụng. "
        "Nó được sử dụng rộng rãi trong phát triển web, khoa học dữ liệu, "
        "trí tuệ nhân tạo và tự động hóa. "
        "Cộng đồng Python rất lớn và hỗ trợ tuyệt vời, "
        "với nhiều thư viện phong phú để giải quyết mọi vấn đề."
    )

# Mở file và đọc toàn bộ nội dung
with open("van_ban.txt", "r", encoding="utf-8") as f:
    noi_dung = f.read()

# Đếm số từ
so_tu = len(noi_dung.split())

# In kết quả
print("Nội dung văn bản:")
print(noi_dung)
print("\nTổng số từ trong tập tin:", so_tu)