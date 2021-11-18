class AbstractCook(object):
    def __init__(self):
        self.for_food = 0
        self.for_drink = 0
        self.food_str = 'Food'
        self.drink_str = 'Drink'

    def add_food(self, amount, price):
        self.for_food += amount * price

    def add_drink(self, amount, price):
        self.for_drink +=  amount * price


    def total(self):
        return "%s: %d, %s: %d, Total: %d" % (self.food_str, self.for_food,self.drink_str, self.for_drink, self.for_food + self.for_drink)

class JapaneseCook(AbstractCook):

    def __init__(self):
        AbstractCook.__init__(self)
        self.food_str = 'Sushi'
        self.drink_str = 'Tea'

class RussianCook(AbstractCook):
    def __init__(self):
        AbstractCook.__init__(self)
        self.food_str = 'Dumplings'
        self.drink_str = 'Compote'

class ItalianCook(AbstractCook):
    def __init__(self):
        AbstractCook.__init__(self)
        self.food_str = 'Pizza'
        self.drink_str = 'Juice'


if __name__ == '__main__':

    #These "asserts" using only for self-checking and not necessary for auto-testing

    client_1 = JapaneseCook()
    client_1.add_food(2, 30)
    client_1.add_food(3, 15)
    client_1.add_drink(2, 10)


    client_2 = RussianCook()
    client_2.add_food(1, 40)
    client_2.add_food(2, 25)
    client_2.add_drink(5, 20)

    client_3 = ItalianCook()
    client_3.add_food(2, 20)
    client_3.add_food(2, 30)
    client_3.add_drink(2, 10)

    assert client_1.total() == "Sushi: 105, Tea: 20, Total: 125"
    assert client_2.total() == "Dumplings: 90, Compote: 100, Total: 190"
    assert client_3.total() == "Pizza: 100, Juice: 20, Total: 120"
    print("Coding complete? Let's try tests!")
