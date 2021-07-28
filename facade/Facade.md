## 📝 Facade

** *Exemplos e conteúdos adptados e retirados do curso ["Padrões de Projeto (Design Patterns) com Python"](https://www.udemy.com/course/padroes-de-projeto-com-python)*

​

### Introdução

O padrão Facade oculta as complexidades do sistema interno e oferece uma inteface ao cliente para que este possa acessar o sistema de forma simplificada.
Um pouco mais sobre o Facade:

- Oferece uma interface unificada para um conjunto de interfaces em um subsistema e define uma inteface de alto nível que ajuda o cliente a usar o subsistema de forma fácil
- O Facade procura fazer a representação de um subsistema complexo com um único objeto de interface. Ele não encapsula o subsistema, mas, na verdade, combina os subsistemas subjacentes
- Promove o desacoplamento da implementação com vários clientes

​

* * *

​

### Exemplos

```python
# Facade
class GerenciamentoEventos:

    def __init__(self):
        print('GerenciamentoEventos :: Vou organizar com todo mundo!\n\n')

    def organizar(self):
        self.salao = SalaoFestas()
        self.salao.agendar()

        self.florista = Florista()
        self.florista.arranjar_flores()

        self.comida = Restaurante()
        self.comida.preparar()

        self.musica = Banda()
        self.musica.montar_palco()


# Subsistema 1
class SalaoFestas:

    def __init__(self):
        print('SalaoFestas :: Agendando o salão de festas para o casamento...')

    def _esta_disponivel(self):
        print('SalaoFestas :: Este salão de festas está disponível?')
        return True

    def agendar(self):
        if self._esta_disponivel():
            print('SalaoFestas :: Agendamento do salão realizado.\n')


# Subsistema 2
class Florista:

    def __init__(self):
        print('Florista :: Flores para um evento?')

    def arranjar_flores(self):
        print('Florista :: Rosas, Margaridas e Lírios serão usados...\n')


# Subsistema 3
class Restaurante:

    def __init__(self):
        print('Restaurante ::Comida para eventos...')

    def preparar(self):
        print('Restaurante :: Comida chinesa e brasileira serão servidas... \n')


# Subsistema 4
class Banda:

    def __init__(self):
        print('Banda :: Arranjos musicais para o evento...')

    def montar_palco(self):
        print('Banda :: Preparando o palco para tocar Jazz e Rock no evento. \n')


# Cliente
class Cliente:

    def __init__(self):
        print('Cliente :: Uau! Preparação para o casamento!')

    def contrata_gerente_eventos(self):
        print('Cliente :: Vou contratar uma empresa que gerencia eventos\n')

        ge = GerenciamentoEventos()
        ge.organizar()

    def __del__(self):
        print('Cliente :: Foi muito simples organizar este evento com o Facade...')


if __name__ == '__main__':
    cliente = Cliente()
    cliente.contrata_gerente_eventos()
```

​

* * *

​

### Princípio do Conhecimento Mínimo

Como vimos anteriormente, o padrão Facade oferece um sistema unificado que faclita o uso de subsistemas. Além disso, o Facade desacopla o cliente do subsistema.
O princípio de design de software utilizado por trás do padrão Facade é conhecido como Princípio do Conhecimento Mínimo.

O Princípio do Conhecimento Mínimo nos orienta no sentido de reduzir as interações entre os objetos a apenas alguns amigos que sejam próximos a você. Isso significa que:

- Quando fizermos o design de um sistema, para todo objeto criado, devemos observar o número de classes com que essa classe interage e o modo como a interação ocorre
- Seguindo estre princípio, certifique-se de evitar situações em que haja muitas classes criadas que estejam altamente acopladas umas às outras
- Se houver muitas dependências entre as classes, o sistema será difícil de manter. Qualquer mudança em uma parte do sistema poderá resultar em alterações não intencionais em outras partes, o que significa que o sistema estará exposta a regressões, e isso deve ser evitado

​

### Principais Dúvidas sobre o padrão Facade

- D1 - Ao buscar mais informações sobre o padrão Facade ouvi falar sobre a Leite de Demeter. Como ela está relacionada com este padrão?
  - R1 - A Leite de Demeter diz que cada unidade de software deve ter um conhecimento apenas limitado de outras unidades do sistema. Uma unidade deve se comunicar apenas com seus amigos. Uma unidade não deve conhecer os detalhes internos do objeto que ela manipula.
 O Princípio do Conhecimento Mínimo e a Leite de Demeter são iguais, e ambos apontam para a filosofia do Baixo Acoplamento.
- D2 - Pode haver vários Facades em um subsistema?
  - R2 - Sim, podemos implementar mais de uma fachada para um grupo de componentes do subsistema.
- D3 - Quais são as desvantagens do Princípio do Conhecimento Mínimo?
  - R3 - Usando o padrão Facade fazemos uso de uma interface simplificada para os clientes interagirem com o sistema. No intuito de oferecer esta interface simplificada, uma aplicação poderá ter várias interfaces desnecessárias que aumentarão a complexidade do sistema reduzindo o desempenho em tempo de execução.
- D4 - O cliente pode acessar os subsistemas de forma direta/independente?
  - R4 - Sim, mas devemos lembrar que o padrão Facade oferece interfaces simplificadas para que o cliente não precise se preocupar com a complexidade dos subsistemas.
- D5 - O padrão Facade acrescenta alguma funcionalidade própia ao sistema?
  - R5 - Fazendo uso do padrão Facade podemos adicionar uma lógica aos subsistemas, por exemplo, garantindo que a ordem de invocação dos subsistemas possa ser decidida pelo Facade.
