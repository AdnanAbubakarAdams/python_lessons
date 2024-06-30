import sys
import pandas as pd
top_scorers_of_alltime = pd.read_html('https://en.wikipedia.org/wiki/List_of_footballers_with_500_or_more_goals#:~:text=With%20over%20890%20goals%20at%20club%20and,as%20the%20top%20goalscorer%20of%20all%20time.')

print(sys.path)
print(len(top_scorers_of_alltime))
