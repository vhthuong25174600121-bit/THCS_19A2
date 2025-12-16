A = set(map(int, input("A: ").split()))
B = set(map(int, input("B: ").split()))

hieu_A_B = set()
hieu_B_A = set()
giao = set()
hop = set()

for x in A:
    if x in B:
        giao.add(x)
    else:
        hieu_A_B.add(x)
    hop.add(x)

for x in B:
    if x not in A:
        hieu_B_A.add(x)
    hop.add(x)

print("A - B:", hieu_A_B)
print("B - A:", hieu_B_A)
print("Giao:", giao)
print("Hợp:", hop)