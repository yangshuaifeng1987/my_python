'''
input()函数用于向用户生成一条提示，然后获取用户输入的内容。由于Input()函数总会将用户输入的内容放入字符串，因此用户
可以输入任何内容，input()函数总是返回一个字符串。
'''

msg=input("请输入你的值:")
print(type(msg))
print(msg)