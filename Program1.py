class Calculator:
    def addition(self,a,b):
        print(a+b)
    def subtraction(self,a,b):
        print(a-b)
    def multiplication(self,a,b):
        print(a*b)
    def division(self,a,b):
        if b==0:
            print("Division operation cannot perform enter value greater than zero")
        else:
            print(a/b)

a=float(input("Enter the number:"))
b=float(input("Enter the number:"))
type_of_operation=input("Enter type of operation to perform:")

calci=Calculator()
if type_of_operation=='+':
    calci.addition(a,b)
elif type_of_operation=='-':
    calci.subtraction(a,b)
elif type_of_operation=='*':
    calci.multiplication(a,b)
elif type_of_operation=='/':
    calci.division(a,b)
