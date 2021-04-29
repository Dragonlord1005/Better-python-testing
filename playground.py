x = 1


def y():
    print(x)


def c():
    y = 3

    def h():
        print(y + x)

    h()


c()
