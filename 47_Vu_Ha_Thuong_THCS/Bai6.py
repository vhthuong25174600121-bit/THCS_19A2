#Nhập 1 năm
nam = int(input("Nhập 1 năm: "))
#Kiểm tra xem đó phải năm nhuận hay không
nam_nhuan = (nam % 400 == 0) or (nam % 4 == 0 and nam % 100 != 0)
#In kết quả 
print("Năm nhuận ?", nam_nhuan)