a = list(map(int, input("Nhập danh sách: ").split()))

tong_chan = 0
tong_le = 0

for x in a:
    if x % 2 == 0:
        tong_chan += x
    else:
        tong_le += x

print("Tổng chẵn:", tong_chan)
print("Tổng lẻ:", tong_le)