#有时候我们需要将字符串与数值进行拼接，而Python不允许直接拼接数值和字符串，程序必须将数值转换成字符串
#将数值转换成字符串，可以使用str()或repr()函数
s1='这本书的价格是:'
p=99.8
#字符串直接拼接数值程序报错
print("使用str()函数拼接数值:",s1+str(p))
print("使用repr()函数拼接数值",s1+repr(p))