from datetime import date

class User:

    def __init__(self, date_of_birth):
        self.date_of_birth = date_of_birth

    @property
    def age(self):
        today = date.today()
        return (
            today.year
            - self.date_of_birth.year
            - ((today.month, today.day) < (self.date_of_birth.month, self.date_of_birth.day))
        )

def adult_only(func):
    def wrapper(user, *args, **kwargs):
        if user.age < 18:
            raise ValueError(f"User is not an adult. Age: {user.age}")
        return func(user, *args, **kwargs)
    return wrapper

@adult_only
def buy_alcohol(user):
    print(f"User can buy alcohol. Age: {user.age}")

adult_user = User(date(1990, 1, 1))
young_user = User(date(2015, 6, 15))

buy_alcohol(adult_user)
buy_alcohol(young_user)