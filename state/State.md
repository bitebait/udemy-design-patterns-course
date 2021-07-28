## 📝 State

** *Exemplos e conteúdos adptados e retirados do curso ["Padrões de Projeto (Design Patterns) com Python"](https://www.udemy.com/course/padroes-de-projeto-com-python)*

​

### Introdução

O padrão de projeto State (estado) é um padrão comportamental que, às vezes, também é chamado de padrão de objetos para estados. Neste padrão, um objeto pode encapsular vários comportamentos de acordo com seu estado interno.
O padrão State também é considerado como uma maneira de um objeto alterar seu comportamento em tempo de execução.
Para entender melhor o padrão State, considere o caso de um rádio simples. Um rádio tem canais AM/FM, uma chave para alterar entre os tipos de canais, além de um botão para escanear canais na fas faixas AM/FM.
Quando um rádio é ligado, seu estado-base já está definido, por exemplo para FM. Ao clicar no botão para escanear canais, o rádio é sintonizado em várias frequências ou canais válidos de FM. Quando o estado-base é alterado para AM, o botão de escaneamento ajuda o usuário a sintonizar vários canais de AM. Então, de acordo com o estado-base do rádio, o comportamento do botão de escaneamento muda dinamicamente, sintonizando canais AM ou FM.

O padrão State permite que um objeto altere o seu comportamento quando o seu estado interno muda. Isso faz parecer que o próprio objeto alterou sua classe.
O padrão de projeto State é usado para desenvolver Máquinas de Estado Finitas (Finite State Machines) e ajuda a acomodar Ações de Transição de Estados (State Transmission Actions).

​

### Compreendendo o padrão de projeto State

- **State** é considerada uma interface que encapsula o comportamento do objeto. Esse comportamento está associado ao estado do objeto.
- **StateConcreto** é uma subclasse que implementa a interface State. Esta subclasse implementa o comportamento propriamente dito associado ao estado particular do objeto.
- **Context** define a interface de interesse dos clientes. Context também mantém uma instância da subclasse StateConcreto que, internamente, define a implementação do estado particular do objeto.

​

### Exemplo de Código

```python
from abc import ABCMeta


class EstadoComputador(metaclass=ABCMeta):
    nome = 'EstadoComputador'
    permitido = []

    def mudar(self, estado):
        if estado.nome in self.permitido:
            print(f'Atual: {self} => mudou de estado para: {estado.nome}')
            self.__class__ = estado
        else:
            print(
                f'Atual: {self} => não pode alterar seu estado para: {estado.nome}')

    def __str__(self):
        return self.nome


class Ligar(EstadoComputador):
    nome = 'Ligar'
    permitido = ['Desligar', 'Suspender', 'Hibernar']


class Desligar(EstadoComputador):
    nome = 'Desligar'
    permitido = ['Ligar']


class Suspender(EstadoComputador):
    nome = 'Suspender'
    permitido = ['Ligar']


class Hibernar(EstadoComputador):
    nome = 'Hibernar'
    permitido = ['Ligar']


class Computador:

    def __init__(self, modelo='Dell'):
        self.modelo = modelo
        self.estado = Desligar()

    def alterar(self, estado):
        self.estado.mudar(estado)


if __name__ == '__main__':
    comp = Computador()

    # Ligar
    comp.alterar(Ligar)

    # Desligar
    comp.alterar(Desligar)

    # Ligar
    comp.alterar(Ligar)

    # Suspender
    comp.alterar(Suspender)

    # Hibernar
    comp.alterar(Hibernar)

    # Ligar
    comp.alterar(Ligar)

    # Desligar
    comp.alterar(Desligar)
```

​

* * *

​

### Vantagens e Desvantagens do padrão State

### - Vantagens

- No padrão State, o comportamento de um objeto é resultado da função de seu estado, e o comportamento muda em tempo de execução de acordo com este estado. Isso elimina a dependência lógica condicional de if/else ou de switch/case (para linguagens que possui).
- Com o padrão State, as vantagens de implementar um comportamento polifórmico são evidentes, além de ser mais fácil adicionar estado para dar suporte a novos comportamentos.
- O padrão de projeto State também melhora a coesão, pois comportamentos específicos de estados são agregados nas classes StateConcreta, que são colocados em um só lugar no código.
- Com o padrão State é muito fácil acrescentar um comportamento simplesmente adicionando mais uma classe StateConcreta. Desta forma aumenta a flexibilidade, permitindo estender o comportamento da aplicação e facilitando a manutenlçao do código em geral.

### - Desvantagens

- Grande aumento do número de classes. Como todo estado deve ser definido com a ajuda de StateConcreta, há uma chance de acabarmos escrevendo muito mais classes com uma pequena funcionalidade.
- Com a introdução de cada novo comportamento, a classe Context deve ser atualzada para lidar com o novo comportamento. Isso deixa o comportamento de Context mais frágil a cada novo comportamento adicionado.
