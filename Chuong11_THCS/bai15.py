t = tuple(map(int, input("Nhập tuple: ").split()))

chan = []
le = []
tong_chan = 0
tong_le = 0

for x in t:
    if x % 2 == 0:
        chan.append(x)
        tong_chan += x
    else:
        le.append(x)
        tong_le += x

print(tuple(chan), tong_chan)
print(tuple(le), tong_le)