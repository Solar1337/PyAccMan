import hashlib, os

def sign_up():
    print("Sign Up")
    user = input("Username: ")
    if os.path.isfile(user + ".json") == True:
        print("USER ALREADY EXISTS")
    else:
        f = open(user + ".json", "w+")
        f.write('{\n    "user": ' + '"' + user +  '",\n')
        pw = input("Password: ")
        hash = hashlib.md5(pw.encode())
        f.write('    "hash": ' + '"' + hash.hexdigest() + '"\n}')
        f.close()
        print("USER CREATED")

def sign_in():
    print("Sign In")
    user = input("Username: ")
    if os.path.isfile(user + ".json") == True:
        f = open(user + ".json", "r+")
        pw = input("Password: ")
        hash = hashlib.md5(pw.encode())
        if '"hash": ' + hash.hexdigest() in f.read():
            f.close()
            print("ACCESS GRANTED")
        else:
            print("ACCESS DENIED")
    else:
        print("USER DOES NOT EXIST")

start = input("1. Sign In\n2. Sign Up\n")
if start == "1":
    sign_in()
elif start == "2":
    sign_up()
