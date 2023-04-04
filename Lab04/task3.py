def cw3():
    #Zestaw 3. Napisz funkcję szyfrującą wiadomość szyfrem cezara.
    #Dla ułatwienia należy przekształcić wiadomość tak aby zawierała tylko wielkie lub małe litery.
    # Funkcja przyjmuje: wiadomość
    #– tekst do zaszyfrowania, klucz
    #– liczbę o ile należy przesunąć litery w alfabecie oraz zwraca zaszyfrowaną wiadomość w formie łańcucha znaków -string. (40%)
    #Funkcja szyfruje tylko litery – inne znaki wstawia do końcowej zaszyfrowanej wiadomości bez zmian(10%)
    #Funkcja rozwiązuje problem klucza przesuwającego litery poza zakres listy  z alfabetem oraz problem podania klucza o dowolnej wielkości(20%).
    #Funkcja opcjonalnie przyjmuje dowolny alfabet. Domyślnie używa angielskiego(10%).

    message = input("Text to change XD")
    key = int(input("Type code"))
    #lang = input("what language \n")

    langDictionary = {
        "ENGLISH": 26,
        "POLISH": 32,
        "SPANISH": 27
    }

    result = caesarCode(message,key)
    print(result)


def checkIfPossible(c):
    doNotChangeList = [",", ".", "/", "\\", "-", "+", "=", "`", "?", "<", ">", "£",
                       "!", "@", "#", "$", "%", "^", "7", "*", "(", ")",
                       "0", "1", "2", "3", "4", "5", "6", "7", "8", "9"]

    for i in range(0, len(doNotChangeList)):
        #print(doNotChangeList, " z listy")
        print(i, "moje i")
        print(c, "moje c")
        if(c == doNotChangeList[i]):
            print(i, "<- i")
            print("Falseee")
            return False
    return True
def caesarCode(message, key):
    result = ""
    langLetterCount = 26

    if (key >= langLetterCount):
        key = key % int(langLetterCount)
        print("key was reduced to", key)

    for letter in message:
        if (checkIfPossible(letter) == True):
            print("brake here")
            result += letter

        if ord(letter) + key > ord('z'):
            result += chr(ord(letter) + key - int(langLetterCount)).capitalize()
        else:
            result += chr(ord(letter) + key).capitalize()

    return result + " final"



