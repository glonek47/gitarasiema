logowanko = {
    "marcin": "123123",
    "mariusz": "admin",
    "marcinek": "marcin2115",
    "admin": "admin",
    "ada": "123456",
    "adam": "afsdfasd"
}
while True:
    login = input("podaj login ")
    if logowanko.get(login) is not None:
        password = input("podaj hasło ")
        if password == logowanko.get(login):
            if 'admin' == login and  password == 'admin':
                print("Logged in as an admin ")
                break;
            else:
                print("Logged in as a user ")
                break;

        else:
            print("Wrong password try again")
    else:
        print("No such person in the system")
