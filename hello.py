# -*- coding: utf-8 -*-
def move(n,a,b,c):
	if n==1:
		print('move',a,'-->',c)
		return
	move(n-1,a,c,b)
	print('move',a,'-->',c)
	move(n-1,b,a,c)
move(2,'A','B','C')

L = ['MIC','SAR','JAC']
r = []
n = 3
for i in range(n):
	r.append(L[i])

print(r)

L = [x*x for x in range(10)]
print(L)


def f(x):
	return x*x
r = map(f,[1,2,3,4,5,6,7,8,9])
print(list(r))

from functools import reduce
def str2int(s):
	def fn(x,y):
		return x*10+y
	def char2num(s):
		return {'0':0,'1':1,'2': 2, '3': 3, '4': 4, '5': 5, '6': 6, '7': 7, '8': 8, '9': 9}[s]
	return reduce(fn,map(char2num,s))
print(str2int('13579'))

def prod(L):
	def mul(x,y):
		return x*y
	return reduce(mul,L)
print('3*5*7*9=',prod([3,5,7,9]))

def str2float(s):
	float = len(s)-s.index('.')-1
	s = s.replace('.','')
	def char2num(m):
		return {'0':0,'1':1,'2': 2, '3': 3, '4': 4, '5': 5, '6': 6, '7': 7, '8': 8, '9': 9}[m]
	def order(a,b):
		return a*10 + b
	return reduce(order,map(char2num,s))/10**float
print('str2float(\'123.456\')=',str2float('123.456'))

def _odd_iter():
	n = 1
	while True:
		n = n+2
		yield n
def _not_divisible(n):
	return lambda x : x % n > 0
def primes():
	yield 2
	it = _odd_iter()
	while True:
		n = next(it)
		yield n
		it = filter(_not_divisible(n),it)

for n in primes():
	if n < 1000:
		print(n)
	else:
		break

print(list(map(lambda x: x * x,[1,2,3,4,5,6])))

f = lambda x: x * x
print(f(6))

def int2(x,base=2):
	return int(x,base)
print(int2('1000000'))

'a test module'
__author__ = 'chenkp'

import sys
def test():
	args = sys.argv
	if len(args) == 1:
		print('hello,world!')
	elif len(args) == 2:
		print('Hello,%s!' % args[1])
	else:
		print('too many argu')
if __name__=='__main__':
	test()

print(sys.path)

class Student(object):
	"""docstring for Student"""
	def __init__(self, name,score):
		self.__name = name
		self.__score = score

	def print_score(self):
		print('%s: %s' % (self.__name,self.__score))

	def get_grade(self):
		if self.__score >= 90:
			return 'A'
		elif self.__score >= 60:
			return 'B'
		else:
			return 'C'
	def get_name(self):
		return self.__name

	def get_score(self):
		return self.__score

	def set_score(self,score):
		if 0 <= score <=100:
			self.__score = score
		else:
			raise ValueError('bad score')

	def set_name(self,name):
		if (len(name) > 5):
			raise ValueError('bad name')
		else:
			self.__name = name
bart = Student('Bart Simp',59)
bart.set_score(80)
bart.set_name('chen')
print(bart.get_score())
print(bart.get_name())
class Stu(object):
	pass

s = Stu()
s.name = 'Michael'
print(s.name)


def set_age(self,age):
	self.age = age
from types import MethodType
s.set_age = MethodType(set_age,s)
s.set_age(25)
print(s.age)

class new(object):
	"""docstring for new"""
	def get_score(self):
		return self.__score

	def set_score(self,value):
		if not isinstance(value,int):
			raise ValueError('score must be an integer')
		if value < 0 or value > 100:
			raise ValueError('score must between 0~100')
		self.__score = value

t = new()
t.set_score(60)

print(t.get_score())

t.set_score(90)


with open('D:\\work\\test.txt','w') as f:
	f.write('Hello , chenkp')
