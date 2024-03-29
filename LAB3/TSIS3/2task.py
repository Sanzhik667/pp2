movies = [
{
"name": "Usual Suspects", #0
"imdb": 7.0,
"category": "Thriller"
},
{
"name": "Hitman",         #1
"imdb": 6.3,
"category": "Action"
},
{
"name": "Dark Knight",    #2
"imdb": 9.0,
"category": "Adventure"
},
{
"name": "The Help",       #3
"imdb": 8.0,
"category": "Drama"
},
{
"name": "The Choice",     #4
"imdb": 6.2,
"category": "Romance"
},
{
"name": "Colonia",        #5
"imdb": 7.4,
"category": "Romance"
},
{
"name": "Love",           #6
"imdb": 6.0,
"category": "Romance"
},
{
"name": "Bride Wars",     #7
"imdb": 5.4,
"category": "Romance"
},
{
"name": "AlphaJet",       #8
"imdb": 3.2,
"category": "War"
},
{
"name": "Ringing Crime",  #9
"imdb": 4.0,
"category": "Crime"
},
{
"name": "Joking muck",    #10
"imdb": 7.2,
"category": "Comedy"
},
{
"name": "What is the name",      #11
"imdb": 9.2,
"category": "Suspense"
},
{
"name": "Detective",      #12
"imdb": 7.0,
"category": "Suspense"
},
{
"name": "Exam",           #13
"imdb": 4.2,
"category": "Thriller"
},
{
"name": "We Two",         #14
"imdb": 7.2,
"category": "Romance"
}
]
def sublist_movies_high_score(movies): 
    out_list=[];
    for i in range(0,len(movies)):
        curr_movie=movies[i];
        if curr_movie['imdb']>5.5:
            out_list.append(curr_movie)
    return out_list

print ('')
print ('Список фильмов с IMDB > 5.5: ')
print ('')
out_list=sublist_movies_high_score(movies)
print (out_list)