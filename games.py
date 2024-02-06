from Scrapper import get_outcomes

import os

directory = r'C:\Users\adamf\PycharmProjects\Visual Studio\Bet365_scrapper\Matches 060224'
best = []
second_best = []


for filename in os.listdir(directory):
    if filename.endswith(".txt"):
        outcomes = get_outcomes(directory + '/' + filename)
        best.append(outcomes[0])
        second_best.append(outcomes[1])
        continue
    else:
        continue

for i in range(len(best)):
    print(best[i])