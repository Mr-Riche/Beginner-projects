one = "1"
two = "2"
three = "3"
four = "4"
while True:
    balance = 1000
    print("==MENU==")
    print("1.Check Balance")
    print("2.Deposit money")
    print("3.withdraw money")
    print("4.exit")

    choice = input("choose an option 1-4 >>")
    if choice == one:
        print(f"you balance is {balance}")
    elif choice == two:
        deposit = int(input("deposit amount >>"))
        print(deposit + balance)
        print(f"new balance is {balance}")
    elif choice == three:
        withdraw = int(input("withdraw amount"))
        print(balance-withdraw)
    elif choice == four:
        break
