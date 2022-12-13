class account:
    def __init__(self,title,balance):
        self.title = title
        self.balance = balance

class savings_acccount(account):
    def __init__(self,title,balance,interest_rate):
        super().__init__(title,balance)
        self.interest_rate = interest_rate

account_obj = account("Fahima",5000)
savings_acccount_obj = savings_acccount("shivani",5000,5)
print(savings_acccount_obj.title)
print(savings_acccount_obj.balance)
print(savings_acccount_obj.interest_rate)
