from post import Post
from user import User

app_user_one = User( 'oliver@gmail.com', "Oliver", "007896Asd", "Minmed")
app_user_one.get_user_info()
app_user_one.change_job_title("male")
app_user_one.get_user_info()


app_user_two = User('Johnong@gmail.com', "John", "007896Dfg", "Woo")
app_user_two.get_user_info()

new_post = Post("on a secret mission today", app_user_two.name)

new_post.get_post_info()