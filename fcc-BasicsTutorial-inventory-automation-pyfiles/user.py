# class is like a blueprint (similar to javascript constructors) that make Objects (individidual special attributes and functions)
# all classes have the __init__ function, executed automatically when we create objects from that class.
# init is like a constructor function
# self references the User class (its own class)
# self.attribute is only for the creation, but must be equal to the corresponding Class Parameter: self.email must be equal to user_email (param)

class User:
    def __init__(self, user_email, name, password, current_job_title):
        self.email = user_email
        self.name = name
        self.password = password
        self.current_job_title = current_job_title

    # methods (Like Javascript)
    def change_password(self, new_password):
        self.password = new_password

    def change_job_title(self, new_job_title):
        self.current_job_title = new_job_title

    def get_user_info(self):
        print(
            f"User {self.name} currently works as a {self.current_job_title} and you can contact them at {self.email}")


