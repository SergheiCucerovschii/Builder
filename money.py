class Money:
    _currencies = ("MDL", "USD", "EUR", "RUB", "RON")

    def __init__(self, amount, currency):
        global _currencies
        self.amount = amount
        self.currency = currency
        if self.amount < 0:
            raise ValueError(f"Enter a valid amount")
        else:
            if self.currency not in self._currencies:
                raise ValueError(f"You can pay only in {self._currencies}")


    def __str__(self):
        return f"The selected tour costs {self.amount} {self.currency}"

#m = Money(50,"USD")
#print(m)