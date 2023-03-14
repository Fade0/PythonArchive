
if __name__ == '__main__':
    a = input("Liczba A\n")
    print("Liczba A:", a)
    b = input("Liczba B\n")
    print("Liczba B:", b)
    znak = input("Podaj znak działania [+, -, *, /, ^]\n")
    print("Podany znak:", znak)


    if(znak == "+"):
        print(int(a)+int(b))
    elif(znak == "-"):
        print(int(a)-int(b))
    elif (znak == "*"):
        print(int(a)*int(b))
    elif (znak == "/"):
        print(int(a)/int(b))
    elif (znak == "^"):
        print(int(a)**int(b))
