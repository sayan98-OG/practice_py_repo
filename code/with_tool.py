
with open('file.txt') as f:
    print(f.read())

print('closed the file')    
 # when you are using with we dont need to close the file. exiting the indentation automatically closes the file.