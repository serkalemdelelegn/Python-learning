#conditional expression = a one shortcut for the if-else statemernt (ternary operation)
#                       = print or assign one of two values based on a condition
#                       = x if condition else y
 
#num =int(input("enter any number "))

#print("posetive" if num > 0 else "negative")

#result="even" if num%2==0 else "odd")
a=int(input("enter a number: "))
b=int(input("enter the second number: "))

result= a if a>b else b
result2= a if a<b else b

print(result)
print(result2)
