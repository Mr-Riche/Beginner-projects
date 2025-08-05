attempts = 0
user_name_reg = "richard"
password_reg = "12345"
while attempts < 3:
    user_name = input("username").lower()
    password = input("password")
    if user_name == user_name_reg and password == password_reg:
        print("login successful")
        break
    else:
        attempts += 1
        print("attempt failed try again")
        print(f"you only have 3 and you have used {attempts}")
if attempts == 3:
    print("you can no longer login for today")
