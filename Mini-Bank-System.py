"""Mini Bank Account"""

while True:
    try:
        user_name = input("Please Enter your name :- ").strip().lower()
        if not user_name:
            print("Customer name cannot be empty.")
            continue

        balance = int(input("Enter starting balance :- "))
        if balance <= 0:
            print("Balance cannot be negative or zero.")
            continue

        break
    except ValueError:
        print("Invalid input! Please enter a valid number.")
        
menu = ["1. Check Balance", "2. Deposit Money", "3. Withdraw Money", "4. Transaction History", "5. Exit"]

li = []

while True:
    print("========= BANK MENU =========")
    for i in menu:
         print(i)

    user_input = None   
    try:
        user_input = int(input("\nSelect an option :- "))
    except ValueError:
        print("please enter a valid number: ")
        continue

    if user_input == 5:
        print("Thank you for using our bank system.")
        print(user_name)
        break

    elif user_input < 1 or user_input > 5:
        print("Invalid choice!")

    elif user_input == 1:
        print(f"Your Balance: {balance} TK")

    elif user_input == 2:

        try:
            dep = int(input("Enter deposit amount :- "))
            if dep < 0:
                print("Deposit amount cannot be negative!")
            else:
                balance += dep
                deposit = ({"Deposit": dep})
                li.append(deposit)
                print(f"Your balance: {balance} TK")

        except ValueError:
            print("Invalid input! Please enter a valid number.")
            
    elif user_input == 3:

        try:
            withd = int(input("Enter withdraw amount :- "))
            if withd < 0:
                print("Withdraw amount cannot be negative! ")
            elif withd > balance:
                print("Insufficient Balance! ")
            else:
                balance -= withd
                # balance = balance - withd
                withdraw = ({"Withdraw": withd})
                li.append(withdraw)
                print(f"Successfully withdraw! Now your balance is: {balance} TK ")

        except ValueError:
                    print("Invalid input! Please enter a valid number.")
        
    elif user_input == 4:
        print("======== TRANSACTION HISTORY ========")
        print(f"Customer Name: {user_name} ")
        print(f"Current Balance: {balance} TK")
        for item in li:
            for key, value in item.items():
                 print(f"{key} > {value} TK ")
        
lines = []
for customer in li:
    if customer.get('Deposit', 0) > 0:
        lines.append(f"{user_name} > Deposit: {customer['Deposit']}")
    if customer.get('Withdraw', 0) > 0:
        lines.append(f"{user_name} > Withdraw: {customer['Withdraw']}")

result = "\n". join(lines)
if result:
    with open("customers.txt", "a") as f:
        f.write(result + "\n")