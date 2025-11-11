# Nhập số kWh
so_kwh = int(input("Nhập số kWh điện đã tiêu thụ: "))

# Đơn giá
bac1 = 1678
bac2 = 1734
bac3 = 2014

# Tính kWh tương ứng từng bậc (không dùng if)
kwh_bac1 = min(so_kwh, 100)
kwh_bac2 = min(max(so_kwh - 100, 0), 100)
kwh_bac3 = min(max(so_kwh - 200, 0), 100)

# Tổng tiền
tong_tien = kwh_bac1 * bac1 + kwh_bac2 * bac2 + kwh_bac3 * bac3

# In kết quả
print("Tổng tiền điện phải trả:", tong_tien, "VNĐ")