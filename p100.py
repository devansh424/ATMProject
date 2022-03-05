class Atm(object):
    def __init__(self, card_number, pin_number, balance):
        self.card_number = card_number
        self.pin_number = pin_number
        self.balance = balance

    def cashWithdrawl(self, amount):
        print(amount, "Has Been Withdrawn From The", self.card_number)
        self.balance -= amount
    
    def deposit(self, amount):
        print(amount, "Has Been Depostited In The", self.card_number)
        self.balance += amount
    
    def balanceEnquiry(self):
        print("Your Account Balance Is", self.balance)

atm_1 = Atm("123245342","1222",20000)

atm_1.cashWithdrawl(5000)
atm_1.deposit(4000)
atm_1.balanceEnquiry()