movies = [
{
"name": "Usual Suspects", 
"imdb": 7.0,
"category": "Thriller"
},
{
"name": "Hitman",
"imdb": 6.3,
"category": "Action"
},
{
"name": "Dark Knight",
"imdb": 9.0,
"category": "Adventure"
},
{
"name": "The Help",
"imdb": 8.0,
"category": "Drama"
},
{
"name": "The Choice",
"imdb": 6.2,
"category": "Romance"
},
{
"name": "Colonia",
"imdb": 7.4,
"category": "Romance"
},
{
"name": "Love",
"imdb": 6.0,
"category": "Romance"
},
{
"name": "Bride Wars",
"imdb": 5.4,
"category": "Romance"
},
{
"name": "AlphaJet",
"imdb": 3.2,
"category": "War"
},
{
"name": "Ringing Crime",
"imdb": 4.0,
"category": "Crime"
},
{
"name": "Joking muck",
"imdb": 7.2,
"category": "Comedy"
},
{
"name": "What is the name",
"imdb": 9.2,
"category": "Suspense"
},
{
"name": "Detective",
"imdb": 7.0,
"category": "Suspense"
},
{
"name": "Exam",
"imdb": 4.2,
"category": "Thriller"
},
{
"name": "We Two",
"imdb": 7.2,
"category": "Romance"
}
]

2.1
Write a function that:
Accepts a single movie dictionary from the movies list as an argument.
Returns True if the IMDB score is above 5.5.

def imdb(title):
    for i in movies:
        if i["name"] == title:
            if i["imdb"] > 5.5:
                return True
            else:
                return False
#imdb("Hitman")
imdb("Exam")
#imdb("We Two")

3.1

Write a function that:

1. Accepts the list of movies and a specified imdb score.
2. Returns the sublist of movies that have a score greater than the specified score.

def imdb_greater(list,score):
    list_greater = []
    for i in list:
        if i["imdb"] > score:
            list_greater.append(i["name"])
    return list_greater
imdb_greater(movies, 6.0)

4.1
Write a function that:
Accepts the movies list and a category name.
Returns the movie names within that category (case-insensitive!)
If the category is not in the data, print a message that it does not exist and return None.

def category(list,name):
    name_lower = name.lower()
    cat_list = []
    for i in list:
        if i["category"].lower() == name_lower:
            cat_list.append(i["name"])
    return cat_list
category(movies,"Romance")

5.1
Write a function that:
Accepts the movies list and a "search criteria" variable.
If the criteria variable is numeric, return a list of movie titles with a score greater than or equal to the criteria.
If the criteria variable is a string, return a list of movie titles that match that category (case-insensitive!). If there is no match, return an empty list and print an informative message.

def search(list,criterion):
    new_list = []
    for i in list:
        if type(criterion) in [int, float]:
            if i["imdb"] >= criterion:
                new_list.append(i["name"])
        else:
            if i["category"].lower() == criterion.lower():
                new_list.append(i["name"])
    if type(criterion) == str and len(new_list) == 0:
        print ("There are no movies matching that category")
    else:
        return new_list
search(movies,"Romance")


