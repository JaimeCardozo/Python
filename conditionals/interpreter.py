operation = input("Operation: ")
operation = operation.replace(" ","")
operator = operation.strip("1234567890")
position_operator = operation.find(operator)
print(position_operator)
number1 = float(operation[0:position_operator])
number2 = float(operation[position_operator + 1:len(operation)])   
print(number1)
print(number2)
result = 0
match operator:
    case "+":
        result = number1 + number2
    case "-":
        result = number1 - number2
    case "*":
        result = number1 * number2
    case "/":
        result = number1/number2
    case _:
        print("Expresion not valid")    
print(result)
