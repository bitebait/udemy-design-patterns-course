## 📝 Revisão de Programação Orientada a Objetos

** *Exemplos e conteúdos adptados e retirados do curso ["Padrões de Projeto (Design Patterns) com Python"](https://www.udemy.com/course/padroes-de-projeto-com-python)*

​

### - Classes

* Representam **entidades** do mundo real
* Definem os objetos com **atributos** e comportamentos (**métodos**)
* Possuem **construtores** (método especial) que proporcionam o estado inicial para os **objetos**
* Classes são como templates (**modelos**), portanto, podem ser facilmente **reutilizadas**

​

### - Métodos

* Representam o **comportamento dos objetos**, ou seja, as **ações** que estes objetos podem praticar
* Os métodos atuam nos **atributos** além de implementar a **funcionalidade** desejada para o objeto

​

### - Objetos

* Representam **entidades no contexto da aplicação** em desenvolvimento
* Entidades **interagem entre si** para resolver problemas do mundo real

​

#### Exemplo

* Pessoa é uma entidade e Carro também é uma entidade
* Pessoa dirige Carro para se deslocar de um lugar para outro

​

### Exemplo de Classe

```python
class Person:
    """Representa uma pessoa do mundo real."""

    def __init__(self, first_name, last_name):
        self.first_name = first_name
        self.last_name = last_name

    def __str__(self):
        return self.first_name

    def get_full_name(self):
        return "{} {}".format(self.first_name, self.last_name)

pessoa = Person("William", "Schwaab")

print(pessoa)
# William

print(pessoa.get_full_name())
# William Schwaab
```

* *  *

​

### - Encapsulamento

* O comportamento de um objeto permanece oculto para o mundo externo, ou os objetos mantêm suas informações de estado (atributos) como privadas
* Os clientes não podem alterar o estado interno dos objetos atuando diretamente em seus atributos; em vez disso estas alterações devem ser realizadas através de métodos

*Em Python, o conceito de encapsulamento não é implícito pois não existem palavras reservadas como **public**, **private** e **protected** necessarias para tratar este conceito.*

​

### - Polimorfismo

O polimorfismo pode ser de dois tipos:

* Um objeto oferece diferentes implementações de um método de acordo com os parâmetros de entrada
* A mesma interface (implementação) pode ser usada por objetos de tipos diferentes

​

### - Herança

Usamos herança para darmos mais flexibilidade às nossas classes e o poder de reutilização, além de:

* A herança indica que uma classe deriva (extende) sua funcionalidade da classe-pai

* A herança permite que reutilizemos características e funcionalidades definidas na classe-pai
* A herança cria hierarquias por meio do relacionamento entre objetos de diferentes classes

​

### - Abstração

* A abstração oferece uma interface (implementação) simples aos clientes, por meio da qual eles podem interagir com os elementos do programa e utilizar os métodos que foram difinidos
* Abstraindo (simplificando) a complexidade do programa os clientes não precisam conhecer as implementações internas, bastando apenas executá-las

​

### - Composição

* A composição nos ajuda a combinar objetos ou classes em estruturas de dados ou implementações mais complexas
* Na composição, um objeto é usado para chamar/executar métodos de outras classes, disponibilizando assim, as funcionalidades básicas sem o uso de herança
