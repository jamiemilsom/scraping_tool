import re
import os

def get_outcomes(filename):
    text = open(filename, 'r', encoding='utf-8').read()

    # Split the text based on the team name

    halfs = re.split(r'herItem_TabText ">Full Time Score</div></div><div data-con', text)

    text = halfs[1]

    split_text = re.split(r'<div class="bbl-StickyMarketColumnHeader_Label ">(.*?)<\/div>', text)

    home, draw, away = split_text.pop(1), split_text.pop(2), split_text.pop(3)

    game = f"{home} vs {away}"

    team = [home, draw, away]

    odds_dict = {}

    # Print the split text
    for i, item in enumerate(split_text[1:]):

        # Extract scores, teams, and odds using regular expressions
        pattern = r'<span class="bbl-BetBuilderParticipant_Name">(.*?)<\/span><span class="bbl-BetBuilderParticipant_Odds">(.*?)<\/span>'
        matches = re.findall(pattern, item)

        # Create a table of teams, scores, and odds
        table = []
        for match in matches:
            score = match[0]
            odds = match[1]
            numer, denom = odds.split('/')
            # Specify the third value here
            decimal_odds = 1 + int(numer) / int(denom)  # Replace 'Some value' with your desired value
            table.append((game, score, odds, decimal_odds))

        # Print the table
        # for row in table:
        #     print(row)

        odds_dict[team[i]] = table


    #print(odds_dict)

    # Find the team with the highest odds
    outcomes = []
    for team, table in odds_dict.items():
        for row in table:
            game, score, odds, decimal_odds = row
            outcome = (game, team, score, odds, decimal_odds)
            outcomes.append(outcome)

    # Sort the outcomes list in ascending order based on the fourth item in each tuple
    outcomes = sorted(outcomes, key=lambda x: x[4])

    # Print all the outcomes
    return outcomes

print(get_outcomes('full.txt')[0])