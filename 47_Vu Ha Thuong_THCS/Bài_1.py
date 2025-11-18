n = int(input("Nhập số n: "))
if n < 0:
    print("Không phải số chính phương")
else:
     k = int(n**0.5)
     if k*k == n:
          print("Là số chính phương")
     else:
          print("Không là số chính phương")     
    