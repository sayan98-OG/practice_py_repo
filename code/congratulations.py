#add date and name to a email
from datetime import date
letter = '''
         Dear <|Name|>,
         You are selected!
         <|Date|>'''

name = input("Provide the name - ")
today = str(date.today())

print(letter.replace("<|Name|>", name).replace("<|Date|>", today))


