
if __name__ == '__main__':
    ans = ""
    userAnswears = []
    tablicaPytan = [
        "1. Najczęstszym sposobem spędzania wolnego czasu jest dla Ciebie: ",
        "2. W jakich okolicznościach czytasz książki najczęściej? ",
        "3. Jeżeli spędzasz czas wolny czytając książki, jaki jest główny powód takiego wyboru",
        "4. Po książki w jakiej formie sięgasz najczęściej? ",
        "5. Ile książek czytasz średnio w ciągu roku? ",
        "6. Jak często średnio czytasz książki? ",
        "7. Po jakie gatunki książek sięgasz najczęściej? "
    ]

    Q1 = {
        "q": tablicaPytan[0],
        "a":"oglądanie telewizji/filmów/seriali",
        "b":"czytanie książek/czasopism",
        "c":"słuchanie muzyki",
    }

    Q2 = {
        "q": tablicaPytan[1],
        "a":"podczas podróży",
        "b":"w czasie wolnym (po pracy, na urlopie)",
        "c":"podczas pracy/nauki (to ich element)",
    }

    Q3 = {
        "q": tablicaPytan[2],
        "a":"chęć poszerzenia wiedzy",
        "b":"czytanie mnie relaksuje/odpręża",
        "c":"fakt, że czytanie jest modne",
    }

    Q4 = {
        "q": tablicaPytan[3],
        "a":"papierowej (tradycyjnej)",
        "b":"e-booki (książki elektroniczne) na komputerze",
        "c":"e-booki na tablecie/telefonie",
    }

    Q5 = {
        "q": tablicaPytan[4],
        "a":"0",
        "b":"żadnej w całości - jedynie fragmenty",
        "c":"1",
    }

    Q6 = {
        "q": tablicaPytan[5],
        "a":"codziennie",
        "b":"raz w tygodniu",
        "c":"raz w miesiącu",
    }

    Q7 = {
        "q": tablicaPytan[6],
        "a":"kryminały/thrillery",
        "b":"romanse",
        "c":"psychologiczne",
    }

    #Pytanie 1
    print(Q1['q'],"\t")
    print(Q1['a'],"\t")
    print(Q1['b'],"\t")
    print(Q1['c'],"\t")

    ans = input("Podaj swoją odpowiedź: \n")
    userAnswears.append(ans)

    #Pytanie 2
    print(Q2['q'],"\t")
    print(Q2['a'],"\t")
    print(Q2['b'],"\t")
    print(Q2['c'],"\t")

    ans = input("Podaj swoją odpowiedź: \n")
    userAnswears.append(ans)

    #Pytanie 3
    print(Q3['q'],"\t")
    print(Q3['a'],"\t")
    print(Q3['b'],"\t")
    print(Q3['c'],"\t")

    ans = input("Podaj swoją odpowiedź: \n")
    userAnswears.append(ans)

    #Pytanie 4
    print(Q4['q'],"\t")
    print(Q4['a'],"\t")
    print(Q4['b'],"\t")
    print(Q4['c'],"\t")

    ans = input("Podaj swoją odpowiedź: \n")
    userAnswears.append(ans)

    #Pytanie 5
    print(Q5['q'],"\t")
    print(Q5['a'],"\t")
    print(Q5['b'],"\t")
    print(Q5['c'],"\t")

    ans = input("Podaj swoją odpowiedź: \n")
    userAnswears.append(ans)

    #Pytanie 6
    print(Q6['q'],"\t")
    print(Q6['a'],"\t")
    print(Q6['b'],"\t")
    print(Q6['c'],"\t")

    ans = input("Podaj swoją odpowiedź: \n")
    userAnswears.append(ans)

    #Pytanie 7
    print(Q7['q'],"\t")
    print(Q7['a'],"\t")
    print(Q7['b'],"\t")
    print(Q7['c'],"\t")

    ans = input("Podaj swoją odpowiedź: \n")
    userAnswears.append(ans)

    print(userAnswears)