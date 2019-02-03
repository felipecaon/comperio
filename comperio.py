import requests

username = 'blackocean'
f = open("sites.txt", "r")
found_profiles_file = open("found_profiles.txt", "w+")
found_profiles_file.truncate()


def main():
    for url in f:
        formatted_url = url.format(username)
        if(requests.get(formatted_url).status_code == 200):
            found_profiles_file.write(formatted_url)

    found_profiles_file.seek(0)
    for profile in found_profiles_file:
        print('Found profiles:\n')
        print(profile)


if __name__ == "__main__":
    main()
