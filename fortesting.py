f = open('left.txt','r')
g = open('dead.txt','r+')
n = '9'
#print(f.read())
#print(f.readline(4))
print(f.read().split('\n'))
g.write(n)
g.close()
f.close()