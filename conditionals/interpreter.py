operation = input("Operation: ")
operation = operation.replace(" ","")
operator = operation.strip("1234567890")
position_operator = operation.find(operator)
if position_operator == 1:
    number1 = float(operation[position_operator - 1])
    number2 = float(operation[position_operator + 1])
else:
    number1 = float(operation[0:position_operator])
    number2 = float(operation[position_operator + 1: len(operation)])   
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


