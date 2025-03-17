#detect double space in a string

string = input("Enter the string - ")

index = string.find("  ")
if index ==-1:
    print("No double spaces detected")
else:
    print(f"Double space on index number - {index}")



