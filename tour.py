from money import *
from datetime import *
from tourist import *

_destinations = ({"name": "Greece", "price": Money(100, "EUR")}, {"name": "France", "price": Money(120, "EUR")},
                 {"name": "Italy", "price": Money(200, "EUR")}, {"name": "USA", "price": Money(300, "USD")})


class _Tour:
    def __init__(self, destination, name, tourists, period):
        self.destination = destination
        self.name = name
        self.tourists = tourists
        self.period = period
        self.cost = self.calculateCost()

    def calculateCost(self):
        for i in _destinations:
            if i["name"] == Italy:
                self.cost = Money(200, EUR)

        return self

class TourBuilder:
  ensurance = True
  guided= True
  def __init__(self,destination,name,tourists,period):
    self._tour = _Tour(destination,name,tourists,period)
  def withEnsurance(self):
    if ensurance == True:
        self.cost = self.cost + (self.cost / 100 * 5)
    return self


  def withGuide(self):
      if guided == True:
          self.cost= self.cost + Money(100)
      return self
  def build(self):
    return self._tour

# tour = TourBuilder("Italy","The best parst of Italy",[Tourist("John Doe", 21), Tourist("Jane Doe", 30), Tourist("Jenny", 6)],Period("01.01.2021","02.02.2021")).withEnsurance().withGuide().build()
