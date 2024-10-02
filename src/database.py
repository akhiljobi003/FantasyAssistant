import sqlite3
import requests
from bs4 import BeautifulSoup
import pandas as pd

def fetch_nba_data():
    """
    Fetch NBA player data from Basketball Reference.
    """
    url = 'https://www.basketball-reference.com/leagues/NBA_2024_totals.html'
    
    try:
        response = requests.get(url, timeout=10)
        response.raise_for_status()
        
        soup = BeautifulSoup(response.content, 'html.parser')
        table = soup.find('table', {'id': 'totals_stats'})
        
        if table:
            df = pd.read_html(str(table))[0]
            df = df.dropna(subset=['Player', 'Tm'])  # Remove rows with NaN values in Player or Tm
            
            # Handle players who played for multiple teams
            df = df.groupby('Player').last().reset_index()
            
            # Rename columns for consistency with previous code
            df = df.rename(columns={
                'Player': 'name',
                'Tm': 'team',
                'G': 'games_played',
                'PTS': 'points',
                'TRB': 'rebounds',
                'AST': 'assists',
                'STL': 'steals',
                'BLK': 'blocks',
                'FG%': 'fg_pct',
                'FT%': 'ft_pct',
                '3P': 'threes_made'
            })
            
            # Calculate per-game averages
            for stat in ['points', 'rebounds', 'assists', 'steals', 'blocks', 'threes_made']:
                df[f'{stat}_per_game'] = df[stat] / df['games_played']
            
            return df
        else:
            print("Table not found on the webpage.")
            return pd.DataFrame()
        
    except requests.RequestException as e:
        print(f"Error fetching data from {url}: {str(e)}")
        return pd.DataFrame()
    except Exception as e:
        print(f"An unexpected error occurred: {str(e)}")
        return pd.DataFrame()

def setup_database():
    conn = sqlite3.connect('nba_players.db')
    df = fetch_nba_data()
    if not df.empty:
        df.to_sql('players', conn, if_exists='replace', index=False)
        print(f"Database updated with {len(df)} players.")
    else:
        print("Failed to update database due to empty dataset.")
    conn.close()

def get_player_data():
    conn = sqlite3.connect('nba_players.db')
    df = pd.read_sql_query("SELECT * FROM players", conn)
    conn.close()
    return df.to_dict('records')

if __name__ == "__main__":
    setup_database()
