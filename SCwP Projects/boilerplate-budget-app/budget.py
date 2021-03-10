class Category:
    category = None
    ledger = []

    def __init__(self, category):
        self.category = category
        self.ledger = []

    def deposit(self, amount, description=""):
        self.ledger.append({"amount": amount,
                            "description": description})

    def withdraw(self, amount, description=""):
        if self.check_funds(amount):
            self.ledger.append({"amount": -(amount),
                                "description": description})
            return True
        else:
            return False

    def get_balance(self):
        balance = 0
        for transaction in self.ledger:
            balance += transaction["amount"]
        return balance

    def transfer(self, amount, category):
        if self.check_funds(amount):
            description = f"Transfer to {category.category}"
            self.ledger.append({"amount": -(amount),
                                "description": description})
            category.deposit(amount, f"Transfer from {self.category}")
            return True
        else:
            return False

    def check_funds(self, amount):
        if self.get_balance() < amount:
            return False
        else:
            return True

    def __str__(self):
        result = f"{self.category.center(30, '*')}\n"
        total = 0
        for transaction in self.ledger:
            try:
                description = transaction["description"][:23].ljust(23)
            except Exception:
                description = "".ljust(23)
            amount = transaction["amount"]
            amount = round(amount, 2)
            total += amount
            result += f"{description}"
            result += str("{:.2f}".format(amount)).rjust(7) + "\n"
        result += f"Total: {round(total,2)}"
        return result


def create_spend_chart(categories):
    res = "Percentage spent by category\n"
    total_amt_spent = 0
    amts = {}

    for categ in categories:
        amt_spent = 0
        for transaction in categ.ledger:
            if transaction["amount"] < 0:
                amt_spent += -(transaction["amount"])
        amts[categ] = amt_spent
        total_amt_spent += amt_spent

    percent = {}
    for categ in categories:
        per = (amts[categ]/total_amt_spent)*100
        per = int(per)
        percent[categ] = per

    # starting at 100 and stopping at 0 by dec 10 each time
    for x in range(100, -10, -10):
        res += str(x).rjust(3) + "| "
        for categ in categories:
            if percent[categ] >= x:
                res += "o  "
            else:
                res += "   "
        res += "\n"

    dashes = len(categories)*3 + 1
    dash = "-"
    res += f"    {dash*dashes}\n"

    maxx = len(categories[0].category)
    for categ in categories:
        if len(categ.category) > maxx:
            maxx = len(categ.category)
    i = 0
    for x in range(maxx):
        res += "     "
        for categ in categories:
            try:
                if categ.category[i]:
                    res += categ.category[i] + "  "
                else:
                    res += " "
            except Exception:
                res += "   "
        if x != maxx-1:
            res += "\n"
        i += 1
    return res
