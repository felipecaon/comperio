import requests
import json
from argparse import ArgumentParser, RawDescriptionHelpFormatter

from requests.exceptions import SSLError

from helpers.colored_text_helper import ColoredTextHelper


def _load_sites():
    sites = open("sites.json", "r")
    return json.load(sites)


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
    sites = _load_sites()
    color = ColoredTextHelper()
    color.start()

    for username in args.username:
        print('Now trying: ', end='')
        print(color.black(text=username))
        print('----------------')
        found_profiles = []
        found_profiles = []
        for data in sites:
            url = data['url']
            identifier = data['identifier']
            formatted_url = url.format(user=username)

            response = None
            try:
                response = requests.get(formatted_url)
            except Exception or SSLError:
                message = f'{identifier}: ERROR'
                print(color.red(text=message))

            if response is not None:
                if response.status_code == 200:
                    found_profiles.append(formatted_url)
                    message = f'{identifier}: FOUND'
                    print(color.green(text=message))
                else:
                    message = f'{identifier}: NOT FOUND'
                    print(color.light_red(text=message))

        print('\nFound profiles:')
        print('----------------')
        for profile in found_profiles:
            print(profile)


if __name__ == "__main__":
    main()
