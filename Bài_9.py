def tinh_tong_chu_so(n):
    tong = 0
    for ch in str(n):
        tong += int(ch)
    return tong

print(tinh_tong_chu_so(12345))
