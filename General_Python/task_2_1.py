
"""
2.1 The questions in this section should be attempted using only core python, i.e. no
additional packages should be imported. If you cannot answer the questions without
additional packages, then do import them, but this will affect the mark given.

2.1 You work on the Gameloft database, and you want to store game information in python
objects. Write a python class to act as a store for those objects, which will store
the following game parameters: Game_name, Game_genre, Year_of_release. The class
should also be able to return:
● The number of games,
● The list of games,
● A list of games that have their game_name starting with the letter given by the user.
"""


class GameStore:
    """
    A class to act as a store for game objects.

    Attributes:
        games (list): List to store game objects.

    Methods:
        add_game(game_name, game_genre, year_of_release):
            Adds a game to the store.

        get_number_of_games():
            Returns the number of games in the store.

        get_list_of_games():
            Returns a list of game names in the store.

        get_games_starting_with(letter):
            Returns a list of games that have their game_name starting with the given letter.
    """

    def __init__(self):
        """
        Initializes a GameStore object with an empty list of games.
        """
        self.games = []

    def add_game(self, game_name, game_genre, year_of_release):
        """
        Adds a game to the store.

        Args:
            game_name (str): Name of the game.
            game_genre (str): Genre of the game.
            year_of_release (int): Year of release of the game.
        """
        self.games.append({
            'Game_name': game_name,
            'Game_genre': game_genre,
            'Year_of_release': year_of_release
        })

    def get_number_of_games(self):
        """
        Returns the number of games in the store.

        Returns:
            int: Number of games in the store.
        """
        return len(self.games)

    def get_list_of_games(self):
        """
        Returns a list of game names in the store.

        Returns:
            list: List of game names.
        """
        return [game['Game_name'] for game in self.games]

    def get_games_starting_with(self, letter):
        """
        Returns a list of games that have their game_name starting with the given letter.

        Args:
            letter (str): Starting letter of game names to filter.

        Returns:
            list: List of games obj matching the starting letter.
        """
        return [game for game in self.games if game['Game_name'].startswith(letter)]


# Create a GameStore object
store = GameStore()

# Add some games to the store
store.add_game("Asphalt 9: Legends", "Racing", 2018)
store.add_game("Modern Combat 5", "First-person shooter", 2014)
store.add_game("Gangstar Vegas", "Action", 2013)
store.add_game("Order & Chaos Online", "MMORPG", 2011)

# Test the methods of the GameStore class
print(store.get_number_of_games())  # Output: 4

games = store.get_list_of_games()
print(games)  # Output: ['Asphalt 9: Legends', 'Modern Combat 5', 'Gangstar Vegas', 'Order & Chaos Online']

letter = 'A'
games_starting_with_A = store.get_games_starting_with(letter)
print(games_starting_with_A)
# Output: [{'Game_name': 'Asphalt 9: Legends', 'Game_genre': 'Racing', 'Year_of_release': 2018},
#           {'Game_name': 'Order & Chaos Online', 'Game_genre': 'MMORPG', 'Year_of_release': 2011}]

letter = 'G'
games_starting_with_G = store.get_games_starting_with(letter)
print(games_starting_with_G)
# Output: [{'Game_name': 'Gangstar Vegas', 'Game_genre': 'Action', 'Year_of_release': 2013}]

letter = 'M'
games_starting_with_M = store.get_games_starting_with(letter)
print(games_starting_with_M)
# Output: [{'Game_name': 'Modern Combat 5', 'Game_genre': 'First-person shooter', 'Year_of_release': 2014}]
