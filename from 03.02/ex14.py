value = []
items=[x for x in input("Nhap cac so nhi phan: ").split(',')]
for p in items:
    intp = int(p, 2)
    if not intp%5:
        value.append(p)
print (','.join(value))
#lam sao de phan biet dc so nghi phan, 1100 co chia het cho 5 k?