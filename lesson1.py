age = int(input("enter your age: "))
if age > 18:
    print("Adult!")
else:
    print("Young!")

password = 12345
user_pass=int(input("enter a password"))
if password == user_pass:
    print("Logged in")
else:
    print("Access denied")

height = int(input("enter your height: "))
if age > 12 and height > 160 :
    print("OK")
else:
    print("Forbidden")