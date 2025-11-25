class Animal:

    def emitir_som(self):
        print('Emitindo som...')


class Cachorro(Animal):

    def emitir_som(self):
        print('Au au!')

class Gato(Animal):

    def emitir_som(self):
        print('Miau!')

cachorro = Cachorro()
gato = Gato()


cachorro.emitir_som
gato.emitir_som