# Football Match Outcome Prediction using Python

## Overview
This project provides Python scripts for parsing football match statistics from HTML files, analyzing probabilities, and suggesting potential bets based on calculated probabilities. It utilizes data parsing, data manipulation, and visualization techniques to provide insights into football match outcomes.

## Contents
1. **parse_football_stats.py:** This script defines a function to parse football match statistics from HTML files.
2. **top_n_outcomes_from_folder.py:** This script implements a function to retrieve the top outcomes from HTML files in a specified directory.
3. **analysis.ipynb:** This notebook parses and gridsearches the matches to find the combination of scores with the highest likihood.

## Usage
1. Clone the repository to your local machine.
2. Ensure you have Python installed along with necessary libraries (pandas, BeautifulSoup).
3. Place HTML files containing football match statistics in the Matches folder.
4. Use `parse_football_stats.py` to parse individual HTML files.
5. Use `top_n_outcomes_from_folder.py` to retrieve top outcomes from multiple HTML files in a directory.
6. Run `analysis.ipynb` to perform a grid search for top-performing combinations and visulisations.

## Dependencies
- Python 3.x
- pandas
- BeautifulSoup

## Contributing
Contributions are welcome! Feel free to submit bug reports, feature requests, or pull requests via GitHub.

## License
This project is licensed under the MIT License.

## Authors
Adam Fowlie, Jamie Milsom
