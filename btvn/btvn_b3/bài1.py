# Nhập số phần tử N
N = int(input("Nhập số phần tử N: "))

# Nhập list số nguyên
list = []
for i in range(N):
    list.append(int(input(f"Nhập phần tử thứ {i}: ")))

# Nhập X và đếm số lần xuất hiện
X = int(input("Nhập số X: "))
print("Số lần X xuất hiện:", list.count(X))

# Thay thế phần tử từ vị trí 2 -> 7 
list[2:8] = [8, 5, 4, 0, 1, 3]
print("List sau khi thay thế:", list)

# Tìm số lớn nhất và nhỏ nhất 
print("Số lớn nhất:", max(list))
print("Số nhỏ nhất:", min(list))

# Nhập Y và chèn vào đầu list
Y = int(input("Nhập số Y: "))
list.insert(0, Y)
print("List sau khi chèn:", list)

# Kiểm tra tăng dần, giảm dần
if list == sorted(list):
    print("TĂNG")
elif list == sorted(list, reverse=True):
    print("GIẢM")
else:
    print("NO")