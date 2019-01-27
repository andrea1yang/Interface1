#!/usr/bin/env python
# coding:utf-8

# author:Andrea


def Typeusername():
	username = input(u'请输入注册账号：')
	return username

def Typepassword():
	password = input(u'请输入密码：')
	return password


def register(username,password):
	'''
	:parameter:username是注册账号
	:parameter:password是注册密码  =
	:return:
	'''

	'''
	将注册账号和密码写入文件registerfile中
	'''
	register_file = open('registerfile','w')
	register_file.write(username + '|' +password)
	'''
	一个文件的打开都要有一个关闭  
	'''
	register_file.close()


def login(username,password):
	'''
	:parameter:username是登录账号
	:parameter:password是登录密码
	:return:
	'''
	'''
	1.读取registerfile中的注册账号和密码
	2.判断登录的账号密码和注册的是否一致，如果一致判断成功
	'''
	duqu = open('registerfile','r')
	for line in duqu:
		'''
		可以看到文档读取出来的数据是字符串型，需要转成列表的模式
		print(line)
		print(type(line))
		'''
		Loginlist = line.split('|')
		if username == Loginlist[0] and password == Loginlist[1]:
			#print(u'登录成功了')
			return True
		else:
			#print(u'登录失败')
			return False


def info(username,password):
	'''
	先从注册写入的文件中，读取出注册时的账号，
	如果登录函数返回的是成功的True，则验证登录输出登录成功提示
	'''
	duqu = open('registerfile', 'r')
	for line in duqu:
		Loginlist = line.split('|')
		x=login(username,password)
		if x:
			print(u'{0}已成功登录'.format(Loginlist[0]))
		else:
			print(u'登录失败')


def exit():
	import  sys
	sys.exit()


def main():
	'''
	这是主函数，可以调用上面的登录注册，
	当输入1调用注册
	当输入2调用登录
	当输入3调用验证登录
	'''
	while True:
		r = int(input(u'调用函数1.注册，2.登录，3.验证登录:\n'))
		if r == 1:
			username = Typeusername()
			password = password()
			register(username,password)

		elif r == 2:
			username = Typeusername()
			password = input(u'请输入密码：')
			login(username,password)
			info(username,password)

		elif r == 3:
			exit()
		else:
			print(u'请输入正确数字')



main()

