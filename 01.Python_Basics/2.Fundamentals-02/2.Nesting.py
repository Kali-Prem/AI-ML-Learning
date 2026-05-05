username = input("enter username: ")
password = input("enter password")

if(username == "admin" and password == "pass"):
    print("Success")
else:
    if(username != "admin"):
        print("enter valid username")
    else:
        print("enter valid password")
