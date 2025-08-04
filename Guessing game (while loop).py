print("guess number between 1-10")
secret_number = 7
while True:
    guess = int(input(">>>"))
    if guess > secret_number:
        print("too high")
    if guess < secret_number:
        print("too low")
    if guess == secret_number:
        print("correct")
        break
