# Move dataset

Our dataset comes from [kaggle](https://www.kaggle.com/rounakbanik/the-movies-dataset#movies_metadata.csv)

It contains 7 files of data, each containing information about movies.

The files are:
* Credits.csv
    * Cast and Crew information about each movie in data set
* Keywords.csv
    * Keywords for each movie in data set
* links.csv
    * Linking id's of movies in our data set to id'd of movies in IMDB's dataset and tmdb's dataset
* links_small.csv
    * same as links.csv but only on smaller subset
* Movies_metadata.csv
    * meta information about movies
* ratings.csv
    * Ratings of movies for each individual user
* rating_small.csv
    * Same as ratings.csv but again only on subset

# Ideas on what to do with dataset


* Word clouds for movies by directors
* Sentiment analysis of movies made by each director

* Word cloud and sentiment of each director but only on their most popular moovie
    * Comparison of their best move to their usual style

* Graph of actors, being connected if they stared in the same movie
* Connecting directors with each other based on actors that stared in
    movies directed by both of the directors
    * Neighbourhood analysis
    * Connecting measures on both graphs

Top rated movies in each genre (top 10 or 20)
* Sentiment analysis of them
* Word cloud for each of them and comparison

metadata:
* adult
    * boolean value stating if move is an adult move or not
* belongs_to_collection
    * information if movie is a part of a collection or not
* budget
    * Money spend on making the movie
* genres
    * List of genres of the movie
* homepage
    * link to movie's homepage if there is one
* id
    * of movie
* imdb_id
    * the id in imdb database for this move
* original_language
    * Language in which move was recorded
* original_title
    * Title in the original language
* overview
    * Short text describing the movie
* popularity
    * popularity rating of the movie (higher ins better)
* poster_path
    * link to poster for the movie
* production_companies
    * name of company that produced the movie
* production_countries
    * country of production company
* release_date
    * release date
* revenue
    * how much money was made by movie
* runtime
    * length of the movie
* spoken_languages
    * language of move
* status
    * released or rumoured
* tagline
    * Really short description of the movie
* title
    * title of the movie
* video
* vote_average
    * average vote
* vote_count
    * number of votes

# Video script

Hello, we are Marita, Tanguy and Luka and as our project we are gonna
analise the movie database from Kaggle.

First of all we wanna say something about the data we are using.
Or dataset is made ot of 7 files that all contain information about movies.
The main file is the one containing all metadata for each movie.
The useful parameters/features we have about each movie are:

* title
    * title of the movie
* budget
    * Money spend on making the movie
* revenue
    * how much money was made by movie

* genres
    * List of genres of the movie
* overview
    * Short text describing the movie
* tagline
    * Really short description of the movie

* original_language
    * Language in which move was recorded
* production_companies
    * name of company that produced the movie
* release_date
    * release date
* status
    * released or rumoured
* belongs_to_collection
    * information if movie is a part of a collection or not
* imdb_id
    * Id of a movie in imdb database

* popularity
    * popularity rating of the movie (higher ins better)
* vote_average
    * average vote
* vote_count
    * number of votes

Other files mostly contain links to other databases for movies, and information
about cast and crew for each movie. The whole data set contains around 45000 movies.
If we inclue all of the subtitles we have arround 60 GB's of

We decided to only analise the 5000 movies with highest revenue and
filtered movies that are already realised only realised movies. For each
of this movie we also downloaded subtitles to use in analysis. We decided to go with
the subset due to performance and space issues with the whole data set.

There are 18.694 of actors with (CONNECTION NUMBER) connections connecting the network.
We also created an director graph, with (DIRECTOR_NUM) directors and (DIRECTOR CONNECTIONS)
connections between them in our data set.

In our analysis we will include:

Graph of actors being connected with each other if they worked together on one of the
movie in our dataset. We will analise the network, to see how it looks like.
We wanna see if there are communities within actor community, see if the
network looks like normal random network. We predict we may find the marvel actors community.
See also wanna see actors have the highest degree in the graph...

We are interested on what is the length of longest path between two actors,
what is the average distance between them ...

We will also create a network of directors, being connected
1. if they worked with each other
2. if they worked with the same actors
In this network we plan to do similar analysis than before.

We will also analise moves done by directors, and calculate their sentiment.
We will try to say something about the style of each director based on this.
We are also interested in directors that usually do really positive/negative
movies and to se the word cloud of that directors.

We also wanna do the same thing for actors, and try to see if actors with
positive/negative sentiment usually work with directors with positive/negative sentiment

Another interesting thing we wanna do is to do sentiment analysis only
for each genre. To se how genre effects sentiment

There is also a posibility of comparing sentiment of the most popular
movie done by director/actor in comparision to that director/actor's
avarage sentiment. We are interested in how much does the most polular
movie differ from their usual style.

We were also thinking of comparing sentiment of overviews of movies to the movies itself.

In the end we will try to create the perfect movie. Take word-clouds to
create a new title. Take the most popular genre...

Thanks for your attention. Hope you like our ideas. If you have any
suggestions please feel free to talk with us!
