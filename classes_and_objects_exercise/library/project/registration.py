from project.user import User
from project.library import Library

class Registration:
    def add_user(self, user: User, library: Library):
        if user.user_id in [u.user_id for u in library.user_records]:
            return f"User with id = {user.user_id} already registered in the library!"

        library.user_records.append(user)


    def remove_user(self, user: User, library: Library):
        if user not in library.user_records:
            return "We could not find such user to remove!"

        library.user_records.remove(user)


    def change_username(self, user_id: int, new_username: str, library: Library):
        try:
            user = next(filter(lambda u: u.user_id == user_id, library.user_records))
        except StopIteration:
            return f"There is no user with id = {user_id}!"

        if user.username == new_username:
            return f"Please check again the provided username - it should be different than the username used so far!"

        user.username = new_username

        return f"Username successfully changed to: {new_username} for user id: {user_id}"