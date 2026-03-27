class CinemaHall:
    def __init__(self, number):
        self.number = number

    def movie_session(self, movie_name, customers, cleaning_staff):
        print (f"Movie {movie_name} started")
        for customer in customers:
            customer.watch_movie(movie_name)
        print (f"Movie {movie_name} ended")
        cleaning_staff.cleaning_hall(movie_name)