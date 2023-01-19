def main():
    users = [{
        "username":"Jaime",
        "password":"kike",
        "cash": "10000"
    },{
        "username":"j",
        "password":"k",
        "cash":"10000"
    }]
    button_1 = True
    button_2 = True
    print("-"*100)
    print("Welcome!!!!")
    print("This programmer is for simulated a bank")

    while button_1:
        print("Main Menu")
        print("")
        print("What's your rool? ")
        print("1. User")
        print("2. Boss")
        print("3. Bye!")
        option = input("")
        print("-"*100)
        match option: 
            case "1":
                users = user(users)
        break

def user(users):
    print("Welcome User!")
    user = input("What's your user? ")
    password = input("what's your password? ")
    button = cheak(user,password,users)
    while button:
        print("Welcome ",user)
        print("What do you wants?")
        print("1. Pay your debts with your cash? ")
        print("2. To Give cash?")
        print("3. Lend cash?")
        print("4. close")
        option = input("")
    match option:
        case "1":
            print("")
            #Search cash and debts of user
        case "2":
            print("")
            #Search user cash 
        case "3":
            print("")
            #search debt and to show many money lend to user depend of cash    
        case "4":
            print("Bye!")
            button = False
        case _:
            print("Invalid option, repeat")
def cheak(user,password,users):
    for use in users:
        if use["username"] == user and use["password"] == password:
            return True
def search_user(user,username,password):
    for use in user:
        if use["username"] == username and use["password"] == password:
            return use
    print("Invalid username or password")
    return False        

main()