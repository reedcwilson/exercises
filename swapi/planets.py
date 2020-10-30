import requests
import json


def count_films(planets):
    return [(sum(1 for f in p['films']), p['name']) for p in planets]


def get_planets(planets, url):
    if url is None:
        return planets
    r = requests.get(url).json()
    planets.extend(r['results'])
    return get_planets(planets, r['next'])


def main():
    planets = get_planets([], 'https://swapi.co/api/planets/')
    return count_films(planets)


if __name__ == '__main__':
    print(json.dumps(sorted(main(), reverse=True)[0][1]))
