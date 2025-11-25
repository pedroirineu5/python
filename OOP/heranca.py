class Carro:
    numero_roda = 4
    quantidade_passageiros = 5 
    
    def acelerar(self):
        print('Acelerando...')
    
    def frear(self):
        print('Freando...')

    def buzinar(self):
        print('Acelerando...')

class Uno(Carro):
    modelo = 'Uno'
    marca = 'fiat'
    ano = 1992


uno = Uno()

uno.acelerar()