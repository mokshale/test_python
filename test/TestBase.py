
print("Hellow World !")


a = 5
b = 10
print(a + b)

# 列表
RUNOOB = [6, 0, 4, 1]
print('清空前:', RUNOOB)
RUNOOB.clear()
print('清空后:', RUNOOB)

#字符串
s1='hello'
s2="hello"
s3="""hello
world"""
s4='I\'m Tom'
s5='我是"河南"人'
print(s5[0]) # 字符串下标
print(s5[1])

# 切片：[起始位置:结束位置:步长]
s='0123456789'
print(s[2:5:1])
print(s[2:5])
print(s[-8:-5])
print(s[2:])
print(s[-8:])
print(s[:5])
print(s[::-1]) #反向输出
print(s[::-2])
print(s[::2]) # 跳着输出
print(s.find('23')) #输出下标
print(s.index('23')) #输出下标,找不到会报错






