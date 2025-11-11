#Nhập tên đăng nhập và mật khẩu
ten = input("Nhập tên đăng nhập: ")
mat_khau = input("Nhập mật khẩu: ")
#Kiểm tra
quyen_truy_cap = (ten == "admin") and (mat_khau != "password123")
#In kết quả
print("Quyền truy cập:", quyen_truy_cap)
