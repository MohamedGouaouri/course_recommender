import pandas as pd
import numpy as np
from pathlib import Path
import os

print(os.path.join(os.path.dirname(__file__), 'data/udemy_courses.csv'))
df = pd.read_csv(os.path.join(os.path.dirname(
    __file__), 'data/udemy_courses.csv'))
course_indices = pd.Series(
    df.index, index=df["course_title"]).drop_duplicates()
sim_matrix = np.load(os.path.join(
    os.path.dirname(__file__), 'store/sim_matrix.npy'))


def recommend_course(title, k=10):
    # Get index
    idx = course_indices[title]
    # Search inside sim_matrix
    scores = list(enumerate(sim_matrix[idx]))
    scores_sorted = sorted(scores, key=lambda x: x[1], reverse=True)
    # rec
    selected_course_indices = [i[0] for i in scores_sorted[1:]]
    selected_course_scores = [i[1] for i in scores_sorted[1:]]
    result = df['course_title'].iloc[selected_course_indices]
    rec_df = pd.DataFrame(result)
    rec_df["similarity_score"] = selected_course_scores
    return rec_df.head(k)
