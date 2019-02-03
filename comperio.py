import requests
from argparse import ArgumentParser, RawDescriptionHelpFormatter

f = open("sites.txt", "r")
found_profiles_file = open("found_profiles.txt", "w+")
found_profiles_file.truncate()


def main():

    parser = ArgumentParser(formatter_class=RawDescriptionHelpFormatter)

    parser.add_argument("username",
                        nargs='+', metavar='USERNAMES',
                        action="store",
                        help="One or more usernames"
                        )

    args = parser.parse_args()

    for username in args.username:
        print('Now trying: ' + username)
        for url in f:
            formatted_url = url.format(username)
            if(requests.get(formatted_url).status_code == 200):
                found_profiles_file.write(formatted_url)

        found_profiles_file.seek(0)
        print('Found profiles:\n')
        for profile in found_profiles_file:
            print(profile)


if __name__ == "__main__":
    main()
