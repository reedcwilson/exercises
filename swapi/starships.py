import requests
import json


def get_starship_names(starships):
    return [s['name'] for s in starships]


def get_starships(starships, url):
    if url is None:
        return starships
    r = requests.get(url).json()
    starships.extend(r['results'])
    return get_starships(starships, r['next'])


def main():
    starships = get_starships([], 'https://swapi.co/api/starships/')
    return get_starship_names(starships)


if __name__ == '__main__':
    print(json.dumps(sorted(main())))
