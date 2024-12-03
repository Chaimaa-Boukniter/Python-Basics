def calculator():
    a = float(input("Enter the first number : "))
    b = float(input("Enter the second number : "))
    op = input ("choose the operation (+ , - , / , ** , *) : ")
    while op not in ['+', '-', '*', '**', '/'] :
        print ("Invalid operation! ")
        op = input ("choose the operation (+ , - , / , ** , *) : ")
    if op == '+' :
        result = a + b 
        print (f"{a} + {b} = {result}")
    elif op == '-' :
        result = a - b 
        print (f"{a} - {b} = {result}")
    elif op == '*' :
        result = a * b 
        print (f"{a} * {b} = {result}")
    elif op == '**' :
        result = a ** b 
        print (f"{a} ** {b} = {result}")
    else:
        if b == 0 :
            print ("Erreur , deviding by 0 is not possible")
            while b == 0 :
                b = float(input("Enter the second number different from 0 : "))
        result = a / b 
        print (f"{a} / {b} = {result}")
        

calculator()