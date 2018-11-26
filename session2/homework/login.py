print("Hi there, welcome to the superuser gateway")

user = input("Username: ")
if user != "c4e":
    print("You are not superuser")
    exit()

pas = input("Password: ")
if pas != "codeofchange":
    print("Password is incorrect")
else:
    print("Welcome") 
