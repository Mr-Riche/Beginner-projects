print("guess number between 1-10")
secret_number = 7
while secret_number > 0:
    secret_number = int(input(">>>"))
    if secret_number > 7:
        print("too high")
    if secret_number < 7:
        print("too low")
    if secret_number == 7:
        print("correct")
        break
