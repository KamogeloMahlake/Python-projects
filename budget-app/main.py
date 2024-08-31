class Category:
    def __init__(self, item):
        self.item = item
        self.ledger = []
        self.balance = 0

    def __str__(self) -> str:
        topline = self.item.center(30, "*")
        items = []
        for i in self.ledger:
            if len(i["description"]) > 23:
                description = f"{i['description'].replace(i['description'][23-len(i['description']):], '')}{i['amount']:7.2f}"
                items.append(description)
            else:
                spaces = (23 - len(i['description'])) * " "
                description = f"{i['description']}{spaces}{i['amount']:7.2f}"
                items.append(description)
        if "deposit" in items[0]:
            items[0] = (f"initial deposit        {self.ledger[0]['amount']:7.2f}")
        final_output = "\n".join(items)
        total = f"Total: {self.balance:.2f}"
        return f"{topline}\n{final_output}\n{total}"

    def deposit(self, amount, description=''):
        self.ledger.append({'amount': amount, "description": description})
        self.balance += amount

    def withdraw(self, amount, description=''):
        if self.check_funds(amount):
            self.ledger.append({"amount": -amount, "description": description})
            self.balance -= amount
            return True
        
        return False
    
    def get_balance(self):
        return self.balance
    
    def transfer(self, amount, Category):
        if self.check_funds(amount):
            self.balance -= amount
            Category.deposit(amount, f"Transfer from {self.item}")
            self.ledger.append({"amount": -amount, "description": f"Transfer to {Category.item}"})
            return True
        return False

    def check_funds(self, amount):
        if amount > self.balance:
            return False
        return True 


def create_spend_chart(categories):
    for c in categories:
        pass

food = Category("Food")
food.deposit(1000, 'deposit')
food.withdraw(10.15, "groceries")
food.withdraw(15.89, "restuarant and more food for dessert")
clothing = Category("Clothing")
food.transfer(50, clothing)
print(food)
print(clothing.ledger)