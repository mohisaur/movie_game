import random
import string 
movie_name=input("enter movie name: ")
iteration_count = 0
while len(movie_name) > 0:
    iteration_count += 1
    choice_type=random.choice(["letter","number"])
    if choice_type=="letter":
        random_letter=random.choice(string.ascii_letters)
        movie_name = movie_name.replace(random_letter, "")
    else:
        random_number=random.choice(string.digits)
        movie_name = movie_name.replace(random_number, "")
    
print(iteration_count)
