n = int(input("Nhập n: "))

print(f"Các số nguyên tố nhỏ hơn {n} là:")
for num in range(2, n):
    is_prime = True
    for i in range(2, num):  
        if num % i == 0:
            is_prime = False
            break
    if is_prime:
        print(num, end=" ")