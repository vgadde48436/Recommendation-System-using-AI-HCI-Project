import pandas as pd
from sklearn.feature_extraction.text import CountVectorizer
from sklearn.metrics.pairwise import cosine_similarity


def load_data(file_path):
    """
    Loads the movie dataset from a CSV file.
    """
    try:
        movies = pd.read_csv(file_path)
        return movies
    except FileNotFoundError:
        print("Error: movies.csv file not found.")
        return None


def prepare_data(movies):
    """
    Cleans the dataset and combines important features into one column.
    """
    movies = movies.fillna("")

    movies["combined_features"] = (
        movies["title"] + " " +
        movies["genre"] + " " +
        movies["overview"] + " " +
        movies["keywords"]
    )

    return movies


def build_similarity_matrix(movies):
    """
    Converts text data into numerical form and calculates cosine similarity.
    """
    vectorizer = CountVectorizer(stop_words="english")
    feature_matrix = vectorizer.fit_transform(movies["combined_features"])

    similarity_matrix = cosine_similarity(feature_matrix)

    return similarity_matrix


def recommend_movies(movie_title, movies, similarity_matrix, number_of_recommendations=5):
    """
    Recommends movies similar to the movie title entered by the user.
    """
    movie_title = movie_title.lower()

    movie_titles = movies["title"].str.lower().tolist()

    if movie_title not in movie_titles:
        print("\nMovie not found in the dataset.")
        print("Please check the spelling or try another movie title.")
        return

    movie_index = movie_titles.index(movie_title)

    similarity_scores = list(enumerate(similarity_matrix[movie_index]))

    sorted_movies = sorted(
        similarity_scores,
        key=lambda x: x[1],
        reverse=True
    )

    print("\nRecommended Movies:")
    print("-------------------")

    count = 0

    for index, score in sorted_movies:
        if index != movie_index:
            print(f"{count + 1}. {movies.iloc[index]['title']}")
            count += 1

        if count == number_of_recommendations:
            break


def main():
    """
    Main function to run the recommendation system.
    """
    print("Movie Recommendation System")
    print("===========================")

    movies = load_data("movies.csv")

    if movies is None:
        return

    movies = prepare_data(movies)

    similarity_matrix = build_similarity_matrix(movies)

    print("\nAvailable Movies:")
    print("-----------------")

    for title in movies["title"]:
        print("-", title)

    user_input = input("\nEnter a movie title: ")

    recommend_movies(user_input, movies, similarity_matrix)


if __name__ == "__main__":
    main()