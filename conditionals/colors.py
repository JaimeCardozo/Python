#in this code you will know your color
age = int(input("What's your age "))
if   age >=0 and age < 10:
    color =  "Black"
elif age>10 and age<18:
    color = "Bronce"
elif age>18 and age<50:
    color = "Silver"
else:
    color = "Gold"
print(f"your color is {color}")    
            
        