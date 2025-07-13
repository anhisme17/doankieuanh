Bài 1:

- Python là ngôn ngữ lập trình thông dịch.
    - Khi chạy một chương trình Python, trình thông dịch sẽ “đọc” từng dòng code, kiểm tra cú pháp, và thực hiện ngay dòng code đó trước khi chuyển sang dòng tiếp theo. Thay vì dịch toàn bộ code thành một file thực thi duy nhất rồi mới chạy (như cách các ngôn ngữ biên dịch hoạt động).


Bài 2:
- Các kiểu dữ liệu trong Python

    - str: chuỗi kí tự ("hello dka")
    - int: số nguyên   (int(17))
    - float: số thực   (float(8.5))
    - list: danh sách  (list[1,2,3])
    - tuple: bộ giá trị cố định   (tuple(1,2,3))
    - dict: từ điển    (dict{name="Anh",age=19})
    - set: tập hợp     (set{1,2,3})
    - bool: kiểu đúng/sai    (true, false)

- Các toán tử trong Python

    - (**)	Toán tử mũ
    - (~ + -)	Phần bù; phép cộng và trừ một ngôi (với tên phương thức lần lượt là +@ và -@)
    - (* / % //)	Phép nhân, chia, lấy phần dư và phép chia //
    - (+ -)	Phép cộng và phép trừ
    - (>> <<)	Dịch bit phải và dịch bit trái
    -  (&)	Phép Và Bit	
    - (^ |)	Phép XOR và OR
    - (<= < > >=)	Các toán tử so sánh
    - (<> == !=)	Các toán tử so sánh bằng
    - (= %= /= //= -= += *= **=)	Các toán tử gán
    - (is is not)	Các toán tử Identity
    - (in not in)	Các toán tử Membership
    - (not or and)	Các toán tử logic

- Mệnh đề điều kiện và vòng lặp
    - Mệnh đề điều kiện(if,else if,else)
        time = 10
    if (time < 10):
        print ("Good morning")
    elif (time < 20):
        print ("Good day")
    else:
        print ("Good evening")
    - Vòng lặp while 
        x = 0
    while (x < 1000):
        x = x + 1
    print (x)  
    - Vòng lặp for
        numbers = [1, 2, 3, 4, 5]
    for number in numbers:
        print(number)
- Kiểu dữ liệu True, False
    - Chỉ có 2 giá trị: True và False.
    - Dùng để kiểm tra điều kiện trong if, while,..
