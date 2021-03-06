# exercise 0 <Creating LISTS and DICTIONARIES>
# my lists
fav_colours = ["green", "teal", "gray", "black"]
ages_list = [25, 23, 17, 17, 49, 49]
# if heads -> True, tails -> False
coin_flips = ["heads", "heads", "heads", "tails", "heads"]
fav_artists = ["James Blake", "Post Malone", "Joji"]

# my dictionaries
words = {
"implication": "The conclusion that can be drawn from something although it is not explicitly stated.",
"truth": "That which is true or in accordance with fact or reality.",
"routine": "A sequence of actions regularly followed; a fixed program."
}
fav_movies = {
"Seven Pounds": 2008,
"Mad Max: Fury Road": 2015,
"The Fifth Element": 1997
}
cities = {
"Moscow": 12000000,
"Beijing": 21500000,
"Lisbon": 500000
}
ages_dict = {"Mia": 23, "Sasha": 17, "Nastja": 17, "Natalya": 49, "Sergey": 49}

# exercise 1
print("Exercise #1:")
print("---------------------------------")
print('*****')
print(coin_flips)
print('*****')
print(fav_colours[0])
print('*****')
# sort ages_list in ascending order
sorted_ages_list = sorted(ages_list)
print(sorted_ages_list)
print('*****')
# add a baby (0 years old) to the ages_list
ages_list.append(0)
print(ages_list)
print('*****')
# print when "The Fifth Element" was released
print(fav_movies["The Fifth Element"])
print('*****')
print("---------------------------------")

# exercise 2
print()
print("Exercise #2:")
print("---------------------------------")
print('*****')
print(fav_colours[len(fav_colours)-1])
print('*****')
cities["Abuja"] = 780000
print(cities)
print('*****')
reversed_coin_flips = list(reversed(coin_flips))
print(reversed_coin_flips)
print('*****')
print("The population of Moscow is {:,}".format(cities["Moscow"]))
print('*****')
for artist in fav_artists:
    print("I think {} is AWESOME".format(artist))
print('*****')
print("---------------------------------")

# exercise 3
print()
print("Exercise #3:")
print("---------------------------------")
print('*****')
for artist in fav_artists[0:2]:
    print(artist)
print('*****')
for movie, year in fav_movies.items():
    print("{} was released in {}.".format(movie, year))
print('*****')
sorted_and_reversed_ages_list = list(reversed(sorted(ages_list)))
print(sorted_and_reversed_ages_list)
print('*****')
fav_movies["Beauty and the Beast"] = [1991, 2017]
print(fav_movies)
print('*****')
print("---------------------------------")

# exercise 4
print()
print("Exercise #4:")
print("---------------------------------")
print('*****')
for age in ages_list:
    if age < 30:
        print(age)
print('*****')
max_age = max(ages_list)
print("The maximum age in the ages_list is {}.".format(max_age))
print('*****')
num_heads = 0
for flip in coin_flips:
    if flip == "heads":
        num_heads += 1
print("By looping through the coin_flips list:")
print("The coin came up heads {} time(s).".format(num_heads))
print("By using the .count() method:")
print("The coin came up heads {} time(s).".format(coin_flips.count("heads")))
print('*****')
fav_artists.pop(2)
print(fav_artists)
print('*****')
cities["Moscow"] = 11920000
print(cities)
print('*****')
print("---------------------------------")

# exercise 5
print()
print("Exercise #5:")
print("---------------------------------")
print('*****')
sum_total_population = 0
for population in cities.values():
    sum_total_population += population
print(cities)
print("The sum total population of all the cities in the list is {:,}.".format(sum_total_population))
print('*****')
for name, age in ages_dict.items():
    if age > 30:
        print("{} is old.".format(name))
    else:
        print("{} is young.".format(name))
print('*****')
print(fav_colours)
for colour in fav_colours[len(fav_colours)-2:]:
    print(colour)
print('*****')
for index, age in enumerate(ages_list):
    ages_list[index] = age + 1
print(ages_list)
print('*****')
fav_colours.append("white")
fav_colours.append("blue")
print(fav_colours)
print('*****')
print("---------------------------------")

# exercise 6
print()
print("Exercise #6:")
print("---------------------------------")
print('*****')
dict_of_movies = {
1999: ["The Matrix", "Star Wars: Episode 1", "The Mummy"],
2009: ["Avatar", "Sherlock Holmes", "Fast & Furious"],
2019: ["How to Train Your Dragon 3", "Toy Story 4", "Aladdin"]
}
print(dict_of_movies)
print('*****')
phone_buttons = [[1,2,3],[4,5,6],[7,8,9],['*',0,'#']]
print(phone_buttons)
print('*****')
countries_list = [
{'name': 'France', 'continent': 'Europe', 'isIsland': False},
{'name': 'Nigeria', 'continent': 'Africa', 'isIsland': False},
{'name': 'Brunei', 'continent': 'Asia', 'isIsland': True}
]
print(countries_list)
print('*****')
print("---------------------------------")

# exercise 7
print()
print("Exercise #7:")
print("---------------------------------")
print('*****')
for i in range(0,20):
    print("I will not skateboard in the halls")
print('*****')
message_list = []
for i in range(0,20):
    message_list.append("I will not skateboard in the halls")
print(message_list)
print(len(message_list))
print('*****')
number_list = []
for n in range(1,51):
    number_list.append(n)
print(number_list)
print(len(number_list))
print('*****')
sum = 0
for num in number_list:
    sum = sum + num
print("The total sum of numbers in the number_list is {}".format(sum))
print('*****')
number_list_2 = []
for k in range(1,51):
    for i in range(0,3):
        number_list_2.append(k)
print(number_list_2)
print(len(number_list_2))
print('*****')
land_countries = []
for country in countries_list:
    if not country['isIsland']:
        land_countries.append(country)
print("All countries:")
print(countries_list)
print("Land Countries:")
print(land_countries)
print('*****')
print("---------------------------------")

# exercise 8
print()
print("Exercise #8:")
print("---------------------------------")
print('*****')
my_expenses_2017 = [100, 55, 9.85, 15.70, 3.99, 52.99, 45, 147, 10.19]
my_expenses_2018 = [67, 42, 7.89, 23.43, 4.99, 546.99, 13.87, 132, 9.13]
def sum_expenses(expenses):
    sum = 0
    for expense in expenses:
        sum += expense
    return sum
print("My expenses in 2017:\n{:.2f}".format(sum_expenses(my_expenses_2017)))
print("My expenses in 2018:\n{:.2f}".format(sum_expenses(my_expenses_2018)))
print('*****')
print("---------------------------------")
