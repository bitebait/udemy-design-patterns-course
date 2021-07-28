## 📝 Singleton

** *Exemplos e conteúdos adptados e retirados do curso ["Padrões de Projeto (Design Patterns) com Python"](https://www.udemy.com/course/padroes-de-projeto-com-python)*
​
​

### - Introdução

Um dos padrões de projeto mais simples e conhecidos no mundo da programação. O **_Singleton_** proporciona uma forma de ter um, e somente um, objeto de determinado tipo, além de um ponto de acesso global à este objeto.

​

### Exemplos de uso

> - Logging (logs)
> - Operações de Database
> - Spoolers de Impressão

...e outros cenários que haja apenas uma única instância de determinado objeto diponível para toda a aplicação.

Em resumo, você irã usar **_Singleton_** se suas intenções são:

> - Garantir que um e somente um objeto de determinada classe seja instanciado
> - Oferecer um ponto de acesso para o objeto que seja global no programa
> - Controlar o acesso concorrente a recursos compartilhados

​

## Desvantagens do padrão Singleton

- Variáveis globais podem ser alterada por engano em algum lugar e, como o desenvolvedor pode achar que elas permanecem inalteradas, as variáveis poderão acabar sendo usadas em outro lugar na aplicação
- Variáveis referência podem ser criadas para o mesmo objeto. Como o Singleton cria apenas um objeto, várias referências podem ser criadas neste ponto para o mesmo objeto
- Todas as classes que são dependentes de variáveis globais acabam se tornando altamente acopladas, pois uma mudança feita por uma classe no dado global poderá exercer um impacto em outra classe

​

### Exemplo de Implementação

```python
class Singleton(object):

    def __new__(cls):
        if not hasattr(cls, 'instance'):
            cls.instance = super(Singleton, cls).__new__(cls)
        return cls.instance

s1 = Singleton()
print(f'Instância 1: {id(s1)}')

s2 = Singleton()
print(f'Instância 2: {id(s2)}')
```

​

### Lazy Singleton

```python
class Singleton:

    __instance = None

    def __init__(self):
        if not Singleton.__instance:
            print('O método __init__ foi chamado...')
        else:
            print(f'A instância ja foi criada: {self.get_instance()}')

    @classmethod
    def get_instance(cls):
        if not Singleton.__instance:
            cls.__instance = Singleton()
        return cls.__instance

s1 = Singleton()

print(f'Objeto criado agora: {Singleton.get_instance()}')

s2 = Singleton()  # Instância já criada...
```

​

### Monostate

```python
class Monostate:
    """Diferentes instâncias compartilhando o mesmo estado."""

    __estado = {}

    def __new__(cls, *args, **kwargs):
        obj = super(Monostate, cls).__new__(cls, *args, **kwargs)
        obj.__dict__ = cls.__estado
        return obj

m1 = Monostate()
print(f'M1 ID: {id(m1)}')
print(m1.__dict__)

m2 = Monostate()
print(f'M2 ID: {id(m2)}')
print(m2.__dict__)

m1.nome = 'Test'
print(f'M1: {m1.__dict__}')
print(f'M2: {m2.__dict__}')
```

​

### Singleton Metaclasses

```python
class MetaSingleton(type):

    __instances = {}

    def __call__(cls, *args, **kwargs):
        if cls not in cls.__instances:
            cls.__instances[cls] = super(
                MetaSingleton, cls).__call__(*args, **kwargs)
        return cls.__instances[cls]

class Logger(metaclass=MetaSingleton):
    pass

log1 = Logger()
print(f'Log 1: {id(log1)}')

log2 = Logger()
print(f'Log 2: {id(log2)}')
```

​

---

## Exemplos Práticos

### Primeiro Exemplo

```python
import sqlite3

class Singleton(type):

    _instances = {}

    def __call__(cls, *args, **kwargs):
        if cls not in cls._instances:
            cls._instances[cls] = super(
                Singleton, cls).__call__(*args, **kwargs)
        return cls._instances[cls]

class Database(metaclass=Singleton):

    connection = None

    def connect(self):
        if self.connection is None:
            self.connection = sqlite3.connect("database.sqlite3")
            self.cursor = self.connection.cursor()
        return self.cursor

db1 = Database().connect()
db2 = Database().connect()

print(f'Db 1: {db1}')
print(f'Db 2: {db2}')
```

​

### Segundo Exemplo

```python
class SanidadeCheck:

    __instance = None

    def __new__(cls, *args, **kwargs):
        if not SanidadeCheck.__instance:
            SanidadeCheck.__instance = super(
                SanidadeCheck, cls).__new__(cls, *args, **kwargs)
        return SanidadeCheck.__instance

    def __init__(self):
        self.__servidores = []

    def checar_servidor(self, srv):
        print(f'Checando o {self.__servidores[srv]}')

    def add_servidor(self):
        self.__servidores.append('Servidor 1')
        self.__servidores.append('Servidor 2')
        self.__servidores.append('Servidor 3')
        self.__servidores.append('Servidor 4')

    def mudar_servidor(self):
        self.__servidores.pop()
        self.__servidores.append('Servidor 5')

sc1 = SanidadeCheck()
sc2 = SanidadeCheck()

sc1.add_servidor()
print('Cronograma de checagem de sanidade dos servidores A...')
[sc1.checar_servidor(srv) for srv in range(4)]

sc2.mudar_servidor()
print('Cronograma de checagem de sanidade dos servidores B...')
[sc2.checar_servidor(srv) for srv in range(4)]
```
