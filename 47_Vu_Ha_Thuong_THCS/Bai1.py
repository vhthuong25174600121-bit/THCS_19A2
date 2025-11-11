#Nhập giá sản phẩm và số lượng mua 
gia_san_pham = float(input("Nhập giá sản phẩm: "))
so_luong = int(input("Nhập số lượng mua: "))
#Tổng chi phí trước thuế
tong_chi_phi = gia_san_pham * so_luong
#Tính thuế VAT
thue_VAT = tong_chi_phi * 0.10
#Tổng tiền phải trả
tong_tien = tong_chi_phi + thue_VAT
#In kết quả , làm tròn đén 2 chữ số thập phân
print("Tổng tiền phải trả(bao gồm VAT 10%):", round(tong_tien, 2))