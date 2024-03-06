class Employee:
    def __init__(self):
        self.income = 0

    def earn_money(self, money):
        self.income += money

    @property  # 虛擬的屬性
    def tax_amount(self):
        return self.income*0.05

    @tax_amount.setter
    def tax_amount(self, tax_number):
        self.income = tax_number * 20


wilson = Employee()
wilson.earn_money(300)
print(wilson.tax_amount)  # 15.0 # tax_amount 是虛擬屬性，不是真正的屬性

wilson.tax_amount = 20
print(wilson.income)  # 400
