s = input("Nhập chuỗi: ")

ket_qua = ""
dang_truoc_la_space = False

for ch in s:
    if ch != ' ':
        ket_qua += ch
        dang_truoc_la_space = False
    else:
        if not dang_truoc_la_space:
            ket_qua += ' '
            dang_truoc_la_space = True

print(ket_qua)