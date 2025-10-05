class Ticket:
    def __init__(self, seat_number, ticket_class, price):
        self.seat_number=seat_number
        self.ticket_class=ticket_class
        self.price=price
        self.__airport_fee=100

    def show_info(self):
        print(f"Seat: {self.seat_number}, Class: {self.ticket_class}, Price: {self.price}")

    def change_seat(self, new_seat):
        self.seat_number=new_seat

    def total_price(self):
        return self.price+self.__airport_fee

    @staticmethod
    def ticket_description():
        return "Ticket includes seat number, class and price"

    def generate_receipt(self):
        print(f"Receipt: Seat {self.seat_number}, Class {self.ticket_class}, Total {self.total_price()} UAH")

class InternationalTicket(Ticket):
    def __init__(self, seat_number, ticket_class, price, passport_number):
        super().__init__(seat_number, ticket_class, price)
        self.passport_number=passport_number

    def requires_visa(self):
        return self.ticket_class=="Economy"

class Employee:
    def __init__(self, name, position):
        self.name=name
        self.position=position

    def get_role(self):
        return f"{self.name} works as {self.position}"

class StaffTicket(Ticket, Employee):
    def __init__(self, seat_number, ticket_class, price, name, position):
        Ticket.__init__(self, seat_number, ticket_class, price)
        Employee.__init__(self, name, position)

    def staff_discount(self):
        return self.price * 0.5

if __name__ == "__main__":
    t1=Ticket("12A", "Economy", 1200)
    t2=InternationalTicket("16A", "Business", 2500, "BA132435")
    t3=StaffTicket("2C", "Economy", 1000, "Ivan", "Steward")
    tickets=[t1,t2,t3]
    for ticket in tickets:
        print (f"{ticket.__class__.__name__}: {ticket.total_price()}")

    t1.show_info()
    t1.change_seat("23B")
    t1.show_info()

    print(t2.requires_visa())
    print(t3.staff_discount())
    print(t3.get_role())

    t1.generate_receipt()
    t2.generate_receipt()
    t3.generate_receipt()
