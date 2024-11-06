b=10; """a and b are global variables"""
a=20;
def sum(x,y):
    sum=x+y;  """sum is local variable"""
    return sum
print("Sum is  : ",sum(a,b))
