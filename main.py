from chessdotcom import get_leaderboards, get_player_stats
import pprint

printer = pprint.PrettyPrinter()

def print_leaderboards():
    data = get_leaderboards().json
    categories = data.keys()


    for category in categories:
        for idx, game_mode in enumerate(data[category]):
            print("\n" + "Game Mode:", game_mode) 
            for player in data[category][game_mode]:
                print(f'Rank: {player["rank"]} | Username: {player["username"]} | Rating: {player["score"]}')

def get_player_rating(username):
    data = get_player_stats(username).json
    printer.pprint(data)
    categories = ['chess_blitz', 'chess_rapid', 'tactics']

    for category in categories:
        print('Category:', category)
        if category != 'tactics':
            print(f'Current: {data["stats"][category]["last"]["rating"]}')
            print(f'Best: {data["stats"][category]["best"]["rating"]}')
            print(f'W/L/D Ratio: {data["stats"][category]["record"]["win"]}W | {data["stats"][category]["record"]["loss"]}L | {data["stats"][category]["record"]["draw"]}D')  
        else:
            print(f'Current: {data["stats"][category]["highest"]["rating"]}')

print_leaderboards()
get_player_rating('Ar5hv1r')

