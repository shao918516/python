"""
第二章 数据类型--数值类型、布尔类型
python 的基础数据类型
数值类型：整数类型、浮点类型、复数类型
布尔类型：是数值类型的子类型
序列类型：字符串、字节、列表、元组
映射类型：字典
集合类型：集合
自定义类创建对象
"""

# 一、数值类型
# 1.整数类型(int)  3  -5  0
# (1)定义：变量名=变量值（整数）
#type(object):能够返回object对象所属的类
a=2
print(type(a))
# (2)取值范围（整数的取值范围可以看成是无限）
i=10**100
print(i)
# python3，可以支持所有的整数，当数字的范围超过32位的时候，自动升级
# python2，分为两种整数类型，int（32位）  long（64）

# （3）四种进制
# N进制，逢N 进位
"""
二进制
八进制
十进制
十六进制
"""
"""
十进制  二进制  八进制
0        0      0
1        1      1
2       10
3       11
4      100
5      101
6      110
7      111      7
8     1000     10
9     1001
10    1010
"""
# 二进制 定义需要使用0b或者0B作为前缀
x=0b1010110
# 八进制，0o或者0O作为前缀
y=0o1234567
# print方法没有指定进制，默认打印的是十进制
print(x)
print(y)
# 十六进制，0x或者0X作为前缀  10-15 a/A-f/F
z=0x123456789abcdef
print(z)

# 进制之间的转换
# 不使用函数（手工）
# 其他进制转成十进制（乘幂法）
# 1234=1*1000+2*100+3*10+4*1
# 1234=1*10**3+2*10**2+3*10**1+4*10**0
# 1010=1*2**3+0*2**2+1*2**1+0*2**0=10
# 底数：原来的进制
# 指数：从右向左，当前的位数（右侧第一位是从0开始）
#
# 十进制转换成其他进制（下除取余）
# 除数：要转换成进制
# 取得结果：从下往上

# 二进制和八进制之间：每一位8进制，都使用3位的二进制表示即可。
# a=0o12   1*8**1+2=10
# b=0b001010 1*2**3+0*2**2+1*2**1+0*2**0=10

# 二进制和十六进制之间：每一位十六进制，都使用4位的二进制表示即可
# a=0x12          1*16**1+2=18
# b=0b00010010    1*2**4+0*2**3+0*2**2+1*2**1+0*2**0=18


# -------------
# 进制之间的转换
# 使用函数
# bin(x):将x转换成二进制，返回值是str
# oct(x):将x转换成八进制，返回值是str
# int(x):将x转换成十进制，返回值是int
# hex(x):将x转换成十六进制,返回值是str

print(bin(10))
# print(bin(10)+1) 不可以，因为bin返回的是str
print(oct(10))
print(hex(10))
print(int(10))
# print(int(10)+1) 可以，因为int函数返回int

print(type(bin(10)))
print(type(oct(10)))
print(type(hex(10)))
print(type(int(10)))
print(bin(0x12))

# int()：将字符串转换成整数，将其他进制转换成十进制
print(int("10"))
# print(int("数字",进制)) 将数字按照进制来转换
print(int("10",2))
print(int("10",10))
print(int("10",8))
print(int("10",16))

# 2.布尔类型  bool
# 布尔类型只有两个值True  False（注意大小写）
# 布尔类型是整数类型的子类型
# True---1   False---0
# 定义：变量名=变量值
t=True
f=False
print(type(t),type(f))

# print("new"+1)
print(t+1)  # 实际开发中，不要将布尔类型进行加减乘除运算。

# 真正应用
a=3
print(a<5)

# 数值、字符串、字节、布尔类型，只在内存中存储一份数据。
# a=1
# b=1
# t=True
# b=a<5


# 3.浮点类型 float
# 数学中的小数0.1   0.2
# 在python中，浮点类型只支持十进制
# （1）定义
f=04.1  #浮点类型定义的时候，前面可以加0
print(type(f))

# i=01  #如果是整数类型，前面不能加0
# print(type(i))

#（2）科学计数
print(1.2e8)
print(1.2e-8)

# (3)取值范围
# 浮点类型是有界限
# sys模块中浮点数的最大值和最小值
f=1e1001
print(type(f),f)
import sys
print(sys.float_info.max)
print(sys.float_info.min)

#(4)特殊的浮点数
# nan: not a number 应用的是表示无效数字（当数学上表示没有意义的数字）
      #nan跟谁都不相等，跟自己也不相等

# inf: 无穷大和无穷小 （超过了浮点数的界限之后，只能使用inf来表示）
print(float("nan"))
a=float("inf")
b=float("nan")
print(a*0)
print(a+2)
print(a/a)
x=3
print(x==3)
print(b==b) # nan跟谁都不相等，跟自己也不相等
print(a/a==b)

# 判断一个数是不是nan，只能是math函数下的isnan方法
import math
print(math.isnan(a/a))


# （5）浮点的不精确性
# 浮点数在计算机中只能做到近似存储
print(10/3)
print(0.1+0.2==0.3)
# 为什么不精确(有一部分小数是精确)
# 小数转换成二进制：小数部分*进制  取整数
# 0.1----二进制码
"""
0.1*2=0.2   0
0.2*2=0.4   0
0.4*2=0.8   0
0.8*2=1.6   1
0.6*2=1.2   1
0.2*2=0.4   0
"""
"""
0.5*2=1.0   1
0.25
0.125
"""
"""
使用浮点数时要注意：
（1）尽量避免数量级相差很大的浮点值之间进行计算
"""
f1=5e20
f2=1
print(f1+f2)

# (2)尽量避免等值判断
# 因为浮点数本来就不精确
print(0.1+0.2==0.3)

# 解决浮点数的不精确性
import decimal
# decimal.Decimal 能够显示浮点数真正存储值
x=decimal.Decimal(0.1)
y=decimal.Decimal(0.2)
print(x)
print(y)
print(x+y==0.3)

x1=decimal.Decimal("0.1")
y1=decimal.Decimal("0.2")
z1=decimal.Decimal("0.3")
print(x1,y1)
print(x1+y1==0.3)  # False
print(x1+y1==z1)
print(z1)

# 改变浮点数的有效数字，默认的有效数字是28位
print(decimal.getcontext().prec)
decimal.getcontext().prec=5
x=decimal.Decimal(0.1)
y=decimal.Decimal(0.2)
print(x+y)
print(x,y)
# 注意，只有做运算之后，运算结果才对有效数字生效。x，y本身是不变


# 4.复数类型 complex
import cmath
print(cmath.sqrt(-1))
#虚部使用j表示
c=3-5j
print(type(c))
print(c.real)
print(c.imag)


# 5. 四种类型之间的转换
# 整数、浮点数、复数、布尔
# int(value): 可以将value转换成整数类型（直接去掉小数点，相当于向0取整）
            # 不写value，默认返回0
            # int函数不能将复数类型转换成整数类型
i=0
f=0.1
c=1+2j
b=False
print(int())
print(int(f))
# print(int(c))
print(int(b))


# float(value): 可以将value转换成浮点数
#                # 不写value，默认返回0.0
print(float())
print(float(i))
# print(float(c)) # float函数不能将复数类型转换成浮点数
print(float(b))

# complex(value)：可以将value转换成复数类型
                # 不写value，默认返回0j
print(complex())
print(complex(i))
print(complex(f))
print(complex(b))

# bool(value)：可以将value转换成布尔类型
#           不写value，默认返回False
#         当0  0.0   0j   转换成False，否则转换成True
print(bool())
print(bool(i))
print(bool(f))
print(bool(c))

# 布尔类型可以将所有的数据类型进行转换


#6.  各种数据类型进行运算
# 结果取高级别的类型
# 复数类型>浮点类型>整数类型
print(i+f)
print(i+c)
print(f+c)
print(10/2)