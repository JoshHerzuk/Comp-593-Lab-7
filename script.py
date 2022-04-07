##
#
# Description:
#   This scripts creates and edits a complex data structure and uses that information to print out a couple of sentences
#
# Usage:
#   python script.py 
#
# 
#
#
##########################################################################################################################


def main():

    student_info = {
        'name': 'Joshua',
        'student_id': '10263982',
        'pizza_toppings': ['Sopressata', 'Green Olives', 'Hot Peppers'],
        'movies': [
            {'title': 'The Big Lebowski',
             'genre': 'comedy'
            },
            {'title': 'The Lord of The Rings',
             'genre': 'fantasy'
            }
        ]
    }


    #append new movie
    new_movie = {'title': 'Blade Runner 2049', 'genre': 'sci-fi'}
    student_info['movies'].append(new_movie)

    add_toppings = ('Bacon', 'Arugula', 'Peperoni')
    add_pizza_toppings(student_info, add_toppings)

    print_favourites(student_info)

#add new pizza toppings
def add_pizza_toppings(favourites_info, new_toppings):

    for _ in new_toppings:
        favourites_info['pizza_toppings'].append(_)

    favourites_info['pizza_toppings'].sort()

#this function creates the sentence that will be printed out
def print_favourites(fav_info):

    # defines the start of the sentence
    sentence = "Hello Jeremy my name is " + fav_info['name'] + " and my student number is " + fav_info['student_id'] + "\n"

    #adds a line about pizza toppings
    sentence += 'My ideal pizza has ' 

    for i,g in enumerate(fav_info['pizza_toppings']):
       
        if i < len(fav_info['pizza_toppings']) - 1:
            sentence += g.lower() + ', '

        else:
            sentence += 'and '+ g.lower() + ".\n"

    #adds a sentence about movie genres
    sentence += 'I like to watch '

    for i, g in enumerate(fav_info['movies']):

        if i < len(fav_info['movies']) - 1:

            sentence += g['genre'] + ', '

        else:
            sentence += 'and ' + g['genre'] + ' movies.\n'

    #adds a sentence about movie titles
    sentence += 'Some of my favourites are '

    for i, g in enumerate(fav_info['movies']):

        if i < len(fav_info['movies']) - 1:

            sentence += g['title'] + ', '

        else:
            sentence += 'and ' + g['title'] + '!\n'


    print(sentence)



main()

