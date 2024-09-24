import sqlite3
import random

# Connect to the database
conn = sqlite3.connect('players.db')
c = conn.cursor()

# Create the players table if it doesn't exist
c.execute('''CREATE TABLE IF NOT EXISTS players
             (id INTEGER PRIMARY KEY, name TEXT, position TEXT, team TEXT, points REAL)''')

# Insert some sample player data
players = [
    ("LeBron James", "SF", "Lakers", 27.7),
    ("Giannis Antetokounmpo", "PF", "Bucks", 29.9),
    ("Steph Curry", "PG", "Warriors", 25.5),
    ("Luka Doncic", "PG", "Mavericks", 28.4),
    ("Nikola Jokic", "C", "Nuggets", 26.4)
]
c.executemany("INSERT INTO players (name, position, team, points) VALUES (?, ?, ?, ?)", players)
conn.commit()

# Define the draft function
def draft_players():
    # Get the list of available players from the database
    c.execute("SELECT name, position, team, points FROM players")
    available_players = c.fetchall()

    # Shuffle the list of available players
    random.shuffle(available_players)

    # Initialize the draft order
    draft_order = ["Team 1", "Team 2", "Team 3", "Team 4"]
    round_count = 1

    # Start the draft
    print("Welcome to the Player Draft!")
    while available_players:
        print(f"\nRound {round_count}:")
        for team in draft_order:
            if available_players:
                player = available_players.pop(0)
                print(f"{team} selects {player[0]} ({player[1]} - {player[2]})")
        round_count += 1

    # Close the database connection
    conn.close()

# Run the draft
draft_players()
