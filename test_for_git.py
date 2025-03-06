""""數字加總"""

total = 0

while True:
    num = input("請輸入數字 (輸入0結束):")
    try:
        num = float(num)
        if num == 0:
            break
        total += num
    except ValueError:
        print("請輸入有效的數字！")

print(f"總和是：{total}")
