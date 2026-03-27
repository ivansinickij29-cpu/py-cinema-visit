from app.cinema.bar import CinemaBar
from app.cinema.hall import CinemaHall
from app.people.customer import Customer
from app.people.cinema_staff import Cleaner


def cinema_visit(customers: list, hall_number: int,
                 cleaner: str, movie: str) -> None:
    customer_object = []
    for customer in customers:
        customer_object.append(Customer(name=customer["name"],
                                        food=customer["food"],))
    cleaner_object = Cleaner(name=cleaner)
    hall = CinemaHall(number=hall_number)
    for customer in customer_object:
        CinemaBar.sell_product(product=customer.food, customer=customer)
    hall.movie_session(
        movie_name=movie,
        customers=customer_object,
        cleaning_staff=cleaner_object
    )
