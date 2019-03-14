

from PlatziAgenda import PlatziAgenda

def PlatziSlackComando( comandero, comando, func ):
    def new_function( *args, **kwargs ):
        agenda = PlatziAgenda()
        return func(agenda, *args)
    comandero.nuevo( comando, new_function )



