from flask import Flask, session, jsonify, render_template, request, redirect
import requests
import datetime
import json


app = Flask(__name__)


@app.route('/')
def hello():
    data = json.load(open('./mock.json'))
    print(f"▷ last update: {data['meta']['time']}")
    return render_template('index.html', data=data)


@app.route('/game-select')
def game_select():
    data = json.load(open('./mock.json'))
    return render_template('game-select.html', utc_dt=datetime.datetime.now(), data=data)


@app.route('/track')
def track():
    data = json.load(open('./mock.json'))
    gameSelectedId = request.args.get('game-select')
    # headers = {'Accept': 'application/json'}
    # r = requests.get(f'https://cdn.nba.com/static/json/liveData/boxscore/boxscore_{gameSelectedId}.json', headers=headers)
    # data2 = r.json()
    data2 = json.load(open('./mock2.json'))
    return render_template('track.html', gameSelectedId=gameSelectedId, data=data, data2=data2)


@app.route("/monitoring", methods=["GET", "POST"])
def monitoring():
    data = {
        "Vencedor": request.args['vencedor'],

        "Time-handicap": {
            "time": request.args['handicap-team'],
            "Handicap": request.args['handicap'],
        },

        "Pontos totais": request.args['total-points'],

        "Jogador - cestas de 3": {
            "jogador": request.args['player-three-points'],
            "Cestas de 3": request.args['points-three-points'],
        },

        "Jogador - Rebotes": request.args['player-rebounds'],
        "Número de rebotes": request.args['number-rebounds'],

        "Assistências": {
            "jogador": request.args['player-assists'],
            "assistencias": request.args['qtd-player-assists'],
        },

        "Pontos + Assists": {
            "jogador": request.args['player-points-assists'],
            "Pontos-Assists": request.args['points-assists'],
        },

        "Pontos + Rebotes": {
            "jogador": request.args['player-points-rebounds'],
            "Pontos-Rebotes": request.args['points-rebounds'],
        },

        "Pontos + Assists + Rebotes": {
            "jogador": request.args['player-points-assists-rebounds'],
            " pontos + assists + rebotes": request.args['points-assists-rebounds'],
        },

        "Bloqueios": {
            "jogador": request.args['player-blocks'],
            "bloqueios": request.args['number-blocks'],
        },

        "Roubadas": {
            "jogador": request.args['player-steals'],
            "steals": request.args['ball-steals'],
        },

        "Jogador - Duplo duplo": request.args['double-double-player'],
        "Jogador - Triplo duplo": request.args['triple-double-player'],

        "Ganhador Período": {
            "time": request.args['winner-period'],
            "periodo": request.args['winner-period-period'],
        },

        "Pontos totais - Par/Ímpar": request.args['total-points-even-odd'],
        "Jogo para prorrogação": request.args['jogo-prorrogacao'],

        "Time - pontos individuais": {
            "time": request.args['team-individual-points'],
            "pontos": request.args['number-points'],
        },

        "Time ganhador - diferença de pontos": {
            "time": request.args['winner-difference'],
            "difference": request.args['number-points-difference'],
        },

        "even-odd-points": {
            "time": request.args['team-points-even-odd'],
            "even-odd": request.args['even-odd-team-points'],
        },
    }

    return render_template('monitoring.html', data=data)


@ app.route('/process_form', methods=['POST'])
def process_form():
    gameSelectedId = request.form.get('gameSelectedId')
    return jsonify(gameSelectedId), 200
