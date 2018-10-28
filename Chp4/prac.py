#!/usr/bin/env python2

def addNumbers(x, y):
	return x + y

def name(first, last):
	return '{} {}'.format(first, last)

sq = lambda x:x**2

getFirst = lambda s:s[0]

add = lambda x,y:x+y

names = lambda x,y:'{}, {}'.format(y, x)

map(lambda x:x**2,[4,6,2,8,7,9])

map(lambda x,y:x+y, [1,2,3,4],[5,6,7,8])

map(lambda x,y:'{} {}'.format(x,y), ['Justin', 'Chad', 'Jerrin'], ['Minsk', 'Redmen', 'V.'])

filter(lambda x:len(x) <= 4, ['Justin', 'Chad', 'Jerrin'])

filter(lambda x:x%2==0, [1,2,3,4,5,6,7,8,9])

reduce(lambda x,y:x+y, [1,2,3,4,5,6,7,8,9])

reduce(lambda x,y: x if x >= y else y, [3,5,1,6,2])
a = ['1', '5', '3']
','.join(a)


def sqaure(line):
	return map(lambda x:str(int(x)**2), line)
	
print sqaure(['2', '4', '6'])
