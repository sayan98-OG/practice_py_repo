Number = []

f1 = input("enter the number - ", )
Number.append(f1)
f2 = input("enter the number - ", )
Number.append(f2)
f3 = input("enter the number - ", )
Number.append(f3)
f4 = input("enter the number - ", )
Number.append(f4)
f5 = input("enter the number - ", )
Number.append(f5)
f6 = input("enter the number - ", )
Number.append(f6)

number = list(map(int, Number)) #inputs are always taken as strings. They should be converted to integers to be sorted
print(Number)
number.sort()
print(number)
