# exercise 0 <Creating LISTS and DICTIONARIES>
# my lists
fav_colours = ["green", "teal", "gray", "black"]
ages_list = [25, 23, 17, 17, 49]
# if heads -> True, tails -> False
coin_flips = ["Heads", "Heads", "Heads", "Tails", "Heads"]
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
ages_dict = {"Mia": 23, "Sasha": 17, "Nastja": 17, "Natalya": 49}

# exercise 1
print(coin_flips)
print(fav_colours[0])
# sort ages_list in ascending order
sorted_ages_list = sorted(ages_list)
print(sorted_ages_list)
# add a baby (0 years old) to the ages_list
ages_list.append(0)
print(ages_list)
# print when "The Fifth Element" was released
print(fav_movies["The Fifth Element"])
