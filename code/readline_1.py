
f = open('file.txt')

l=f.readline()
while (l!=''):
    print(l)
    l=f.readline()
f.close()

g = open('file.txt')
text = g.read()

g.close()
print(text)