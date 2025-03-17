
with open('check.txt') as f:
    c = f.read()
    count = c.count('monkey')
    print(count)
with open('check.txt','w') as w:
    if count>1:
        c=c.replace('monkey','sassy')
        w.write(c)
    else:
        w.write(c)


