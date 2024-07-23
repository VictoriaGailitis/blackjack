import random

from game.models import GameModel
from django.shortcuts import render, redirect


def index(request):  # основная страница
    message = ""  # системное сообщение
    if request.method == "POST" and GameModel.firstRun:  # если сделана ставка и первый ход в партии
        GameModel.cur_bid = int(request.POST.get("bid"))  # чтение ставки из ПОСТ-запроса
        # если ставка больше остатка в банке или равна нулю
        if GameModel.cur_bid > GameModel.bank or GameModel.cur_bid == 0:
            message = "Ставка не должна быть больше банка или равна нулю!"
        else:
            GameModel.bank -= GameModel.cur_bid  # вычитание поставленной суммы из банка
            # инициализация необходимых переменных класса (на случай не первого запуска сервера)
            GameModel.dealer_sum = 0
            GameModel.player_sum = 0
            GameModel.dealer_cards = []
            GameModel.player_cards = []
            GameModel.loser = False
            GameModel.winner = False
            GameModel.draw = False
            GameModel.dealerTurn = False
            #  добавление одной случайной карты для дилера и игрока из колоды (карта из колоды удаляется)
            GameModel.dealer_cards.append(GameModel.cards.pop(random.randrange(len(GameModel.cards))))
            GameModel.player_cards.append(GameModel.cards.pop(random.randrange(len(GameModel.cards))))
            GameModel.player_cards.append(GameModel.cards.pop(random.randrange(len(GameModel.cards))))
            #  добавление величин карт к сумме очков дилера и игрока
            for card in GameModel.dealer_cards:
                GameModel.dealer_sum += card['value']
            for card in GameModel.player_cards:
                GameModel.player_sum += card['value']
            GameModel.firstRun = False  # переключение флага (закончен первый ход партии)
    # системные сообщеия на все три исхода игры
    if GameModel.loser:
        message = "Вы проиграли!"
    if GameModel.winner:
        message = "Вы выиграли!"
    if GameModel.draw:
        message = "Ничья"
    #  если партия окончена
    if GameModel.end:
        #  возвращение всех карт в колоду
        GameModel.cards = [{"image": "card-clubs-1.png", "value": 11}, {"image": "card-clubs-2.png", "value": 2},
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
                           {"image": "card-diamonds-11.png", "value": 10},
                           {"image": "card-diamonds-12.png", "value": 10},
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
        GameModel.firstRun = True  # переключение флага (первый ход новой партии)
        GameModel.cur_bid = 0  # обунление текущей ставки
        GameModel.end = False  # переключение флага (начало новой партии)
    # рендер страницы с передачей всех необходимых параметров в шаблон
    return render(request, 'index.html', {'bank': GameModel.bank,
                                          'dealer_cards': GameModel.dealer_cards,
                                          'player_cards': GameModel.player_cards,
                                          'dealer_sum': GameModel.dealer_sum, 'player_sum': GameModel.player_sum,
                                          'message': message, 'bid': GameModel.cur_bid,
                                          'first_run': GameModel.firstRun, 'loser': GameModel.loser,
                                          'winner': GameModel.winner, 'draw': GameModel.draw,
                                          'dealer_turn': GameModel.dealerTurn})


def hit(request):  # взять еще одну карту
    GameModel.firstRun = False  # начало новой партии окончено
    curr_card = GameModel.cards.pop(random.randrange(len(GameModel.cards)))  # получние случайной карты из колоды
    if curr_card['value'] == 11 and GameModel.player_sum + 11 > 21:  # если полученная карта - туз и с ней будет перебор
        curr_card['value'] = 1  # замена ценности карты с 11 на 1
    GameModel.player_cards.append(curr_card)  # перенос карты в руку игрока
    GameModel.player_sum += curr_card['value']  # добавление ценности карты в сумму очков игрока
    if GameModel.player_sum > 21:  # если сумма очков больше 21
        GameModel.loser = True  # флаг проигрыша
        GameModel.end = True  # флаг конца игры
    return redirect('index')  # переадресация на главную страницу


def stand(request):  # передать ход дилеру
    GameModel.dealerTurn = True  # флаг передачи хода дилеру
    curr_card = GameModel.cards.pop(random.randrange(len(GameModel.cards)))  # получение случайной карты из колоды
    GameModel.dealer_cards.append(curr_card)  # добавление карты в руку к дилеру
    GameModel.dealer_sum += curr_card['value']  # добавление ценности карты в сумму очков дилера
    while GameModel.dealer_sum <= 16:  # пока сумма очков дилера меньше или равна 16
        curr_card = GameModel.cards.pop(random.randrange(len(GameModel.cards)))  # получение случайной карты из колоды
        # если полученная карта - туз и с ней будет перебор
        if curr_card['value'] == 11 and GameModel.dealer_sum + 11 > 21:
            curr_card['value'] = 1  # смена ценности карты с 11 на 1
        GameModel.dealer_cards.append(curr_card)  # добавление полученной карты в руку дилера
        GameModel.dealer_sum += curr_card['value']  # добавление ценности карты в сумму очков дилера
    # если количество очков дилера больше очков игрока и меньше или равно 21
    if GameModel.player_sum < GameModel.dealer_sum <= 21:
        GameModel.loser = True  # флаг проигрыша игрока
    # если количество очков дилера меньше количества очков игрока или у дилера больше 21 очка
    elif GameModel.dealer_sum < GameModel.player_sum or GameModel.dealer_sum > 21:
        GameModel.bank += GameModel.cur_bid * 2  # добавление игроку в банк ставки и выигрыша
        GameModel.winner = True  # флаг выигрыша игрока
    else:  # если ничья
        GameModel.bank += GameModel.cur_bid  # возвращаем ставку игроку
        GameModel.draw = True  # флаг ничьи
    GameModel.end = True  # флаг конца партии
    return redirect('index')  # переадресация на главную страницу


def double(request):  # удвоение ставки
    GameModel.cur_bid *= 2  # удвоение текущей ставки
    GameModel.bank -= round(GameModel.cur_bid / 2)  # вычет из банка игрока еще одной ставки (до удвоения)
    curr_card = GameModel.cards.pop(random.randrange(len(GameModel.cards)))  # получение одной случайной карты из колоды
    # если полученная карта - туз и вместе с ней будет перебор
    if curr_card['value'] == 11 and GameModel.player_sum + 11 > 21:
        curr_card['value'] = 1  # смена достоинства карты с 11 на 1
    GameModel.player_cards.append(curr_card)  # добавление карты в руку игрока
    GameModel.player_sum += curr_card['value']  # добавление достоинства карты в сумму очков игрока
    if GameModel.player_sum > 21:  # если сумма очков игрока больше 21
        GameModel.loser = True  # флаг проигрыша игрока
        GameModel.end = True  # флаг конца игры
        return redirect('index')  # переадресация на главную страницу
    return redirect('stand')  # передача хода дилеру


def surrender(request):  # сдача карт и проигрыш половины ставки
    GameModel.bank += round(GameModel.cur_bid / 2)  # возврат половины ставки в банк игрока
    GameModel.loser = True  # флаг проигрыша игрока
    GameModel.end = True  # флаг конца игры
    return redirect('index')  # переадресация на главную страницу


def restart(request):  # обновить банк
    GameModel.bank = 5000  # восстановление начальной величины банка
    return redirect('index')  # переадресация на главную страницу
