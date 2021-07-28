## 📝 Proxy

** *Exemplos e conteúdos adptados e retirados do curso ["Padrões de Projeto (Design Patterns) com Python"](https://www.udemy.com/course/padroes-de-projeto-com-python)*

​

### Introdução

De forma geral, o Proxy é um sistema que serve de intermdiário entre o solicitante, chamado de seeker, e o provedor, chamado de provider.
O solicitante é quem faz a requisição, e o provedor entrega os recursos em resposta à requisição.

No contexto de padrões de projetos, Proxy é uma classe que atua como uma interface para objetos reais. Os objetos podem ser vários tipos, como conexões de rede, objetos grandes em memória e arquivos, dentre outros.
Em resumo, Proxy é um agente que encapsula o objeto que está realmente servindo, podendo inclusive oferecer funcionalidades adicionais ao objeto que ele encapsula sem alterar o código do objeto.

​

### Compreendendo os diferentes tipos de Proxy

Com base no modo como os proxies são usados, podemos classificá-los como **Proxy Virtual**, **Proxy Remoto**, **Proxy de Proteção** e **Proxy Inteligente**.

- **Proxy Virtual** funciona como um "placeholder" para objetos que são muito pesados para instanciar. Por exemplo, se você quiser carregar uma imagem grande em seu site, esta requisição exigirá bastante tempo de carregamento. Geralmente criamos um ícone de placeholder na página web, sugerindo que ali existe uma imagem, no entando a imagem só sera carregada quando o usuário realmente clicar no ícone, evitando assim o custo de carregar uma imagem pesada na memória.
Desta forma, nos proxies virtuais, o objeto real é criado apenas quando o cliente faz sua primeira requisição ou seu primeiro acesso ao objeto.
- **Proxy Remoto** oferece uma representação local de um objeto real que está em um servidor remoto ou em um espaço de enderaçamento diferente. Por exemplo, imagine que você quer implementar um sistema de monitoração para a sua aplicação que tem vários servidores web, servidores de banco de dados, servidores de taregas Celery e servidores de caching, entre outros.
Se quisermos monitorar a utilização de CPU e de disco nestes servidores, precisamos de um objeto que esteja disponível no contexto em que a aplicação de monitoramento é executada, mas que possa executar comandos remotoos para obter os valores dos parâmetros.
Em casos assim, ter um objeto proxy remoto que seja uma representação local do objeto remoto ajudaria.
- **Proxy de Proteção** controla o acesso às partes sensíveis de um objeto real. Por exemplo, em sistemas distribuídos, as aplicações web tem vários serviõs que operam em conjunto para oferecer funcionalidades. Em sistemas como esses, um serviço de autenticação atua como um servidor de proxy de proteção, responsável pela autenticação e pela atuorização.
Neste caso, o proxy internamente ajuda na proteção das funcionalidades essenciais do site verificando agentes não reconhecidos ou não autorizados. Desta forma, o objeto substituto verifica se quem faz a chamda tem as permissões de acesso necessárias para encaminhar a requisição.
- **Proxy Inteligente** interpõe ações adicionais quando um objeto é acessado. Por exemplo, considere que haja um componente com ponto central único em um sistema que armazene dados em um local centralizado. Geralmente, um componente como este é chamado por vários serviços diferentes para que eles possam concluir suas tarefas, e pode resultar em problemas com recursos compartilhados.
Em vez de os serviços chamarem diretamente o componente, um proxy inteligente é encarregado por verificar se o objeto real está travado (sendo executado) antes de ser acessado a fim de garantir que nenhum outro objeto possa alterá-lo.

​

### Algumas vantagens do padrão **Proxy**

- Os proxies podem ajudar a melhorar o desempenho da aplicação ao fazer caching de objetos pesados ou, geralmente, de objetos acessados com frequência
- Os proxies também autorizam o acesso a um objeto real; portanto este padrão auxilia na delegação somente se as permissões estiverem corretas
- Os proxies remotos também facilitam a interação com servidores remotos, que podem funcionar como conexões de rede e de bancos de dados, além de poderem ser usados para monitorar sistemas

​

* * *

​

### Exemplos

```python
from abc import ABCMeta, abstractmethod


# Interface
class Carteita(metaclass=ABCMeta):

    @abstractmethod
    def pagar(self):
        pass


# ObjetoReal
class Banco(Carteita):

    def __init__(self):
        self.cartao = None
        self.conta = None

    def __get_conta(self):
        self.conta = self.cartao
        return self.conta

    def __tem_saldo(self):
        print(f'Banco:: Checando se a conta {self.__get_conta()} tem saldo.')
        return True

    def set_cartao(self, cartao):
        self.cartao = cartao

    def pagar(self):
        if self.__tem_saldo():
            print('Banco:: Pagando bar...')
            return True
        else:
            print('Banco:: Desculpe, você não tem saldo suficiente...')
            return False


# Proxy
class CartaoDebito(Carteita):

    def __init__(self):
        self.banco = Banco()

    def pagar(self):
        cartao = input('Proxy:: Informe o número do cartão: ')
        self.banco.set_cartao(cartao)
        return self.banco.pagar()


# Cliente
class Cliente:

    def __init__(self):
        print('Cliente:: Quero comprar um amendoim')
        self.cartao_debito = CartaoDebito()
        self.comprei = None

    def fazer_pagamento(self):
        self.comprei = self.cartao_debito.pagar()

    def __del__(self):
        if self.comprei:
            print('Cliente:: Finalmente comprei amendoim!')
        else:
            print('Cliente:: Puts, estou sem dinheiro...')


if __name__ == '__main__':
    cliente = Cliente()
    cliente.fazer_pagamento()
```

​

* * *

​

### Principais Dúvidas sobre o padrão Facade

- D1 - Qual é a diferença entre o padrão Decorator (Decorador) e o padrão Proxy?
  - R1 - Um Decorator acrescenta comportamentos ao objeto que ele decora em tempo de execução, enquanto um Proxy controla o acesso a um objeto. O relacionamento entre Proxy e o objeto real é estabelecido em tempo de compilação, e não é dinâmico.
- D2 - Quais são as desvantagens do padrão Proxy?
  - R2 - O padrão Proxy pode aumentar o tempo de resposta da aplicação. Por exemplo, se o Proxy não tiver uma boa arquitetura ou tiver alguns problemas de desempenho, ele poderá contribuir para aumentar o tempo respostas do objeto. Em geral, tudo depende da qualidade da implementação de um Proxy.
- D3 - O cliente pode acessar o objeto de forma independente ao invés de usar o Proxy?
  - R3 - Sim, mas há certas vantagens que os Proxies oferecem, atuando como proxies virtuais, proxies remotos e outros, portanto é vantajoso usar o padrão Proxy ao invés de acessar diretamente o objeto requisitado.
- D4 - O Proxy acrescenta alguma funcionalidade própria ao objeto?
  - R4 - Um proxy pode acrescentar funcionalidades ao objeto real sem alterar o código do objeto, já que tanto o proxy quanto o objeto real implementam a mesma interface.
