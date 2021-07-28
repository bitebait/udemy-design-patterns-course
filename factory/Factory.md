## 📝 Factory

** *Exemplos e conteúdos adptados e retirados do curso ["Padrões de Projeto (Design Patterns) com Python"](https://www.udemy.com/course/padroes-de-projeto-com-python)*

​

### Introdução

O padrão de projetos ***Factory*** (Fábrica), assim como ***Singleton***, faz parte da classificação de padrões de projetos de criação; 
Enquanto o padrão de projetos Singleton é um dos mais simples, o padrão Factory é sem dúvida o mais utilizado no desenvolvimento de software.

Em POO, o termo fábrica (Factory) refere-se a uma classe responsável por criar objetos de outros tipos. Geralmente, a classe que atua como fábrica tem um objeto e métodos associados a ela. O cliente chama esse método com determinados parâmetros, e os objetos do tipo desejado são criado e desenvolvidos ao cliente pela fábrica.

​

### Vantagens

- Baixo acoplamento pois a criação de um objeto pode ser independente da implementação da classe
- O cliente não precisa conhecer classe que cria o objeto. É necessário conhecer apenas a interface, os métodos e parâmetros que devem ser passados para criar os objetos do tipo desejado. Isso simplifica as implementações para o cliente
- Adicionar outra classe à fábrica para criar objetos de outro tipo pode ser facilmente implementado sem que o cliente altere o código
- A fábrica pode reutilizar objetos existentes. Por outro lado, se o cliente criar objetos diretamente, um novo objeto sempre será criado

​

### Tipos de Factory

- Simple Factory (Fábrica Simples)
  - Permite que as interfaces criem objetos sem expor a lógica de sua criação
- Factory Method (Método de Fábrica)
  - Permite que as intefaces criam objetos, mas adia a decisão para que as subclasses determinem a classe para a criação do objeto
- Abstract Factory (Fábrica Abstrata)
  - Uma interface para criar objetos relacionados sem especificar/expor suas classes; o padrão fornece objetos de outra fábrica que, internamente, cria outros objetos

​

* * *

​

### Exemplos

### - Simple Factory

```python
from abc import ABCMeta, abstractmethod


class Animal(metaclass=ABCMeta):

    @abstractmethod
    def falar(self):
        pass


class Cachorro(Animal):

    def falar(self):
        print('Au au!')


class Gato(Animal):

    def falar(self):
        print('Miau!')


# Factory
class Fabrica:

    def criar_animal_falante(self, tipo):
        return eval(tipo)().falar()


# Client
if __name__ == '__main__':
    fab = Fabrica()
    animal = input('Qual animal você quer que fale? [Cachorro, Gato] ')
    fab.criar_animal_falante(animal)
```

​

### - Factory Method

```python
from abc import ABCMeta, abstractmethod


class Secao(metaclass=ABCMeta):

    @abstractmethod
    def __repr__(self):
        pass


class SecaoPessoal(Secao):

    def __repr__(self):
        return 'Seção Pessoal'


class SecaoAlbum(Secao):

    def __repr__(self):
        return 'Seção Álbum'


class SecaoProjeto(Secao):

    def __repr__(self):
        return 'Seção Projeto'


class SecaoPuplicacao(Secao):

    def __repr__(self):
        return 'Seção Publicação'


class Perfil(metaclass=ABCMeta):

    def __init__(self):
        self.secoes = []
        self.criar_perfil()

    @abstractmethod
    def criar_perfil(self):
        pass

    def get_secoes(self):
        return self.secoes

    def add_secao(self, secao):
        self.secoes.append(secao)


class Linkedin(Perfil):

    def criar_perfil(self):
        self.add_secao(SecaoPessoal())
        self.add_secao(SecaoProjeto())
        self.add_secao(SecaoPuplicacao())


class Facebook(Perfil):

    def criar_perfil(self):
        self.add_secao(SecaoPessoal())
        self.add_secao(SecaoAlbum())


if __name__ == '__main__':
    rede_social = input(
        'Qual rede social quer criar o perfil? [Linkedin, Facebook] ')

    perfil = eval(rede_social)()

    print(f'Criando o perfil em {type(perfil).__name__}')
    print(f'O perfil tem as seções: {perfil.get_secoes()}')
```

​

### - Abstract Factory

```python
from abc import ABCMeta, abstractmethod


# AbstractFactory
class PizzaFactory(metaclass=ABCMeta):

    @abstractmethod
    def criar_pizza_veg(self):
        pass

    @abstractmethod
    def criar_pizza(self):
        pass


# ConcretoFactoryA
class PizzaBrasileira(PizzaFactory):

    def criar_pizza_veg(self):
        return PizzaMandioca()

    def criar_pizza(self):
        return PizzaCamarao()


# ConcretoFactoryB
class PizzaItaliana(PizzaFactory):

    def criar_pizza_veg(self):
        return PizzaBrocolis()

    def criar_pizza(self):
        return PizzaBolonha()


# AbstractProdutoA
class PizzaVeg(metaclass=ABCMeta):

    @abstractmethod
    def preparar(self, PizzaVeg):
        pass


# AbstractProdutoB
class Pizza(metaclass=ABCMeta):

    @abstractmethod
    def servir(self, PizzaVeg):
        pass


# ProdutoConcreto
class PizzaMandioca(PizzaVeg):

    def preparar(self):
        print(f'Preparando {type(self).__name__}')


# ProdutoConcreto
class PizzaCamarao(Pizza):

    def servir(self, PizzaVeg):
        print(
            f'{type(self).__name__} é servida com camarão na {type(PizzaVeg).__name__}')


# ProdutoConcreto
class PizzaBrocolis(PizzaVeg):

    def preparar(self):
        print(f'Preparando {type(self).__name__}')


# ProdutoConcreto
class PizzaBolonha(Pizza):

    def servir(self, PizzaVeg):
        print(f'{type(self).__name__} é servida com camarão na {type(PizzaVeg).__name__}')


# Cliente
class Pizzaria:

    def fazer_pizzas(self):
        for factory in [PizzaBrasileira(), PizzaItaliana()]:
            self.factory = factory
            self.pizza = self.factory.criar_pizza()
            self.pizza_veg = self.factory.criar_pizza_veg()
            self.pizza_veg.preparar()
            self.pizza.servir(self.pizza_veg)


pizzaria = Pizzaria()
pizzaria.fazer_pizzas()
```
