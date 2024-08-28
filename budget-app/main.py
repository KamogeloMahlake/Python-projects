class Category:
    def __init__(self, item):
        self.item = item
        self.ledger = []
        self.balance = 0

    def __str__(self) -> str:
        topline = "*" * ((30 - len(self.item)) // 2) + self.item +  "*" * ((30 - len(self.item)) // 2)
        items = []
        for i in self.ledger:
            if len(i["description"]) > 23:
                description = f"{i['description'].replace(i['description'][23-len(i['description']):], '')}{i['amount']:7}"
                items.append(description)
            else:
                spaces = (23 - len(i['description'])) * " "
                description = f"{i['description']}{spaces}{i['amount']:7}"
                items.append(description)
        final_output = "\n".join(items)
        total = f"Total: {self.balance}"
        return f"{topline}\n{final_output}\n{total}"

    def deposit(self, amount, description=False):
        if description:
            self.ledger.append({'amount': amount, "description": description})
        else:
            self.ledger.append({'amount': amount})
        self.balance += amount

    def withdraw(self, amount, description=False):
        if amount <= self.balance :
            if description:
                self.ledger.append({"amount": -amount, "description": description})

            else:
                self.ledger.append({"amount": -amount})
            self.balance -= amount
            return True
        
        return False
    
    def get_balance(self):
        return self.balance
    
    def transfer(self, amount, Category):
        if amount <= self.balance:
            self.balance -= amount
            Category.balance += amount
            self.ledger.append({"amount": -amount, "description": f"Transfer to {Category.item}"})
            Category.ledger.append({"amount": amount, "description": f"Transfer from {self.item}"})
            return True
        return False

    def check_funds(self, amount):
        if amount > self.balance:
            return False
        return True 


def create_spend_chart(categories):
    pass

food = Category("Food")
food.deposit(1000, "deposit")
food.withdraw(10.15, "groceries")
food.withdraw(15.89, "restuarant and more food for dessert")
clothing = Category("Clothing")
food.transfer(50, clothing)
clothing.transfer(45, food)
print(food)
print(clothing)

