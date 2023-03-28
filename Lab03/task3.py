def cw3v2():
    import random
    import getpass

    rounds = int(input("Podaj liczbę rund: "))
    players_count = int(input("Wybierz tryb gry: (1) komputer, (2) dwóch graczy\n"))
    while players_count not in [1, 2]:
        players_count = int(input("Nieprawidłowy wybór, spróbuj ponownie: "))
    player1_name = input("Podaj imię gracza 1: ")
    player2_name = input("Podaj imię gracza 2: ") if players_count == 2 else "Komputer"

    player1_move = 1;
    player2_move = 1;

    scores = {player1_name: 0, player2_name: 0}
    actions = ["papier", "nożyce", "kamień"]

    def choose_action(player_name):
        if player2_name == "Komputer":
            player2_move = random.choice(actions)
            return player2_move
        else:
            print(f"{player1_name}, wybierz ruch: (1) papier, (2) nożyce, (3) kamień")
            while True:
                player1_move = getpass.getpass("Wybierz ruch (wpisz 1, 2 lub 3): ")
                if player1_move in ["1", "2", "3"]:
                    return actions[int(player1_move) - 1]
                else:
                    print("Nieprawidłowy wybór, spróbuj ponownie.")


    def get_winner(player1_move, player2_move):
        if player1_move == "papier" and player2_move == "nożyce":
            return 2
        elif player1_move == "nożyce" and player2_move == "kamień":
            return 2
        elif player1_move == "kamień" and player2_move == "papier":
            return 2
        elif player1_move == player2_move:
            return 0
        else:
            return 1

    for round_num in range(1, rounds + 1):
        print(f"Runda {round_num}:")
        player1_move = choose_action(player1_name)
        player2_move = choose_action(player2_name)
        print(f"{player1_name}: {player1_move}, {player2_name}: {player2_move}")
        winner = get_winner(player1_move, player2_move)
        if winner == 0:
            print("Remis!")
        else:
            winner_name = player1_name if winner == 1 else player2_name
            print(f"{winner_name} wygrał rundę!")
            scores[winner_name] += 1

    print("Wyniki:")
    for player_name, score in scores.items():
        print(f"{player_name}: {score}")
    if scores[player1_name] > scores[player2_name]:
        print(f"{player1_name} wygrał grę!")
    elif scores[player2_name] > scores[player1_name]:
        print(f"{player2_name} wygrał grę!")
    else:
        print("Remis!")


