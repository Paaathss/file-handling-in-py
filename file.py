

f = open('demo02.text','w+')
f.write('hello gys')
f.close()


f = open('demo02.text','w+')
for i in range(20):
       f.write('hello gys %d\n'%(i+1))
f.close()


f = open('demo02.text','a+')
for i in range(4):
       f.write('hello love you gys %d\n'%(i+1))
f.close()

f = open('demo02.text','r')
con = f.read()
print(con)
f.close()


f = open('demo02.text','r')
con = f.readline(4)
print(con)
f.close()





f = open('demo02.text','r')
con = f.read(6)
print(con)
f.close()



f = open('demo02.text','r')
con = f.read(6)
print(con)

print(f.tell())
print(f.seek(0))

con1 = f.read(12)
print(con1)

f.close()