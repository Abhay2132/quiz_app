from random import choice

cc = list([str(i) for i in range(0,10)]) + ['a','b','c', 'd', 'e', 'f']
rc = lambda : ("#"+"".join([choice(cc) for i in range(0,6)]))
