from bs4 import BeautifulSoup

import requests
import json
import flask
from jinja2 import Template, Environment, FileSystemLoader

env = Environment(loader=FileSystemLoader('templates'))
template = env.get_template('./home.html')


# score = requests.get("https://cdn.nba.com/static/json/liveData/scoreboard/todaysScoreboard_00.json",                     headers={'Accept': 'application/json'})

# print(score.json())


mock = json.load(open("./mock.json"))


dados = mock
html_renderizado = template.render(games=dados)
