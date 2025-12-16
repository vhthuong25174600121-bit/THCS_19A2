sv = {'An': 8, 'Binh': 9, 'Chi': 8}
kq = {}

for ten in sv:
    diem = sv[ten]
    if diem not in kq:
        kq[diem] = [ten]
    else:
        kq[diem].append(ten)

print(kq)