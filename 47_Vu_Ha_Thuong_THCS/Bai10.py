# Nhập dữ liệu
luong_co_ban = float(input("Nhập mức lương cơ bản: "))
so_ngay_cong = int(input("Nhập số ngày công trong tháng: "))

# Lương 1 ngày
luong_1_ngay = luong_co_ban / 22

# Lương chính
luong_chinh = luong_1_ngay * so_ngay_cong

# Tính tiền thưởng (10% nếu trên 22 ngày)
thuong = max(0, so_ngay_cong - 22) * 0.10 * luong_chinh / max(1, so_ngay_cong - 22)  # nếu >22 ngày, =0 nếu <=22

# Tính tiền phạt (5% nếu dưới 22 ngày)
phat = max(0, 22 - so_ngay_cong) * 0.05 * luong_chinh / max(1, 22 - so_ngay_cong)  # nếu <22 ngày, =0 nếu >=22

# Tổng lương thực nhận
tong_luong = luong_chinh + thuong - phat

# In kết quả
print("Tổng lương thực nhận:", tong_luong)