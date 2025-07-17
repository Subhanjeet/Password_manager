MasterPassword = "subhanjeet"

def view():
    with open("password.txt","r") as f:
        for line in f.readlines():
            data = line.rstrip()
            user, passw = data.split("|")
            print("username:",user,", password:",passw)
def add():
    name = input("Acount Name: ")
    password = input("password: ")
    with open("password.txt","a") as f:
        f.write(name + "|" + password + "\n")
while True:
    password_manager = input("What is your Master Password: ").lower()
    if password_manager != MasterPassword:
        print("Incorrect password")
        break
    elif password_manager == MasterPassword:
            mode = input("would you like to add a new password or view existing once (add/view) or press q for quit: ").lower()
            if mode == "q":
                    print("Thanks for using")
                    break
            if mode == "add":
                add()
                print("The password is sucessfuly added!!")
                break
            elif mode == "view":
                view()
                break