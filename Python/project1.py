# 🏧 ATM Project

Atm_pin = 7884
Balance = 76000
attempts = 3

while attempts > 0:
    try :

        pin = int(input("Enter 4 Digit PIN : "))

        if pin == Atm_pin:
            print("Pin Is Correct")
            break

        else:
            attempts -= 1
            print("You Entered The Incorrect Pin")

            if attempts > 0:
                print("Remaining Attempts : ", attempts)
            else:
                print("Account Blocked")

    except ValueError:

        print("PIN enterd Must Be Number")

if attempts > 0:

    while True :
        try:

            print("\n=============ATM MENU============")
            print("\n1. Balance")
            print("2. Withdraw")
            print("3. Deposit")
            print("4. Exit")

            choice = int(input("Enter The Choice : "))

            if choice == 1:
                print("Balance : ", Balance)

            elif choice == 2:
                withdraw = int(input("Enter withdrawal Amount : "))

                if withdraw <= 0 :
                    print("The Withdrawal Amount Must be More Than 0")

                elif withdraw > Balance :
                    print("INSUFFICIENT BALANCE")

                else:
                    Balance -= withdraw
                    print("Withdrawal Of : ", withdraw)
                    print("Remaining Balance : ", Balance)

            elif choice == 3:
                deposit = int(input("Enter Deposit Amount : "))

                if deposit <= 0:
                    print("Deposit Amount Must Be Greater Than 0")

                else:
                    Balance += deposit
                    print("Deposited of : ", deposit)
                    print("Remaining Balance : ", Balance)

            elif choice == 4:
                print("Thankyou For Using Our Atm")
                break

            else:
                print("Invalid Choice")

        except ValueError : 
            print("Enter Valid Number")

                
                