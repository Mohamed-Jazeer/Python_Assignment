import re
def registration():
    db = open("C:/Python/database.txt", "r")
    email = input("Create email ID: ")
    password = input("Create Password: ")
    data = { }
    for line in db:
        line = line.split(",")
        data.update({line[0]:line[1]})

    if re.match("[a-zA-z][a-zA-Z0-9._]*@[a-z]*.[a-z]", email):
        pass
        if email in data:
            print("email already exits. Please Login"), login()
        else:
            if len(password)<6 or len(password)>16:
                print("password must have atleast 6 to 16 characters")

            elif not re.search("[a-z]", password):
                print("password must contain 1 lowercase letter")

            elif not re.search("[A-Z]", password):
                print("password must contain 1 uppercase letter")

            elif not re.search("[0-9]", password):
                print("password must contain 1 digit")

            else:
                db = open("C:/Python/database.txt", "a")
                db.write(email + "," + password+"\n")
                print("Register successfully. Please Login")
                db.close()

    else:
        print("email not valid")

def login():
    db = open("C:/Python/database.txt", "r")
    email = input("Enter email ID: ")
    password = input("Enter Password: ")

    data = {}
    for line in db:
        line = line.split(",")
        data.update({line[0]: line[1]})

    if email in data:
        if password in data[email]:
            print("Login success")
        else:
            print("Incorrect password."+"\n"+"To Retrieve password" ), forgotpassword()
    else:
        print("Email doesn't exit. Please Register to Login"), registration()

def forgotpassword():
    db = open("C:/Python/database.txt", "r")
    email = input("Enter email ID: ")
    data = {}

    for line in db:
        line = line.split(",")
        data.update({line[0]: line[1]})
    if email in data:
        print(data.get(email))
    else:
        print("Check email ID")

def home(option=None):
    option = input( "Login | Register:")
    if option == "Login":
        login()
    elif option == "signup":
        registration()
    else:
        print("please enter a option")

        
home()


