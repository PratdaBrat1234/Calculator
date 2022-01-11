x = "1 is * = multipulcation, 2 is / = Division, 3 is + = Addition, 4 is - = Subtraction, 5 is ** = exponents"
print(x)
mode = input("What mode would you like to use decimal, regular, or both:")
mode=str(mode)
if mode == "regular":
    print("Disclaimer: Only put whole numbers")
    option=input("Enter your option:")
    option=int(option)
    if option == 1:
        factor = input("Enter your factor:")
        factor = int(factor)
        var1 = factor
        factor2 = input("Enter your factor2:")
        factor2 = int(factor2)
        var2 = factor2
        var3 = var1 * var2
        print(var3)
    elif option == 2:
        dividend = input("Enter your dividend:")
        dividend = int(dividend)
        var1 = dividend
        divisor = input("Enter your divisor:")
        divisor = int(divisor)
        var2 = divisor
        var3 = var1 / var2
        print(var3)
    elif option == 3:
        number = input("Enter your number:")
        number = int(number)
        var1 = number
        multiple = input("Enter your digits:")
        multiple = int(multiple)
        var2 = multiple
        var3 = var1 + var2
        print(var3)
    elif option == 4:
        number = input("Enter your number:")
        number = int(number)
        var1 = number
        multiple = input("Enter your digits:")
        multiple = int(multiple)
        var2 = multiple
        var3 = var1 - var2
        print(var3)
    elif option == 5:
        base = input("Enter your base:")
        base = int(base)
        var1 = base
        power = input("Enter your power:")
        power = int(power)
        var2 = power
        var3 = var1 ** var2
        print(var3)

if mode == "decimal":
    print("Disclaimer: Only put decimal numbers(except when it it asks for an option) ")
    option=input("Enter your option:")
    option=float(option)
    if option == 1:
        factor = input("Enter your factor:")
        factor = float(factor)
        var1 = factor
        factor2 = input("Enter your factor2:")
        factor2 = float(factor2)
        var2 = factor2
        var3 = var1 * var2
        print(var3)
    elif option == 2:
        dividend = input("Enter your dividend:")
        dividend = float(dividend)
        var1 = dividend
        divisor = input("Enter your divisor:")
        divisor = float(divisor)
        var2 = divisor
        var3 = var1 / var2
        print(var3)
    elif option == 3:
        number = input("Enter your number:")
        number = float(number)
        var1 = number
        multiple = input("Enter your digits:")
        multiple = float(multiple)
        var2 = multiple
        var3 = var1 + var2
        print(var3)
    elif option == 4:
        number = input("Enter your number:")
        number = float(number)
        var1 = number
        multiple = input("Enter your digits:")
        multiple = float(multiple)
        var2 = multiple
        var3 = var1 - var2
        print(var3)
    elif option == 5:
        base = input("Enter your base:")
        base = float(base)
        var1 = base
        power = input("Enter your power:")
        power = float(power)
        var2 = power
        var3 = var1 ** var2
        print(var3)
if mode == "both":
    print("Disclaimer: If it says Enter your [blank] without decimal before it, don't put a decimal for the code will glitch and there will be an error")
    option=input("Enter your option:")
    option=int(option)
    if option == 1:
        factor = input("Enter your decimal factor:")
        factor = float(factor)
        var1 = factor
        factor2 = input("Enter your factor:")
        factor2 = int(factor2)
        var2 = factor2
        var3 = var1 * var2
        print(var3)
    elif option == 2:
        dividend = input("Enter your decimal dividend:")
        dividend = float(dividend)
        var1 = dividend
        divisor = input("Enter your divisor:")
        divisor = int(divisor)
        var2 = divisor
        var3 = var1 / var2
        print(var3)
    elif option == 3:
        number = input("Enter your number:")
        number = int(number)
        var1 = number
        multiple = input("Enter your decimal:")
        multiple = float(multiple)
        var2 = multiple
        var3 = var1 + var2
        print(var3)
    elif option == 4:
        number = input("Enter your decimal:")
        number = float(number)
        var1 = number
        multiple = input("Enter your digits:")
        multiple = int(multiple)
        var2 = multiple
        var3 = var1 - var2
        print(var3)
    elif option == 5:
        base = input("Enter your decimal base:")
        base = float(base)
        var1 = base
        power = input("Enter your power:")
        power = int(power)
        var2 = power
        var3 = var1 ** var2
        print(var3)
