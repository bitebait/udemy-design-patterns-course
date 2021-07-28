class Model:

    def __init__(self):
        self.produtos = {
            'ps5': {'id': 1, 'nome': 'Playstation 5', 'preco': 1244},
            'xbox': {'id': 2, 'nome': 'Xbox Series X', 'preco': 1445},
            'swtich': {'id': 3, 'nome': 'Nintendo Switch', 'preco': 1700},
        }


class Controller:

    def __init__(self):
        self.modelo = Model()

    def listar_produtos(self):
        produtos = self.modelo.produtos.keys()

        print('------------Produtos-------------')
        for chave in produtos:
            print(f"ID: {self.modelo.produtos[chave]['id']}")
            print(f"Nome: {self.modelo.produtos[chave]['nome']}")
            print(f"Preço: {self.modelo.produtos[chave]['preco']}\n")


class View:

    def __init__(self):
        self.controlador = Controller()

    def produtos(self):
        self.controlador.listar_produtos()


if __name__ == '__main__':
    view = View()
    view.produtos()
