from django.db import models
from django.db.models.base import ModelBase


# Класс игры
class GameModel(ModelBase):
    bank = 5000  # начальное количество денег
    # Массив карт
    cards = [{"image": "card-clubs-1.png", "value": 11}, {"image": "card-clubs-2.png", "value": 2},
             {"image": "card-clubs-3.png", "value": 3}, {"image": "card-clubs-4.png", "value": 4},
             {"image": "card-clubs-5.png", "value": 5}, {"image": "card-clubs-6.png", "value": 6},
             {"image": "card-clubs-7.png", "value": 7}, {"image": "card-clubs-8.png", "value": 8},
             {"image": "card-clubs-9.png", "value": 9}, {"image": "card-clubs-10.png", "value": 10},
             {"image": "card-clubs-11.png", "value": 10}, {"image": "card-clubs-12.png", "value": 10},
             {"image": "card-clubs-13.png", "value": 10},
             {"image": "card-diamonds-1.png", "value": 11}, {"image": "card-diamonds-2.png", "value": 2},
             {"image": "card-diamonds-3.png", "value": 3}, {"image": "card-diamonds-4.png", "value": 4},
             {"image": "card-diamonds-5.png", "value": 5}, {"image": "card-diamonds-6.png", "value": 6},
             {"image": "card-diamonds-7.png", "value": 7}, {"image": "card-diamonds-8.png", "value": 8},
             {"image": "card-diamonds-9.png", "value": 9}, {"image": "card-diamonds-10.png", "value": 10},
             {"image": "card-diamonds-11.png", "value": 10}, {"image": "card-diamonds-12.png", "value": 10},
             {"image": "card-diamonds-13.png", "value": 10},
             {"image": "card-hearts-1.png", "value": 11}, {"image": "card-hearts-2.png", "value": 2},
             {"image": "card-hearts-3.png", "value": 3}, {"image": "card-hearts-4.png", "value": 4},
             {"image": "card-hearts-5.png", "value": 5}, {"image": "card-hearts-6.png", "value": 6},
             {"image": "card-hearts-7.png", "value": 7}, {"image": "card-hearts-8.png", "value": 8},
             {"image": "card-hearts-9.png", "value": 9}, {"image": "card-hearts-10.png", "value": 10},
             {"image": "card-hearts-11.png", "value": 10}, {"image": "card-hearts-12.png", "value": 10},
             {"image": "card-hearts-13.png", "value": 10},
             {"image": "card-spades-1.png", "value": 11}, {"image": "card-spades-2.png", "value": 2},
             {"image": "card-spades-3.png", "value": 3}, {"image": "card-spades-4.png", "value": 4},
             {"image": "card-spades-5.png", "value": 5}, {"image": "card-spades-6.png", "value": 6},
             {"image": "card-spades-7.png", "value": 7}, {"image": "card-spades-8.png", "value": 8},
             {"image": "card-spades-9.png", "value": 9}, {"image": "card-spades-10.png", "value": 10},
             {"image": "card-spades-11.png", "value": 10}, {"image": "card-spades-12.png", "value": 10},
             {"image": "card-spades-13.png", "value": 10}
             ]
    firstRun = True  # первый ход партии
    dealer_cards = []  # карты дилера
    player_cards = []  # карты игрока
    dealer_sum = None  # сумма очков дилера
    player_sum = None  # сумма очков игрока
    loser = False  # игрок проиграл
    winner = False  # игрок выиграл
    draw = False  # ничья
    end = False  # конец партии
    dealerTurn = False  # ход дилера
    cur_bid = 0  # текущая ставка


