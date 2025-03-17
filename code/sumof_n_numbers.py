# solution 1
l = []
i=0
n = int(input("how many natural numers you want to add: "))
while (i<n+1):
    l.append(i)
    i += 1

print(sum(l))

# solution 2
total = 0
m = int(input("how many natural numers you want to add: "))
for i in range (m+1):
    total = total+i

print(total)