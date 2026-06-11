# Recommendation-System-using-AI-HCI-Project
# Recommendation System using AI - HCI Project

## Project Overview

This project is a simple movie recommendation system created using artificial intelligence techniques. The system uses a content-based recommendation approach to suggest movies that are similar to a movie entered by the user.

The purpose of this project is to demonstrate how intelligent systems can help users make better decisions by filtering large amounts of information and recommending relevant options.

## Recommendation System Type

This project uses a content-based filtering method. Content-based filtering recommends items based on item features such as title, genre, overview, and keywords. In this project, movie features are converted into numerical form and compared using similarity measurement.

## Features

- Accepts a movie title from the user
- Searches for the movie in the dataset
- Calculates similarity between movies
- Recommends similar movies
- Provides a simple text-based interface
- Includes basic error handling for unavailable movie titles

## Technologies Used

- Python
- Pandas
- Scikit-learn
- CountVectorizer
- Cosine Similarity

## Files Included

- `app.py` - Main Python file for the recommendation system
- `movies.csv` - Sample movie dataset
- `requirements.txt` - Required Python libraries
- `README.md` - Project documentation

## How to Run the Project

1. Install Python on your computer.
2. Download or clone this repository.
3. Open the project folder in VS Code, PyCharm, or terminal.
4. Install the required libraries:

```bash
pip install -r requirements.txt
