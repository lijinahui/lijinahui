from typing import Union

# 使用Union类型，必须先导包
my_list: list[Union[int, str]] = [1, 2, "itheima", "itcast"]

def func(data: Union[int, str]) -> Union[int, str]:
    pass
func()

