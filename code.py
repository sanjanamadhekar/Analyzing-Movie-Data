# --------------
from csv import reader


def explore_data(dataset, start, end, rows_and_columns=False):
    
    """Explore the elements of a list.
    
    Print the elements of a list starting from the index 'start'(included) upto the index 'end'         (excluded).
 
    Keyword arguments:
    dataset -- list of which we want to see the elements
    start -- index of the first element we want to see, this is included
    end -- index of the stopping element, this is excluded 
    rows_and_columns -- this parameter is optional while calling the function. It takes binary          values, either True or False. If true, print the dimension of the list, else dont.
    """
    printable = dataset[start:end]
    for i in printable:
        print(i)
        print()
    if rows_and_columns:
        if isinstance(dataset, list):
            print("rows = "+ str(len(dataset)))
        if isinstance(dataset[start], list):
            print("columns = "+ str(len(dataset[start])))
        
        
def duplicate_and_unique_movies(dataset, index_):
    """Check the duplicate and unique entries.
    
    We have nested list. This function checks if the rows in the list is unique or duplicated based on the element at index 'index_'.
    It prints the Number of duplicate entries, along with some examples of duplicated entry.
    
    Keyword arguments:
    dataset -- two dimensional list which we want to explore
    index_ -- column index at which the element in each row would be checked for duplicacy 
    
    """
    
    unique_names_list = []
    duplicate_names_list = []
    
    for i in movies:
        if i[index_] not in unique_names_list:
            unique_names_list.append(i[index_])
        elif i[index_] in unique_names_list:
            duplicate_names_list.append(i[index_])
    
    for i in unique_names_list:
        if i in duplicate_names_list:
            unique_names_list.remove(i)
    
    return unique_names_list,duplicate_names_list


def movies_lang(dataset, index_, lang_):
    """Extract the movies of a particular language.
    
    Of all the movies available in all languages, this function extracts all the movies in a            particular laguage.
    Once you ahve extracted the movies, call the explore_data() to print first few rows.

    Keyword arguments:
    dataset -- list containing the details of the movie
    index_ -- index which is to be compared for langauges
    lang_ -- desired language for which we want to filter out the movies
    
    Returns:
    movies_ -- list with details of the movies in selected language
    
    """
    
    movies_ = [i for i in dataset if i[index_] == lang_]
    
    return movies_
    



def rate_bucket(dataset, rate_low, rate_high):
    """Extract the movies within the specified ratings.
    
    This function extracts all the movies that has rating between rate_low and high_rate.
    Once you ahve extracted the movies, call the explore_data() to print first few rows.
    
    Keyword arguments:
    dataset -- list containing the details of the movie
    rate_low -- lower range of rating
    rate_high -- higher range of rating
    
    Returns:
    rated_movies -- list of the details of the movies with required ratings
    """
    
    rating_index = movies_header.index('vote_average')
    rated_movies = [i for i in dataset if (rate_high)>=float(i[rating_index])>=(rate_low)]

    return rated_movies




# Read the data file and store it as a list 'movies'
opened_file = open(path, encoding="utf8")
read_file = reader(opened_file)
movies = list(read_file)


# The first row is header. Extract and store it in 'movies_header'.
movies_header = movies[0]
print(movies_header)

# Subset the movies dataset such that the header is removed from the list and store it back in movies

movies.remove(movies[0])
# Delete wrong data


# Explore the row #4553. You will see that as apart from the id, description, status and title, no other information is available.
# Hence drop this row.
explore_data(movies,4553,4554)
movies.remove(movies[4553])

# Using explore_data() with appropriate parameters, view the details of the first 5 movies.


explore_data(movies,1,6,True)


# Our dataset might have more than one entry for a movie. Call duplicate_and_unique_movies() with index of the name to check the same.
name_index = movies_header.index('title_movies')
unique, duplicate = duplicate_and_unique_movies(movies, name_index)


# We saw that there are 3 movies for which the there are multiple entries. 
# Create a dictionary, 'reviews_max' that will have the name of the movie as key, and the maximum number of reviews as values.

reviews_max = {}

review_count_index = movies_header.index('vote_count')

for name in duplicate:
    reviews_count_list = [int(i[review_count_index]) for i in movies if i[name_index] == name]
    reviews_max[name] = max(reviews_count_list)
    
# Create a list 'movies_clean', which will filter out the duplicate movies and contain the rows with maximum number of reviews for duplicate movies, as stored in 'review_max'. 
movies_clean = [i for i in movies if (i[name_index] in unique or (i[name_index] in duplicate and (int(i[review_count_index]) == reviews_max[i[name_index]])))]

# Calling movies_lang(), extract all the english movies and store it in movies_en.

movies_en = movies_lang(movies_clean,movies_header.index('original_language'),'en')

# Call the rate_bucket function to see the movies with rating higher than 8.
high_rated_movies = rate_bucket(movies_en,8,10)


