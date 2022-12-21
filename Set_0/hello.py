name = input("What's your name? ")
#the function  strip() remove whitespace from str(string)
#the function capitalize() capitalize first letter from string 
#name = name.capitalize()

#the function title() capitalize every word in the string
name = name.strip().title()
#Split user's name into first name and last name
full_name = name.split()
print(f"Hello, my name is {full_name}")
