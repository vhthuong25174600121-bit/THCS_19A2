#Nhập tổng số kẹo và số học sinh
tong_so_keo = int(input("Nhập tổng số kẹo: "))
so_hoc_sinh = int(input("Nhập tổng số học sinh: "))
#Tính số kẹo mỗi học sinh nhận được 
keo_moi_hoc_sinh = tong_so_keo//so_hoc_sinh
#Tính số kẹo còn thừa 
keo_con_thua = tong_so_keo%so_hoc_sinh
#In kết quả
print("Mỗi học sinh nhận được:", keo_moi_hoc_sinh, "kẹo")
print("Số kẹo còn thừa:",keo_con_thua, "kẹo")
