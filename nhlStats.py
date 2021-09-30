import pandas as pd

#Import data
excelFile = pd.ExcelFile('/Users/douglasquinn/Desktop/nhl_skaterstats.xlsx')
players = pd.read_excel(excelFile, 'players')
stats = pd.read_excel(excelFile, 'stats')
teams = pd.read_excel(excelFile, 'teams')
positions = pd.read_excel(excelFile, 'positions')
print('Excel sheets imported')

players.info()

defence = players.loc[players['POS'] == 'D']
print(defence)

print(players['POS'].describe())

print(stats.head())

print(players['POS'].value_counts())

print(players['POS'].value_counts(normalize=True))

stats2 = pd.merge(stats, teams, how="left", left_on="Tm", right_on="FRANCHISE").drop_duplicates()
print(stats2.head())

stats2['Team Name'] = stats2['NAME']
stats2.drop(['NAME', 'Tm', 'TEAM LIST'], axis=1, inplace=True)
print(stats2.head())

topPlayers = stats.loc[(stats['GP'] > 60) & (stats['PTS'] > 65) & (stats['+/-'] < -5) & (stats['Season'] == 2018)]
print(topPlayers)

topGoals = stats.loc[stats['Season'] == 2018].nlargest(10, ['G'])
print(topGoals)

topAssists = stats.loc[stats['Season'] == 2018].nlargest(10, ['A'])
print(topGoals)
