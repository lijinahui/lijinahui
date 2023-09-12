# 演示第二种字符串格式化的方式：f"{占位}"
name = "传智播客"
set_up_year = 2006
stock_price = 19.99
# f：format
print(f"我是{name},我成立于：{set_up_year}年，我今天的股价是：{stock_price}")

# 演示表达式进行字符串格式化
print("1 * 1 的结果是：%d" %(1 * 1))
print(f"1 * 2的结果是：{1 * 2}")
print("字符串在python中的类型名是：%s" % type("字符串"))

# 练习
name = "传智播客"
stock_price=19.99
stock_code="003032"
stock_price_daily=1.2
growth_days=7

print(f"公司:{name},股票代码:{stock_code},当前股价:{stock_price}")
print("每日增加系数是：%.1f,经过%s天的增长后，股价达到了：%.2f"%(stock_price_daily,growth_days,stock_price * stock_price_daily ** growth_days))




