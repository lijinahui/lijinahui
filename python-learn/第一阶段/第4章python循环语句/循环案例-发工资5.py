j = 5000
for i in range(1,21):
    import random
    num = random.randint(1, 10)
    if num < 5 :
        print(f"员工{i}，绩效分{num}，不发工资，下一位。")
        continue
    if j >= 1000:
        j -= 1000
        print(f"员工{i}发工资1000元，账户余额还剩余:{j}")
    else:
        print(f"余额不足，当前余额：{j}元，不足以发工资，不发了，下个月再来")
        break

