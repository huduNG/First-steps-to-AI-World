s = input("Nhap chuoi cua ban: ")
words = [word for word in s.split(" ")]
print (" ".join(sorted(list(set(words)))))
# chua loai bo tu lap va sap xep lai
