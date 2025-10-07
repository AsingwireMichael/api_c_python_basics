def getValues(num1, num2):
    """_summary_

    Args:
        num1 (_type_): _description_
        num2 (_type_): _description_    
    """
    if  num1 > num2:
        print(num1)
    else:
        print(num2)
    
    
    
    sum = num1 + num2
    
    return sum


input1 = int(input("Enter first value "))
input2 = int(input("Enter second value "))

result = getValues(input1, input2)
print(f"The sum is {result}")


