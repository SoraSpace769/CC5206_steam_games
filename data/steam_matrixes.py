import pandas as pd

'''
For data gathered in a single string separated by ';'.
Each resulting csv file has 'appid' first to join with the main file,
and the possible attributes in different columns.

If a game (rows) is classified as certain genre/category or was released
in a platform (columns), the element's value is 1, 0 otherwise.
'''

# Reading main file to get data
df = pd.read_csv("steam.csv")

# Genres matrix
genres = df['genres'].str.get_dummies(sep=';')
genres.insert(0, 'appid', df['appid'])
genres.to_csv(r'steam_genres.csv', index=False, header=True)
print(genres.sum(), '\n')

# Categories matrix
categ = df['categories'].str.get_dummies(sep=';')
categ.insert(0, 'appid', df['appid'])
categ.to_csv(r'steam_categories.csv', index=False, header=True)
print(categ.sum(), '\n')

# Platforms matrix
plat = df['platforms'].str.get_dummies(sep=';')
plat.insert(0, 'appid', df['appid'])
plat.to_csv(r'steam_platforms.csv', index=False, header=True)
print(plat.sum())

