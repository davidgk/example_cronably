from cronably import Cronably


@Cronably(name='prueba')
def hola():
    print "esto es una prueba"


if __name__ == '__main__':
    hola()
