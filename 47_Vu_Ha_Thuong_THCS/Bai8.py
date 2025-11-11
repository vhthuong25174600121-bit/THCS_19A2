#Nhập cân nặng và chiều cao
can_nang = float(input("Nhập số cân nặng (kg): "))
chieu_cao = float(input("Nhập số chiều cao (m): "))
#Tính BMI
BMI = can_nang/(chieu_cao*chieu_cao)
#In kết quả
print("Kết quả của BMI:", round(BMI, 2))