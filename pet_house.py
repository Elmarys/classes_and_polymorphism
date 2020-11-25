class Customer:

    def __init__(self, name, surname, remaining_balance):
        self.name = name
        self.surname = surname
        self.remaining_balance = remaining_balance
    def customer_info (self):
        return 'Клиент: "{0} {1}" Баланс: "{2}"'.format(self.name, self.surname, self.remaining_balance)


class Database:

    def __init__(self, db=[]):
        self.db = db
    def add_to_database(self, customer):
        return self.db.append(
                'Клиент: "{0} {1}" Баланс: "{2}"'.format(customer.name, customer.surname, customer.remaining_balance))
    def show_database(self):
        for customer in self.db:
            print(customer)


ivan = Customer("Иван", "Петров", "50 рублей")
ignat = Customer("Игнат", "Сидоров", "0 рублей")

db = Database()

db.add_to_database(ivan)
db.add_to_database(ignat)

print(ivan.customer_info())
print(ignat.customer_info())


db.show_database()
