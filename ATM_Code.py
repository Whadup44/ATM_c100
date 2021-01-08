class ATM(object):
    def __init__(self, balance):
        self.balance = balance
    
    def displayBalance(self):
        print(self.balance)
    
    def withdrawMoney(self):
        withdrawnAmount = input("Please input how much money you would like to be withdrawn from your account here: ")
        self.balance = self.balance - int(withdrawnAmount)
        print("Successfully withdrawn 100 from your account, now you have " + str(self.balance) + " money left in your account.")
    
    def depositMoney(self):
        depositedAmount = input("Please input how much money you would like to be deposited into your account here: ")
        self.balance = self.balance + int(depositedAmount)
        print("Successfully deposited 100 into your account, now you have " + str(self.balance) + " money in your account.")

bankOBJ = ATM(20000)

balance = 20000
cardNumber = "8605603279976693"
cardNumberPassword = "725"
isCardCorrect = False
isPasswordCorrect = False
while not(isCardCorrect):
    cardNumberInput = input("Please input your 16-digit card number here: ")
    if cardNumberInput == "8605603279976693":
        isCardCorrect =True
        while not(isPasswordCorrect):
            cardNumberPasswordInput = input("Please input your 3-digit password here: ")
            if cardNumberPasswordInput == "725":
                inputVal = input("To display balance in your account press 1, to withdraw money press 2, to depoit money press 3: ")
                isPasswordCorrect = True
            else:
                print("Sorry, the password inputed is incorrect, please try again")
    else:
        print("Sorry, this car number does not exist in our database. Please try again.")

if  inputVal == "1":
    bankOBJ.displayBalance()
elif inputVal == "2":
    bankOBJ.withdrawMoney()
elif inputVal == "3":
    bankOBJ.depositMoney()