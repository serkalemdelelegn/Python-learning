#logical oerator 
#or - at least one condition must be true 

temp= float(input("what is the wether temprature"))
raining=True

if temp>35 or temp<0 or raining:
 print("the meeting is canclled ")
else:
 print("the meeting is still scheduled")
 
#and - both condition must be true 

temp= float(input("enter the temrprature"))
sunny=False

if temp>=30 and sunny:
 print("it5 is hot outside")
 #not - invert the condition 
elif temp <=0 and not sunny:
 print("out side is cold ")
elif temp < 30 > 5 and sunny:
 print("the temprature is worm")
else:
 print("error")

