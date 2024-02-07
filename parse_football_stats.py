import re
import os
from bs4 import BeautifulSoup
import pandas as pd

def parse_football_stats(filename):
    """
    Parse football match statistics from an HTML file and structure the data into a pandas DataFrame.

    Parameters:
    filename (str): The path to the HTML file containing football match statistics.

    Returns:
    pandas.DataFrame: A DataFrame containing parsed football match statistics, including team names, scores, odds, probabilities, and sorted by probabilities in descending order.
    """

    with open(filename, 'r', encoding='utf-8') as file:
        html_content = file.read()

    soup = BeautifulSoup(html_content, 'html.parser')

    team_elements = soup.find_all('div', class_='bbl-StickyMarketColumnHeader_Label')
    score_elements = soup.find_all('span', class_='bbl-BetBuilderParticipant_Name')
    odds_elements = soup.find_all('span', class_='bbl-BetBuilderParticipant_Odds')
    
    team_choices = [team.text for team in team_elements]
    score = [score.text for score in score_elements]
    odds = [odds.text for odds in odds_elements]
    
    home_team = True
    teams = []
    
    # Add in the team names based on the scores as html is formatted with columnns
    for current_score in score:
        if current_score.split('-')[0] == current_score.split('-')[1]:
            current_team = team_choices[1]
            home_team = False
        elif home_team:
            current_team = team_choices[0]
        else:
            current_team = team_choices[2]
        teams.append(current_team)
    
    game = team_choices[0] + ' vs ' + team_choices[2]
    df = pd.DataFrame({'Game': game,'Team': teams, 'Score': score, 'Odds': odds})
    
    df['Probability'] = df['Odds'].apply(lambda x: float(x.split('/')[1]) / float(x.split('/')[0]))
    df.sort_values(by='Probability', ascending=False, inplace=True, ignore_index=True)
    
    return df
  
    

#test func
# print(parse_football_stats('Matches 060224/luton_sheffutd.html'))
