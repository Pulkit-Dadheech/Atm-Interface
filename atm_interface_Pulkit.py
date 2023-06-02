# Account information
accounts = {
    '1111': {'name': 'Pulkit', 'pin': '1111', 'balance': 50000},
    '2222': {'name': 'Gauresh', 'pin': '2222', 'balance': 55000},
    '3333': {'name': 'Vijay', 'pin': '3333', 'balance': 45000},
    '4444': {'name': 'Piyush', 'pin': '4444', 'balance': 60000},
}

# Welcome Window
print("--------------------------")
print("Welcome to Pulkit ATM")
print("--------------------------")

# Start Menu
while True:
    print("Please select an option:\n")
    print("1. Enter your PIN\t2. Exit\n")
   
    choice = input("Enter your choice (1 or 2): ")

    # Authentication (Pin)
    if choice == '1':
        account_num = input("Enter your Account Number: ")
        if account_num in accounts:
            pin = input("Enter your PIN: ")
            if pin == accounts[account_num]['pin']:
                print("Authentication successful.")
                # Account Info
                while True:
                    print("\nPlease select an option:\n")
                    print("1. Check balance")
                    print("2. Withdraw money")
                    print("3. Deposit money")
                    print("4. Change PIN")
                    print("5. Exit\n")
                    choice = input("Enter your choice (1-5): ")
                    if choice == '1':
                        print(f"Your current balance is: {accounts[account_num]['balance']}")
                    elif choice == '2':
                        amount = float(input("Enter amount to withdraw: "))
                        if amount > accounts[account_num]['balance']:
                            print("Insufficient balance.")
                        else:
                            accounts[account_num]['balance'] -= amount
                            print(f"Withdrawal successful. Your new balance is: {accounts[account_num]['balance']}")
                    elif choice == '3':
                        amount = float(input("Enter amount to deposit: "))
                        accounts[account_num]['balance'] += amount
                        print(f"Deposit successful. Your new balance is: {accounts[account_num]['balance']}")
                    elif choice == '4':
                        new_pin = input("Enter new PIN: ")
                        accounts[account_num]['pin'] = new_pin
                        print("PIN changed successfully.")
                    elif choice == '5':
                        break
                    else:
                        print("Invalid choice. Please try again.")
            else:
                print("Invalid PIN. Please try again.")
        else:
            print("Account not found. Please try again.")
    elif choice == '2':
        print("Thank you for using Pulkit's ATM. Goodbye!")
        break
    else:
        print("Invalid choice. Please try again.")
