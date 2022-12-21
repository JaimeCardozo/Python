#Version 1 with interger, this calculator is used for calculator the sum from two numbers
"""number1 = int(input("enter firts number "))
number2 = int(input("enter second  number ")) 
print("the sum is", number1 + number2) """
#Version 2 with float
number1 = float(input("enter firts number "))
number2 = float(input("enter second  number ")) 
sum = number1 + number2
#the round(number[,ndigits]) is used for nearling one number to decimal most near, depend from ndigits 
sum = round(sum,2)
print("the sum is", sum) 
#write the number separated with "," to used z:,
print(f"the sum is {sum:,}")