from chessdotcom import get_leaderboards
import pprint

printer = pprint.PrettyPrinter()

def print_leaderboards():
    data = get_leaderboards().json
    categories = data.keys()

    for category in categories:
        print('Category:', data[category].keys())

print_leaderboards()

