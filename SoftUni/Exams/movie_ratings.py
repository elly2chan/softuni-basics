movies_quantity = int(input())
counter = 0
highest_rated_movie = ""
lowest_rated_movie = ""
max_rating = 0
min_rating = 11
all_ratings = 0

while counter < movies_quantity:
    movie_name = input()
    movie_rating = float(input())

    if movie_rating > max_rating:
        highest_rated_movie = movie_name
        max_rating = movie_rating

    if movie_rating < min_rating:
        lowest_rated_movie = movie_name
        min_rating = movie_rating

    all_ratings += movie_rating
    counter += 1

average_rating = all_ratings / movies_quantity

print(f'{highest_rated_movie} is with highest rating: {max_rating:.1f}')
print(f'{lowest_rated_movie} is with lowest rating: {min_rating:.1f}')
print(f'Average rating: {average_rating:.1f}')
