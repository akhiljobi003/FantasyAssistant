import sqlite3

'''
TODO: 
Connect to database and fetch
Snake order?
'''

# Connect to the database
# conn = sqlite3.connect('players.db')
# c = conn.cursor()

# Define the draft function
def draft_players():
    '''
    This function will simulate the drafting of players
    It will connect to a database
    Fetch a list of players from the database (available_players)
    Then it will start the draft
        The system will prompt the user to enter a player's name, if needed it can print the players available
        If the user chooses a player, and it is a valid input, it will add it to an array of the specific user's team, and go to the next user
        Repeat for X number of rounds
    '''
    # Get the list of available players from the database
    # c.execute("SELECT name, position, team, points FROM players")
    # available_players = c.fetchall()

    # Add some test players
    available_players = ["1","2",'3','4','5','6','7','8','9','10','11','12','13','14','15','16','17','18','19','20','21','22','23','24', '25']

    player_num = 0
    # Initialize the draft order
    round_count = 0
    while True:
        input_var = input("How many players would you like to play with?")
        if input_var == 'exit':
            return
        if (input_var.isdigit()):
            player_num = int(input_var)
            break
        else:
            print("An error occurred.")


    # Create a matrix of teams, 6 is arbitrary
    teamlist = [[0 for x in range(6)] for y in range(player_num)]

    # Start the draft
    print("Welcome to the Player Draft!")
    while available_players and round_count < 6:
        print(f"\nRound {round_count + 1}:")
        for team in range(player_num):
            if available_players:
                desired = ''

                # Loop to make it so that we get a response that qwe understand
                while True:
                    print(f"Team {team+1}, What player would you like to select?")
                    desired = input()
                    if desired == "exit":
                        return
                    if desired in available_players:
                        break
                    else:
                        print("Error, player not available or something went wrong, choose again.")
                
                # Update the players, remove them from the available list, update the rosters
                player = desired
                available_players.remove(desired)
                print(f"Team {team+1} selects {player}.")
                teamlist[team][round_count] = player
        round_count += 1

    print("Here are the teams")
    team_num = 1
    for team in teamlist:
        print(f"Team {team_num}:")
        team_num += 1
        for player in team:
            print(player)
    # Close the database connection
    # conn.close()

draft_players()