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
                description = f"{i['description'][:23]}{i['amount']:7.2f}"
                items.append(description)
            else:
                spaces = (23 - len(i['description'])) * " "
                description = f"{i['description']}{spaces}{i['amount']:7.2f}"
                items.append(description)
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
    chart = 'Percentage spent by category\n'
    spending = {}
    percentage = {}
    total_spending = 0

    for category in categories:
        spent = abs(sum(i['amount'] for i in category.ledger if i['amount'] < 0))
        spending[category.item] = round(spent, 2)

    total_spending += sum(spending.values())
    for i in spending:
        percentage[i] = int(round(spending[i] / total_spending, 2) * 100)
    
    for i in range(100, -1, -10):
        chart += f"{i}".rjust(3) + "|"
        for percent in percentage.values():
            if percent >= i:
                chart += " o "
            else:
                chart += "   "
        chart += "\n"

    chart += ' ' * 4 + "-" * (len(percentage.values()) * 3 + 1)
    chart += "\n     "
    max_length = max([len(i) for i in list(percentage.keys())])

    for i in range(max_length):
        for name in list(percentage.keys()):
            if len(name) > i:
                chart += name[i] + "  "
            else:
                chart += "   "
        if i < max_length - 1:
            chart += "\n     "
    return chart

        




food = Category("Food")
food.deposit(1000, 'deposit')
food.withdraw(10.15, "groceries")
food.withdraw(15.89, "restuarant and more food for dessert")
clothing = Category("Clothing")
food.transfer(50, clothing)
clothing.withdraw(50)
print(create_spend_chart([food, clothing]))