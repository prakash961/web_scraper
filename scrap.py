import requests
from bs4 import BeautifulSoup as bs
import pandas as pd
import numpy as np

def scrape_players(url):
    src = requests.get(url)
    soup = bs(src.text, 'html.parser')

    player_total = soup.find('div', class_='cb-col cb-col-100 cb-padding-left0')
    player_1 = player_total.find_all('div', class_='cb-col cb-col-100 cb-font-14 cb-lst-itm text-center')

    players = []
    for i in player_1:
        player_rank = i.find('div', class_='cb-col cb-col-16 cb-rank-tbl cb-font-16').text
        player_title = i.find('div', class_='cb-col cb-col-67 cb-rank-plyr').a.text
        player_country = i.find('div', class_='cb-font-12 text-gray').text
        player_rating = i.find('div', class_='cb-col cb-col-17 cb-rank-tbl pull-right').text

        player_info = {
            'Rank': player_rank,
            'Name': player_title,
            'Country': player_country,
            'Rating': player_rating
        }
        players.append(player_info)

    return players

'''
def upsert_logic(combined_df):
    up=[]
    for i in f:
        roww=df[df['name']==i['name']]
        if roww.empty:
            up.append(i)
        else:
            if (df['rank'].values[0] != i['rank'] or df['rating'].values[0] != i['rating']):
                up.append(i)'''

batting_url = 'https://www.cricbuzz.com/cricket-stats/icc-rankings/men/batting'
bowling_url = 'https://www.cricbuzz.com/cricket-stats/icc-rankings/men/bowling'
all_rounder_url = 'https://www.cricbuzz.com/cricket-stats/icc-rankings/men/all-rounder'

batting_players = scrape_players(batting_url)
bowling_players = scrape_players(bowling_url)
all_rounder_players = scrape_players(all_rounder_url)

df = pd.DataFrame(batting_players)
df1 = pd.DataFrame(bowling_players)
df2 = pd.DataFrame(all_rounder_players)

df_tot=[df,df1,df2]
for i in df_tot:
  i['Rank'] = i['Rank'].astype(int)
  i['Rating'] = i['Rating'].astype(float)
  i['Name']= i['Name'].astype(str)
  i['Country']=i['Country'].astype(str)

print(round(np.array(df['Rating']).mean(),2))
print(round(np.array(df1['Rating']).mean(),2))
print(round(np.array(df2['Rating']).mean(),2))

combined_df= pd.concat([df,df1,df2],ignore_index=True)
combined_df.to_csv('cricbuzz.csv',index=False)
