import pandas as pd
from sklearn.feature_extraction.text import TfidfVectorizer
from sklearn.metrics.pairwise import cosine_similarity

books = pd.read_csv("Books.csv")
print(books.head())

books.dropna(inplace=True)
books['Book-Title'] = books['Book-Title'].str.lower()
books['Book-Author'] = books['Book-Author'].str.lower()
books['Publisher'] = books['Publisher'].str.lower()

books['content'] = books['Book-Title'] + ' ' + books['Book-Author'] + ' ' + books['Publisher']

tfidf = TfidfVectorizer(stop_words='english')
tfidf_matrix = tfidf.fit_transform(books['content'])

cosine_sim = cosine_similarity(tfidf_matrix, tfidf_matrix)

def get_recommendations(title, cosine_sim=cosine_sim):
    idx = books[books['Book-Title'] == title.lower()].index[0]
    sim_scores = list(enumerate(cosine_sim[idx]))
    sim_scores = sorted(sim_scores, key=lambda x: x[1], reverse=True)
    book_indices = [i[0] for i in sim_scores[1:6]]
    return books['Book-Title'].iloc[book_indices]


def personalized_recommendations(title, author=None, year=None):
    recommendations = get_recommendations(title)
    
    if author:
        recommendations = recommendations[books['Book-Author'].str.contains(author)]
    if year:
        recommendations = recommendations[books['Year-Of-Publication'] == int(year)]
    
    return recommendations

