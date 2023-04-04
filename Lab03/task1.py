def cw1():
    numbers = input("Podaj liczby rozdzielone przecinkiem: \n")
    numbers_list = numbers.split(",")

    max_number = int(numbers_list[0])
    min_number = int(numbers_list[0])

    for number in numbers_list:
        number = int(number)
        if number > max_number:
            max_number = number
        if number < min_number:
            min_number = number

    print("Największa liczba to:", max_number)
    print("Najmniejsza liczba to:", min_number)
