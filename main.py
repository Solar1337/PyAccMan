import hashlib, os

def start():
    start = input("1. Delete account")
    if start == "1":
        delete()
    else:
        pass

def delete():
    delete = input("Are you sure you want to delete your account. This action cannot be undone. [Y]es, [N]o")
    if delete == "Y":
        os.remove(user + ".json")
        print("Operation completed successfully.")
    elif delete == "N":
        print("Your account has not been deleted")
        start()
    else:
        print("Response not valid.")

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
    global user
    user = input("Username: ")
    if os.path.isfile(user + ".json") == True:
        f = open(user + ".json", "r+")
        pw = input("Password: ")
        hash = hashlib.md5(pw.encode())
        if '"hash": ' + '"' +  hash.hexdigest() + '"' in f.read():
            f.close()
            print("ACCESS GRANTED")
            start()
        else:
            print("ACCESS DENIED")
    else:
        print("USER DOES NOT EXIST")

pre_start = input("1. Sign In\n2. Sign Up\n")
if pre_start == "1":
    sign_in()
elif pre_start == "2":
    sign_up()

