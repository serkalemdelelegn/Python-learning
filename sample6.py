# validate user input exercise
# username no more than 12 char
# username must not contain spaces
# username must not contain digits

username = input("Enter your username: ")

# username.find(" ")

# username.isalpha()

if len(username)>12:
 print("the username dont exceed 12 char ")
elif not username.find(" ")== -1:
 print ("the username cant contain space ")
elif not username.isalpha():
 print(" username ccan't be digits")
else:
 print(f"welcome {username}")
 