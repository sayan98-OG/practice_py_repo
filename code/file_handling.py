
f = open('file.txt')
data = f.read()

print(data)
f.close()

str = 'Hey Sayan, you are amazing'

g = open('write_file.txt','w')
g.write(str)

g.close()


