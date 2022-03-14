import pandas as pd


file = 'base.xlsx'

xl = pd.ExcelFile(file)

name_list = xl.sheet_names

file_r = pd.read_excel(xl, name_list)

list_of_singer = []
for i in file_r['list']['singer']:
    list_of_singer.append(i)

list_of_genres = []
for i in file_r['list']['genre']:
    list_of_genres.append(i)












