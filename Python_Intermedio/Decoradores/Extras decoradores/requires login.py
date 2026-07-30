def requires_login(func):
    def wrapper(*args, **kwargs):
        if not user_logged_in:
            raise Exception("User not authenticated")
        return func(*args, **kwargs)
    return wrapper

user_logged_in = False

@requires_login
def view_profile():
    print("Showing user's profile")

view_profile()