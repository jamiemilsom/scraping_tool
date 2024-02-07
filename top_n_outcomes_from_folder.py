import os
import pandas as pd
from parse_football_stats import parse_football_stats

def top_n_outcomes_from_folder(directory, n_outcomes=2):
    """
    Retrieve the top 'n_outcomes' outcomes from HTML files in the specified directory.

    Parameters:
    directory (str): The path to the directory containing HTML files with football match statistics.
    n_outcomes (int, optional): The number of top outcomes to retrieve. Defaults to 2.

    Returns:
    pandas.DataFrame: A DataFrame containing the top 'n_outcomes' outcomes, including teams, scores, odds, and probabilities.
    """
    top_n_outcomes = {'Game': [], 'Team': [], 'Score': [], 'Odds': [], 'Probability': []}

    for filename in os.listdir(directory):
        if filename.endswith(".html"):
            outcomes_df = parse_football_stats(f'{directory}/{filename}')
            top_n_df = outcomes_df.head(n_outcomes)

            top_n_outcomes['Game'].extend([top_n_df.iloc[0]['Game']] * n_outcomes)
            top_n_outcomes['Team'].extend(top_n_df['Team'].tolist())
            top_n_outcomes['Score'].extend(top_n_df['Score'].tolist())
            top_n_outcomes['Odds'].extend(top_n_df['Odds'].tolist())
            top_n_outcomes['Probability'].extend(top_n_df['Probability'].tolist())
            
    top_n_outcomes_df = pd.DataFrame(top_n_outcomes)

    return top_n_outcomes_df


# test func
# directory = 'Matches 060224'
# outcomes = top_n_outcomes_from_folder(directory, 5)
# print(outcomes)
