n = int(input("Nhập số nguyên n: "))

dem = 0
tong = 0
bien = n

while bien > 0:
    chu_so = bien % 10       
    tong += chu_so         
    dem += 1                
    bien //= 10        
          
print("Số chữ số:", dem, "Tổng chữ số:", tong)