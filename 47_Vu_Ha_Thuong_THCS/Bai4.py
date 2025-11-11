#Nhập số tiền bằng đơn vị VNĐ
tien_VNĐ = int(input("Nhập số tiền (VNĐ): "))
#Tỷ giá
ty_gia = 24500
#Đổi tiền từ VNĐ sang USD
tien_USD = tien_VNĐ/ty_gia
#In kết quả
print("Số tiền tương đương(USD):",round(tien_USD, 2))

                     