class Tax:
    def __init__(self, money, podatok):
        self.money = money
        self.podatok = podatok
        self.balance = -1

    def taxValue(self):
        return self.money * self.podatok

    def getBalance(self):
        self.balance = self.money - self.taxValue()
        return self.balance

    def rewind(self):
        return self.balance / (1 - self.podatok)

    def execute(self):
        print(
            f"Початкова сума: {self.money}\n"
            f"Відсоток: {self.podatok * 100}%\n"
            f"Податок: {self.taxValue()}\n"
            f"Залишок: {self.getBalance()}\n"
            f"Відновлена сума: {self.rewind()}"
        )

class Tax2:
    def __init__(self, money, tax_min, podatok):
        self.money = money
        self.tax_min = tax_min
        self.podatok = podatok
        self.balance = -1

    def taxValue(self):
        if self.money >= self.tax_min:
            return (self.money - self.tax_min) * self.podatok
        else:
            return 0

    def getBalance(self):
        self.balance = self.money - self.taxValue()
        return self.balance

    def rewind(self):
        if self.balance >= self.tax_min:
            res = self.balance / (1 - self.podatok)
            correction = self.balance - self.tax_min 
            return res 
        else: 
            return self.balance
        """
        restored = (self.balance + self.tax_min) / (1 - self.podatok)
        if restored >= self.tax_min:
            return restored 
        return self.balance
        """
    
    def execute(self):
        print(
            f"Початкова сума: {self.money}\n"
            f"Відсоток: {self.podatok * 100}%\n"
            f"Податок: {self.taxValue()}\n"
            f"Залишок: {self.getBalance()}\n"
            f"Відновлена сума: {self.rewind()}"
        )





money = 1200
percent = 0.1

level1 = Tax(money, percent)
level2 = Tax2(money, 1000, percent)
#level1.execute()

level2.execute()