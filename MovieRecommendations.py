from __future__ import print_function
import numpy as np

########################################################
# These functions will be used in Phase 3 (skip for now)
########################################################

def findSimilar(iLike, userLikes):
    # Create an And similarity
    similarityAnd = np.logical_and(iLike, userLikes)  # replace 0 with the correct code
    # Create a per user and sum
    similarityAndSum = np.sum(similarityAnd,axis = 1)  # replace 0 with the correct code
    # Create an Or similarity
    userSimilarityOr = np.logical_or(iLike, userLikes)  # replace 0 with the correct code

    # Calculate the similarity
    # replace 0 with the correct code to calculate the Jaccard Index for each user
    usersimilarity = similarityAndSum.astype(float) / np.sum(userSimilarityOr, axis = 1)

    usersimilarity = similarityAndSum/(userSimilarityOr.sum(axis = 1) - similarityAndSum)

    # Make the most similar user has a new like that the previous user did not have
    # I used a while loop.

    while True:
        maxIndex = usersimilarity.argmax()
        newLikes = userLikes[maxIndex] - iLike
        newCount = newLikes[newLikes> 0].sum()
        if newCount > 0:
             break
        else:
            usersimilarity[maxIndex] = 0

    # You can "get rid" of a user that is most similar, but doesn't have any new likes
    # by setting the userSimilarity for them to 0
    # When you get the index, save it in the variable maxIndex


    # Print the max similarity number (most times this is something like 0.17
    print("\n User similarity: " +str(usersimilarity[maxIndex]))
    return maxIndex

    # Return the index of the user which is the best match

def printMovie(id):
    # Print the id of the movie and the name.  This should look something like
    # "    - 430: Duck Soup (1933)" if the id is 430 and the name is Duck Soup (1933)
    print("    - "+ str(id) + ": "+ str(movieDict[id]))  # replace 0 with the correct code


def processLikes(iLike):
    print("\n\nSince you like:")

    # Print the name of each movie the user reported liking
    # Hint: Use a for loop and the printMovie function.
    for id in iLike:
        printMovie(id)
    # Convert iLike into an array of 0's and 1's which matches the array for other users
    # It should have one column for each movie (just like the userLikes array)
    # Start with all zeros, then fill in a 1 for each movie the user likes

    iLikeNp = np.zeros(maxMovie)

    for id in iLike:
        iLikeNp[id] = 1

    # Find the most similar user
    user = findSimilar(iLikeNp, userLikes)  # replace 0 with the correct code (hint: use one of your functions)
    print("\nYou might like: ")

    # Find the indexes of the values that are ones
    # https://stackoverflow.com/a/17568803/3854385(Note: You don't want it to be a list, but you do want to flatten it.)

    recLikes = np.argwhere(userLikes[user, :] == 1).flatten()  # replace 0 with the needed code

    # For each item the similar user likes that the person didn't already say they liked
    # print the movie name using printMovie (you'll also need a for loop and an if statement)
    for id in recLikes:
        if iLikeNp[id]:
            print (printMovie(id))


########################################################
# Begin Phase 1
########################################################

# Load Data
# Load the movie names data (u.item) with just columns 0 and 1 (id and name) id is np.int, name is S128
movieNames = np.loadtxt('./ml-100k/u.item',
                        dtype={'names': ('id', 'name'),
                               'formats': (np.int, 'S128')},
                        usecols=(0, 1), delimiter='|')  # replace 0 with the correct code to load the movie names

# Create a dictionary with the ids as keys and the names as the values
movieDict = [dict(zip(movieNames['id'], movieNames['name']))][0]  # replace 0 with the code to make the dict

# Load the movie Data (u.data) with just columns 0, 1, and 2 (user, movie, rating) all are np.int
movieData = np.loadtxt('./ml-100k/u.data',
                       dtype={'names': ('user', 'movie', 'rating'),
                              'formats': (np.int, np.int, np.int)},
                       usecols=(0, 1, 2), delimiter="\t")  # replace 0 with the correct cod eto load the movie data
#print(movieData)
#print(movieNames)

# exit(0)  # Remove this line after we finish phase 1

########################################################
# Begin Phase 2
########################################################
# Compute average rating per movie
# This is non-ideal, pandas, scipy, or graphlib should be used here

# Create a dictionary to hold our temporary ratings
movieRatingTemp = {}  # replace 0 with code for an empty dictionary

# For every row in the movie data, add the rating to a list in the dictionary entry
# for that movies ID (don't forget to initialize the dictionary entry)
for movie in movieData:
    if movie['movie'] not in movieRatingTemp:
        movieRatingTemp[movie['movie']] = []

    movieRatingTemp[movie['movie']].append(movie['rating'])

# Create an empty dictionary for movieRating and movieRatingCount
movieRating = {}  # replace 0 with code for an empty dictionary
movieRatingCount = {}  # replace 0 with code for an empty dictionary

# Using numpy place the average rating for each movie in movieRating and the total number of ratings in movieRatingCount
# Note: You will need a for loop to get each dictionary key
for key in movieRatingTemp:
    movieRating[key] = np.mean(movieRatingTemp[key])
    movieRatingCount[key] = len(movieRatingTemp[key])

#print(movieRating)
#print(movieRatingCount)

# Get sorting ratings
# https://www.saltycrane.com/blog/2007/09/how-to-sort-python-dictionary-by-keys/
movieRatingS = sorted(movieRating.iteritems(),
                      key=lambda (k, v): (v, k), reverse=True)

# Top 10 Movies
# Print the top 10 movies
# It should print the number, title, id, rating and count of reviews for each movie
# ie 2. Someone Else's America (1995) (ID: 1599) Rating: 5.0 Count: 1
print("\nTop Ten Movies:")
for i in range(0, 10):
    key = movieRatingS[i][0]
    print(str(i + 1), "Name: " + str(movieDict[key]) +
          " Rating: " + str(movieRatingS[i][1]) +
          " Rating Count: " + str(movieRatingCount[key]))

    i += 1

# Top 10 Movies with at least 100 ratings
# It should print the same thing, but this time all the movies should have over 100 ratings
# The number should be the movie's absolute rank
# ie (16. Close Shave, A (1995) (ID: 408) Rating: 4.49 Count: 112)
# Number 16 is first in this list because it's the first movie with over 100 ratings

print("\n\nTop Ten movies with at least 100 ratings:")

MoviesPrinted = 0
i = 0
while MoviesPrinted < 10:
    key = movieRatingS[i][0]
    if movieRatingCount[key] >= 100:
        print(str(i + 1), "Name: " + str(movieDict[key]) +
              " Rating: " + str(movieRatingS[i][1]) +
              " Rating Count: " + str(movieRatingCount[key]))
        MoviesPrinted += 1

    i += 1
print ("\n")
#  exit(0) Remove this line after we finish phase 2
#  MoviesPrinted +1 instead of 1 to go from 1 to 10

########################################################
# Begin Phase 3
########################################################

# Create a user likes numpy ndarray so we can use Jaccard Similarity
# A user "likes" a movie if they rated it a 4 or 5
# Create a numpy ndarray of zeros with dimensions of max user id + 1 and max movie + 1
# (because we'll use them as 1 indexed not zero indexed)
# Find the max movie ID + 1
maxMovie = movieData['movie'].max() + 1  # replace 0 with the correct code

# Find the max user Id + 1
maxUser = movieData ['user'].max() + 1  # replace 0 with the correct code

# Create an array of 0s which will fill in with 1s when a user likes a movie
userLikes = np.zeros((maxUser, maxMovie))
#  convert movies in userLikes to 1
# Go through all the rows of the movie data.
# If the user rated a movie as 4 or 5 set userLikes to 1 for that user and movie
# Note: You'll need a for loop and an if statement

for row in movieData:
    if row["rating"] >= 4:
        userLikes[row['user'], row['movie']] = 1

########################################################
# At this point, go back up to the top and fill in the
# functions up there
########################################################

# First sample user
# User Similiarity: 0.133333333333
iLike = [655, 315, 66, 96, 194, 172]
processLikes(iLike)

# What if it's an exact match? We should return the next closest match
# Second sample case
# User Similiarity: 0.172413793103
iLike = [79, 96, 98, 168, 173, 176, 194, 318, 357, 427, 603]
processLikes(iLike)

# What if we've seen all the movies they liked?
# Third sample case
# User Similiarity: 0.170731707317
iLike = [79, 96, 98, 168, 173, 176, 194, 318, 357, 427, 603, 1]
processLikes(iLike)

# If your code completes the above recommendations properly, you're ready for the last part,
# allow the user to select any number of movies that they like and then give them recommendations.
# Note: I recommend having them select movies by ID since the titles are really long.
# You can just assume they have a list of movies somewhere so they already know what numbers to type in.
# If you'd like to give them options though, that would be a cool bonus project if you finish early.

while True:
    run = raw_input("\nWOuld you like ot get a recommendation (Y/N) ")
    if len(run) == 0 or run[0] != "Y":
        break
    iLike = []
    while True:
        movie =raw_input("Enter a movie ID that you like [1-" +str(maxMovie)+ "]"+ "leave blank if done:  ")

        try:
            movieInt = int(movie)
        except ValueError:
            movieInt = 0

        if len(movie) == 0:
            break
        elif movieInt < 1 or movieInt > maxMovie:
            print("Invalid Selection")
            continue
        else:
            iLike.append(movieInt)

        if len(iLike) > 0:
            processLikes(iLike)
        else:
            print("You didn't enter any movies you like so we couldn't make any " +
                  "suggestions!")

"""
user = raw_input("Would you like a movie recommendation? (Y/N)")
if "Y":
    user = True
    while True:
        user_likes = raw_input("Please enter the ID (1-1683) for the movies you like (type ' ' when finished):")
        if user_likes.isdigit():
            if user_likes.isdigit() <= 1683:
                iLike.append(int(user_likes))
                print (iLike)
        elif user_likes == ' ':
            print (processLikes(iLike))
            break
        else:
            print ("Invalid")
else:
    user = False
    exit(0)

"""