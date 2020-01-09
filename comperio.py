import requests
import json
from argparse import ArgumentParser, RawDescriptionHelpFormatter

from helpers.colored_text_helper import ColoredTextHelper

sites = open("sites.json", "r")
sites_data = json.load(sites)
found_profiles_file = open("found_profiles.txt", "w+")
found_profiles_file.truncate()
color = ColoredTextHelper()
color.start()


def _get_arguments():
    parser = ArgumentParser(formatter_class=RawDescriptionHelpFormatter)

    parser.add_argument(
        "username",
        nargs='+',
        metavar='USERNAMES',
        action="store",
        help="One or more usernames"
    )

    return parser.parse_args()


def main():

    args = _get_arguments()

    for username in args.username:
        print('Now trying: ' + username)
        print('----------------')
        found_profiles = []
        for data in sites_data:
            url = data['url']
            identifier = data['identifier']
            formatted_url = url.format(user=username)

            response = None
            try:
                response = requests.get(formatted_url)
            except Exception:
                message = f'{identifier}: ERROR'
                print(color.red(text=message))

            if response.status_code == 200:
                found_profiles.append(formatted_url)
                message = f'{identifier}: FOUND'
                print(color.green(text=message))
            else:
                message = f'{identifier}: NOT FOUND'
                print(color.not_found(text=message))

        print('\nFound profiles:')
        print('----------------')
        for profile in found_profiles:
            print(profile)


if __name__ == "__main__":
    main()
