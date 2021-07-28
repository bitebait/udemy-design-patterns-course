from abc import ABCMeta, abstractmethod


# Template Method
class Viagem(metaclass=ABCMeta):

    @abstractmethod
    def ida(self):
        pass

    @abstractmethod
    def primeiro_dia(self):
        pass

    @abstractmethod
    def segundo_dia(self):
        pass

    @abstractmethod
    def terceiro_dia(self):
        pass

    @abstractmethod
    def retorno(self):
        pass

    def itinerario(self):
        self.ida()
        self.primeiro_dia()
        self.segundo_dia()
        self.terceiro_dia()
        self.retorno()


class ViagemVeneza(Viagem):

    def ida(self):
        print('Viagem de avião...')

    def primeiro_dia(self):
        print('Visita à Basílica de São Marcos na Praça São Marcos')

    def segundo_dia(self):
        print('Visita ao Palácio Doge')

    def terceiro_dia(self):
        print('Aproveitar a comida próximo à Ponte Rialto')

    def retorno(self):
        print('Viagem de avião...')


class ViagemMalvinas(Viagem):

    def ida(self):
        print('Viagem de ônibus...')

    def primeiro_dia(self):
        print('Aprecisar a vida marinha de Banana Reef')

    def segundo_dia(self):
        print('Praticar esportes aquáticos')

    def terceiro_dia(self):
        print('Relaxar na praia e aproveitar o sol')

    def retorno(self):
        print('Viagem de avião...')


class GeekTravel:

    def preparar_viagem(self):
        opcao = input('Qual viagem deseja fazer? [Veneza, Malvinas]: ')
        if opcao == 'Veneza':
            self.viagem = ViagemVeneza()
            self.viagem.itinerario()
        elif opcao == 'Malvinas':
            self.viagem = ViagemMalvinas()
            self.viagem.itinerario()
        else:
            print('Opção inválida!')


if __name__ == '__main__':
    agencia = GeekTravel()
    agencia.preparar_viagem()
