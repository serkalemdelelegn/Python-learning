# weight = float(input("enter ur weight: "))
# unit = input ("Killogram or Pound (K or P)")

# if unit == "K":
#  weight = weight*2.205
# elif unit == "P":
#  weight = weight/2.205
# else:
#  print ("yout weight is nither K nor P")
 
# print (weight)

unit = input("is the unit is f or c: ")
degree = float(input("enter your degree: ")) 

if unit == "f":
 degree = (degree -32) *5/9
elif unit == "c":
 degree = (degree +32) *9/5
else:
 print("u entered wrong out of the system ")
 
print(f"the converted unit is {degree}")
