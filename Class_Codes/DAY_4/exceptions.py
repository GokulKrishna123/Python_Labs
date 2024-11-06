try: 
    num1,num2=eval(input("Enter 2 numbers seperated with a comma:"))
    result=num1/num2
    print("result: ",result)
except ZeroDivisionError:
    print("Error: Division by zero!!")
except SyntaxError:
    print("Comma is missing!!")
except:
    print("Wrong input!!")
else: 
    print("No Exceptions, result is : ",result)
finally: 
    print("This will execute as final line")