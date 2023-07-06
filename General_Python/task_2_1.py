
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


class Game:
    """
    A class to represent a game.

    Attributes:
        name (str): Name of the game.
        genre (str): Genre of the game.
        year (int): Year of release of the game.
    """

    def __init__(self, name: str, genre: str, year: int):
        """
        Initializes a Game object with the specified attributes.

        Args:
            name (str): Name of the game.
            genre (str): Genre of the game.
            year (int): Year of release of the game.
        """
        self.name = name
        self.genre = genre
        self.year = year


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

    def add_game(self, game_name: str, game_genre: str, year_of_release: int):
        """
        Adds a game to the store.

        Args:
            game_name (str): Name of the game.
            game_genre (str): Genre of the game.
            year_of_release (int): Year of release of the game.
        """
        game = Game(game_name, game_genre, year_of_release)
        self.games.append(game)

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
        return list(map(lambda x: x.name, self.games))

    def get_games_starting_with(self, letter: str):
        """
        Returns a list of games that have their game_name starting with the given letter.

        Args:
            letter (str): Starting letter of game names to filter.

        Returns:
            list: List of games obj matching the starting letter.
        """
        return [game.name for game in self.games if game.name.startswith(letter)]


if __name__ == '__main__':
    store = GameStore()

    # Adding games to the store
    store.add_game("Asphalt 9: Legends", "Racing", 2018)
    store.add_game("Modern Combat 5", "First-person shooter", 2014)
    store.add_game("Gangstar Vegas", "Action", 2013)
    store.add_game("Order & Chaos Online", "MMORPG", 2011)

    # Getting the number of games
    num_of_games = store.get_number_of_games()
    print("Number of games:", num_of_games)

    # Getting the list of games
    game_list = store.get_list_of_games()
    print("List of games:", game_list)

    # Getting games starting with a specific letter
    starting_letters = ["A", "M", "O"]
    for starting_letter in starting_letters:
        games_starting_with_letter = store.get_games_starting_with(starting_letter)
        print(f"Games starting with letter '{starting_letter}':", games_starting_with_letter)
