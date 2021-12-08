from chessdotcom import *
import pprint
import requests
import time
import operator

printer = pprint.PrettyPrinter()
start_time = time.time()


def print_leaderboards():
    data = get_leaderboards().json
    categories = data.keys()

    for category in categories:
        for idx, game_mode in enumerate(data[category]):
            print("\n" + "Game Mode:", game_mode)
            for player in data[category][game_mode]:
                print(
                    f'Rank: {player["rank"]} | Username: {player["username"]} | Rating: {player["score"]}'
                )


def get_player_rating(username):
    data = get_player_stats(username).json
    categories = ["chess_blitz", "chess_rapid", "tactics"]

    for category in categories:
        print("Category:", category)
        if category != "tactics":
            print(f'Current: {data["stats"][category]["last"]["rating"]}')
            print(f'Best: {data["stats"][category]["best"]["rating"]}')
            print(
                f'W/L/D Ratio: {data["stats"][category]["record"]["win"]}W | {data["stats"][category]["record"]["loss"]}L | {data["stats"][category]["record"]["draw"]}D'
            )
        else:
            print(f'Current: {data["stats"][category]["highest"]["rating"]}')


def get_most_recent_game(username):
    data = get_player_game_archives(username).json
    url = data["archives"][-1]
    games = requests.get(url).json()
    game = games["games"][-1]
    printer.pprint(game)


def get_club_admins(url_id):
    data = get_club_details(url_id).json
    admins = data["club"]["admin"]
    print("Admins:")
    for info in admins:
        info = requests.get(info).json()
        username = info["username"]
        print(username)


def get_rapid_rating(username):
    data = get_player_stats(username).json
    if "chess_rapid" in data["stats"]:
        return data["stats"]["chess_rapid"]["last"]["rating"]
    else:
        return 0


def display_club_members(url_id):
    data = get_club_members(url_id).json
    all_members = data["members"]["all_time"]
    member_ranking = {}
    for user in all_members:
        member_ranking[user["username"]] = get_rapid_rating(user["username"])

    ordered = dict(
        sorted(member_ranking.items(), key=operator.itemgetter(1), reverse=True)
    )

    print(ordered)


def club_details(url_id):
    data = get_club_details(url_id).json
    name = data["club"]["name"]
    print(name)
    printer.pprint(data)


def club_matches(url_id):
    data = get_club_matches(url_id).json
    printer.pprint(data)


def club_members(url_id):
    data = get_club_members(url_id).json
    printer.pprint(data)


def country_clubs(iso_id):
    data = get_country_clubs(iso_id).json
    club_name = data["clubs"]
    for idx in range(len(club_name)):
        printer.pprint(club_name[idx].split("/")[-1])


# little information
def country_details(iso_id):
    data = get_country_details(iso_id).json
    printer.pprint(data)


def country_players(iso_id):
    data = get_country_players(iso_id).json
    printer.pprint(data)


"""
get daily puzzle
get player clubs
get player current games
get player current games to move
get player games by month / pgn
get player team matches
get player tournaments
get random daily puzzle
get streamers
get team match
get team match board
get team match live
get team match live board
get titled players
get tournament details
get tournament round
get tournament round group details
is player online
"""


# country_players("ZW")
# country_details("ZW")
# country_clubs("DK")
# club_members("tech-with-tim")
# club_matches("tech-with-tim")
# club_details("tech-with-tim")
# get_most_recent_game("Ar5hv1r")
# print_leaderboards()
# get_player_rating('Ar5hv1r')
# get_club_admins("tech-with-tim")
# display_club_members('tech-with-tim')
print("Time Taken:", time.time() - start_time)
