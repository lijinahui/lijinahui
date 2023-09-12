import 第一阶段.my_package.my_module1
from 第一阶段.my_package import my_module2

print(第一阶段.my_package.my_module1.str_reverse("黑马程序员"))
print(第一阶段.my_package.my_module1.substr("itheima", 0, 4))

#my_module2.print_file_info("D:/test_append.txt")
my_module2.append_to_file("D:/test_append.txt", "itheima")
my_module2.print_file_info("D:/test_append.txt")


