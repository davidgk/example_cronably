from cronably import Cronably


@Cronably(name='prueba', repetition_frame='SECONDS',repetition_period=2, loops=3 )
def hola():
    print "esto es una prueba"


if __name__ == '__main__':
    hola()
