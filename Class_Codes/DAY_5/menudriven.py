input_code=''
while(input_code != '5'):
    print("1. Add 2 numbers\n2. Subtract 2 numbers\n3. Multiply 2 numbers\n4. Divide 2 numbers\n5. EXIT\n ")
    input_code=input("Enter your choice\n")
    if(input_code=='1'):
        a=int(input("Enter value for a: "))
        b=int(input("Enter value for b: "))
        print("a+b= ",a+b)
    if(input_code=='2'):
        a=int(input("Enter value for a: "))
        b=int(input("Enter value for b: "))
        print("a-b= ",a-b)
    if(input_code=='3'):
        a=int(input("Enter value for a: "))
        b=int(input("Enter value for b: "))
        print("a*b= ",a*b)
    if(input_code=='4'):
        a=int(input("Enter value for a: "))
        b=int(input("Enter value for b: "))
        print("a/b= ",a/b)