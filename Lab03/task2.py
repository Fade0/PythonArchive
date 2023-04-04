def cw2():
    import random

    cities = ["Warszawa",
              "Kraków",
              "Łódź",
              "Wrocław",
              "Poznań",
              "Gdańsk",
              "Szczecin",
              "Bydgoszcz",
              "Lublin",
              "Katowice"]

    selected_cities = random.sample(cities, 10)

    print("Plan wycieczki po Polsce: ")
    for i, city in enumerate(selected_cities):
        print(f"{i+1}. {city}")