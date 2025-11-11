#Nhập số tiền gửi ban đầu và lãi suất hàng năm
tien_gui = float(input("Nhập số tiền gửi (VNĐ): "))
lai_suat = float(input("Nhập lãi suất hàng năm (%): "))
#Chuyển lãi suất sang dạng thập phân
r = lai_suat/100
#Tính lãi đơn
#Tính lãi 1 tháng
lai_1_thang = tien_gui * r * 1/12
#Tính lãi 2 quý (6 tháng)
lai_2_quy = tien_gui * r * 6/12
#Tính lãi 3 năm 
lai_3_nam = tien_gui * r * 3
#In kết quả
print("Lãi sau 1 tháng:", lai_1_thang)
print("Lãi sau 2 quý:", lai_2_quy)
print("Lãi sau 3 năm:", lai_3_nam)