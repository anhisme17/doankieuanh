thang = int (input("nhập tháng (1-12): "))
nam = int (input("nhập năm: "))

if thang == 2:
    if (nam % 4 == 0 and nam % 100 != 0) or (nam % 400 == 0):
        so_ngay = 29
    else: 
        so_ngay = 28
elif thang in [1, 3, 5, 7, 8, 10]:
    so_ngay = 31
elif thang in [4, 6, 9, 11]:
    so_ngay = 30
else:
    so_ngay = 0

if so_ngay == 0:
    print ("tháng không hợp lệ !")
else: 
    print (f"tháng {thang} năm {nam} có {so_ngay} ngày")