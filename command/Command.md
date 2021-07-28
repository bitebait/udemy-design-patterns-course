## 📝 Command

** *Exemplos e conteúdos adptados e retirados do curso ["Padrões de Projeto (Design Patterns) com Python"](https://www.udemy.com/course/padroes-de-projeto-com-python)*

​

### Introdução

Já aprendemos que os padrões de projetos comportamentais tem como foco as responsabilidades de um objeto, pois eles lidam com a interação entre objetos para alcançar funcionalidades mais complexas.
O padrão Command é um padrão de projeto comportamental, em que um objeto é usado para encapsular todas as informações necessárias para executar uma ação ou disparar um evento posteriormente. Estas informações incluem:

- O nome do método
- Um objeto que seja dono do método
- Valores para os parâmetros do método

​

### Contextualizando o padrão Command

Para entender o padrão Command, considere o caso de um assistente (wizard) de instalação.
Um assistente típico pode ter várias etapas ou telas que capturem preferências de um usuário. Enquanto navega pelo assistente, o usuário faz determinadas escolhas.
Os assistentes geralmente são implementados com padrão Command.
Um assistente é iniciado com um objeto chamado Command. As preferências ou escolhas feitas pelo usuário nas várias etapas do assistente são armazenadas no objeto Command.
Quando o usuário clica no botão "Fim" (Finish) na última tela do assistente, o objeto Command executa um método *execute()* que considera todas as opções armazenadas e faz o procedimento de instalação apropriado.
Assim, todas as informações relacionadas às escolhas são encapsuladas em um objeto que pode ser usado mais tarde para executar uma ação.

​

### Compreendendo o padrão Command

O padrão Command trabalha com os seguintes termos:

- **Command** - Um objeto Command conhece os objetos Receiver e invoca um método deste objeto
- **Receiver** Os valores dos parâmetros do método receptor (Receiver) são armazenados no objeto Command
- **Invoker** - O chamados ou invocador (invoker) sabe como executar um comando
- **Client** - O cliente cria um objeto Command e define o seu receptor

​

### Os principais objetos do padrão Command

- Encapsular uma requisição como um objeto
- Possibilitar a parametrização dos clientes com diferentes requisições
- Permitir salvar as requisições em uma fila
- Oferecer uma callback orientada a objetos

​

### Exemplos de casos de uso do padrão Command

- Parametrizar objetos de acordo com a ação a ser executada
- Adicionar ações em uma fila e executar as requisições em pontos diferentes
- Criar uma estrutura para operações de alto nível baseadas em operações menores

​

### Exemplo de Código

```python
from abc import ABCMeta, abstractmethod


# InterfaceCommand
class Ordem(metaclass=ABCMeta):

    @abstractmethod
    def executar(self):
        pass


# ComandoConcreto
class OrdemCompra(Ordem):

    def __init__(self, acao):
        self.acao = acao

    def executar(self):
        self.acao.comprar()


class OrdemVenda(Ordem):

    def __init__(self, acao):
        self.acao = acao

    def executar(self):
        self.acao.vender()


# Receiver
class Acao:

    def comprar(self):
        print('Você irá comprar ações...')

    def vender(self):
        print('Você irá vender ações...')


# Invoker
class Agente:

    def __init__(self):
        self.__fila_ordens = []

    def adicionar_ordem_na_fila(self, ordem):
        self.__fila_ordens.append(ordem)
        ordem.executar()


if __name__ == '__main__':
    # Cliente
    acao = Acao()
    ordem_compra = OrdemCompra(acao)
    ordem_venda = OrdemVenda(acao)

    # Invoker
    agente = Agente()
    agente.adicionar_ordem_na_fila(ordem_compra)
    agente.adicionar_ordem_na_fila(ordem_venda)
```

​

* * *

​

### Vantagens e Desvantagens do padrão Command

### - Vantagens

- Desacopla as classes que invocam a operação do objeto
- Permite criar uma sequência de comandos oferecendo um sistema de fila
- Podemos facilmente adicionar um novo comando sem alterar o código existente

### - Desvantagens

- Há um número elevado de classes e objetos trabalhando em conjunto para alcançar um objetivo. Como desenvolvedor de aplicações, você deve tomar cuidado para desenvolver essas classes corretamente
- Todo comando individual é uma classe ComandoConcreto que aumenta o volume de classes para implementação e manutenção

​

* * *

​

### Principais Dúvidas sobre o padrão Command

- D1 - É possível fazer uso do padrão Command mesmo que não haja nenhum Receiver e ComandoConcreto que implementem o método de execução?
  - R1 - Sim, é possível fazer isso. A única questão a ser observada neste caso é a interação entre o Invoker e o Receiver. Se o Receiver não estiver definido, o nível de desacoplamento diminui; além do mais, a facilidade de parametrizar comando será perdida. Na dúvida, implemente o padrão por completo.
- D2 - Qual estrutura de dados devo utilizar para implementar o sistema de fila de execução no objeto chamado?
  - R2 - No exemplo de implementação foi utilizado uma lista para implementar a fila; No entando, o padrão Commando menciona o uso da estrutura de dados **pilha** que é mais conveniente em alguns casos.
