from flask import Flask, request
import requests
import json
from summoner import Summoner

app = Flask(__name__)


@app.route('/')
def hello_world():
    server = request.args.get("server")
    name = request.args.get("name")
    if not server or not name:
        return "No user found"
    summoner = get_summoner(server, name)
    g = get_matches(summoner.puuid, "europe")
    return "".join(g)


def get_summoner(server: str, name: str) -> Summoner:
    req_url = f"https://{server}.api.riotgames.com/lol/summoner/v4/summoners/by-name/{name}"
    return Summoner(*get_from_api(req_url).values())


# server = europe
def get_matches(puuid: str, server: str):
    match_list = []
    counter = 0
    while True:
        response = get_some_matches(puuid, server, counter, 100)
        match_list += response
        if len(response) < 100:
            break
        counter += 100
    return match_list


def get_some_matches(puuid: str, server: str, start: int, count: int):
    url = f"https://{server}.api.riotgames.com/lol/match/v5/matches/by-puuid/{puuid}/ids?start={start}&count={count}"
    return get_from_api(url)


def get_from_api(url: str):
    header = {"X-Riot-Token": get_key()}
    response = requests.get(url, headers=header)
    return json.loads(response.text)


def get_key() -> str:
    with open("api_key.txt") as file:
        return file.readline()


if __name__ == '__main__':
    app.run()
