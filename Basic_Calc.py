def function():
    a=int(input("Enter 1st Number:"))
    x=input("Operations:---\nAddition: +\nSubtract: -\nMultiply: *\nDivision: /\nEnter Operation:")
    b=int(input("\nEnter 2nd Number:"))
    d={"+":(a+b),"-":(a-b),"*":(a*b),"/":(a/b)}
    print("Result:",a,x,b,"=",d[x])
try:
    function()
except:
    print("\nEnter Right Operators!!")
    function()
finally:
    print("Task Completed\n")
    print("Next Operation:--")
    function()