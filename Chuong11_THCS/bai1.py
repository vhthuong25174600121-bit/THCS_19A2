s = input("Nhập chuỗi: ")

chu = 0
so = 0
dac_biet = 0

for ch in s:
    if ('a' <= ch <= 'z') or ('A' <= ch <= 'Z'):
        chu += 1
    elif '0' <= ch <= '9':
        so += 1
    else:
        dac_biet += 1

print("Chữ cái:", chu)
print("Chữ số:", so)
print("Ký tự đặc biệt:", dac_biet)