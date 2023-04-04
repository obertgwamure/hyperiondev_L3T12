import spacy

# Load the pre-trained word embeddings model
nlp = spacy.load("en_core_web_md")

# Read the movie descriptions from a file
with open("movies.txt", "r") as f:
    movies = [line.strip() for line in f]

def watch_next(description):
    # Calculate the similarity between the input description and all other movie descriptions
    similarity_scores = []
    for movie in movies:
        similarity = nlp(description).similarity(nlp(movie))
        similarity_scores.append(similarity)

    # Get the index of the movie with the highest similarity score
    max_index = similarity_scores.index(max(similarity_scores))

    # Return the title of the movie with the highest similarity score
    return f"Next movie to watch: {movies[max_index]}"

# Test the function with the given input description
description = "Will he save their world or destroy it? When the Hulk becomes too dangerous for the Earth, the Illuminati trick Hulk into a shuttle and launch him into space to a planet where the Hulk can live in peace. Unfortunately, Hulk land on the planet Sakaar where he is sold into slavery and trained as a gladiator."
print(watch_next(description))
