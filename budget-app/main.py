class Category:
    def __init__(self, item):
        self.item = item
        self.ledger = []
        self.balance = 0

    def __str__(self) -> str:
        return f"{self.balance}\n{self.ledger}"

    def deposit(self, amount, description=False):
        if description:
            self.ledger.append({'amount': amount, "description": description})
        else:
            self.ledger.append({"amount": amount})
        self.balance += amount

    def withdraw(self, amount, description=False):
        if amount <= self.balance:
            self.balance -= amount
            amount -= (amount + amount)
            if description:
                self.ledger.append({"amount": amount, "description": description})

            else:
                self.ledger.append({"amount": amount})
            return True
        return False

            


def create_spend_chart(categories):
    pass

food = Category("Food")
food.deposit(1000, "deposit")
food.withdraw(15.89, "restuarant and more food for dessert")
print(food)