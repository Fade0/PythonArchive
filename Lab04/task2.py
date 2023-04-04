from math import sqrt


def cw2():
    # Zadanie 2. Napisz funkcję sprawdzającą czy podane liczby są liczbami pierwszymi w szybszy sposób niż w przykładzie.
    # Do funkcji można przekazać dowolną liczbę argumentów (liczby).
    # Liczby 0 i 1 nie są liczbami pierwszymi. (10%)

    userInput = numberInput()

    checkNumbers(userInput)


def numberInput():
    numberString = input("Please enter your numbers split them using ',' \n")
    numbersList = numberString.split(",")
    print(numbersList)

    return numbersList


def isPrime(n):
    prime_flag = 0

    if (n > 1):
        for i in range(2, int(sqrt(n)) + 1):
            if (n % i == 0):
                prime_flag = 1
                break
        if (prime_flag == 0):
            print("True")
        else:
            print("False")
    else:
        print("False")


def checkNumbers(numbers):
    for n in numbers:
        result = isPrime(int(n))
        print(result)

    return
