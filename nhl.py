# Python code for programming class

import pandas as pd

excelFile = pd.ExcelFile('/Users/douglasquinn/Desktop/nhl_skaterstats.xlsx')
players = pd.read_excel(excelFile, 'players')
stats = pd.read_excel(excelFile, 'stats')
teams = pd.read_excel(excelFile, 'teams')
positions = pd.read_excel(excelFile, 'positions')
print('Excel sheets imported')

players.info()