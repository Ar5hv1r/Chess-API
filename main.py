from chessdotcom import get_leaderboards
import pprint

printer = pprint.PrettyPrinter()

def print_leaderboards():
    data = get_leaderboards().json
    categories = data.keys()


    for category in categories:
        for idx, game_mode in enumerate(data[category]):
            print("Game Mode:", game_mode) 
            for player in data[category][game_mode]:
                print(f'Rank: {player["rank"]} | Username: {player["username"]} | Rating: {player["score"]}')

print_leaderboards()

