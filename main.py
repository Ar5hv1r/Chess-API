from chessdotcom import get_leaderboards
import pprint

printer = pprint.PrettyPrinter()

def print_leaderboards():
    data = get_leaderboards().json
    categories = data.keys()

    for category in categories:
        print('Category:', category)
        for idx, entry in enumerate(data[category]):
            print(entry)
    


print_leaderboards()