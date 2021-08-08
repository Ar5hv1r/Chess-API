from chessdotcom import get_leaderboards, get_player_stats, get_player_game_archives, get_club_details, get_club_members
import pprint
import requests

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
    categories = ['chess_blitz', 'chess_rapid', 'tactics']

    for category in categories:
        print('Category:', category)
        if category != 'tactics':
            print(f'Current: {data["stats"][category]["last"]["rating"]}')
            print(f'Best: {data["stats"][category]["best"]["rating"]}')
            print(f'W/L/D Ratio: {data["stats"][category]["record"]["win"]}W | {data["stats"][category]["record"]["loss"]}L | {data["stats"][category]["record"]["draw"]}D')  
        else:
            print(f'Current: {data["stats"][category]["highest"]["rating"]}')

def get_most_recent_game(username):
    data = get_player_game_archives(username).json
    url = data['archives'][-1]
    games = requests.get(url).json()
    game = games['games'][-1]
    printer.pprint(game)

def get_club_admins(url_id):
    data = get_club_details(url_id).json
    admins = data['club']['admin']
    print('Admins:')
    for info in admins:
        info = requests.get(info).json()
        username = info['username']
        print(username)

def get_rapid_rating(username):
    data = get_player_stats(username).json
    if 'chess_rapid' in data['stats']:
        return data["stats"]["chess_rapid"]["last"]["rating"]
    else:
        pass


def display_club_members(url_id):
    data = get_club_members(url_id).json
    all_members = data['members']['all_time']
    for user in all_members:
        print('Username:', user["username"], 'Rating:', get_rapid_rating(user["username"]))
    


#get_most_recent_game('Ar5hv1r')
#print_leaderboards()
#get_player_rating('Ar5hv1r')
#get_club_admins("tech-with-tim")
display_club_members('tech-with-tim')