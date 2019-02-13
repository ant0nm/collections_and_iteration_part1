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

print('*****')
print("---------------------------------")
