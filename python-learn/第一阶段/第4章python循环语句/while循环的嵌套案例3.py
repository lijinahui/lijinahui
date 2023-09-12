#
i = 1
while i <=100:
    print(f"今天是第{i}天，准备向小宝表白了。。。")
    j = 1
    while j <= 10:
        print(f"今天送给小宝的第{j}只玫瑰")
        j += 1
    print("小宝，我喜欢你")
    i += 1
print(f"坚持到第{i - 1}天，表白成功")



i = 1
while i <=9:

    j = 1
    while j <= i:
        print(f"{j} * {i} = {j*i}\t",end='')
        j += 1
    i += 1
    print()