oldpassword = input("voer je oude wachtwoord in: ")
newpassword = input("voer je nieuwe wachtwoord in, het moet minimaal 6 characters lang en verschillen van je oude: ")
def new_password():
    if oldpassword != newpassword and len(newpassword) >= 6:
        print("gelukt")
        return True
    else:
        print("je nieuwe wachtwoord voldoet niet aan de eisen")
        return False
print(new_password())
