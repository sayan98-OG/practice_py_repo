
word = input('Enter the word you want to find: ')

with open('poem.txt') as f:
    content = f.read()
    if word in content:
        print('yes we have it')
    else :
        print('no we dont have it')
        
            
