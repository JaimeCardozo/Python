operation = imput("Operation: ")
operation = operation.strip()
operator = operation.strip("1234567890")
number1 = operation.rfind(operator)
number1 = operation[0:number1 - 1]