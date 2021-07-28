## 📝 Template Method

** *Exemplos e conteúdos adptados e retirados do curso ["Padrões de Projeto (Design Patterns) com Python"](https://www.udemy.com/course/padroes-de-projeto-com-python)*

​

### Introdução

Aprendemos em aulas anteriores que os padrões de projetos comportamentais tem como foco as responsabilidades de um objeto, pois eles lidam com a intneração entre objetos para alcançar funcionalidades mais complexas.
O padrão **Template Method** é um padrão de projeto comportamental que define o esqueleto do programa ou m algoritimo em um método chamado *Método Template*.
Você pode, por exemplo, definir os passos para preparar uma bebida como um algoritimo em um Método Template.
O padrão Template Method também ajuda a redefinir ou personalizar os passos do algoritimo adiando a implementação de alguns desses passos para as subclasses. Ou seja, as subclasses podem redefinir o seu próprio comportamento.
Desta forma uma subclasse poderia fazer uso do Método Template para preparar uma bebida e prepar chá enquanto outra subclasse poderia usar o mesmo Método Template para preparar café já que ambas são bebidas.
Vale destacar que a alteração dos passos nas subclasses não exerce impacto na estrutura do algoritimo original. Desta forma, o recurso das subclasses de poder sobrescrever no padrão Template Method permite a criação de diferentes comportamentos ou algoritimos.
No contexto de desenvolvimento de software, uma classe abstrata é usada para definir os passos do algoritimo. Esses passos são conhecidos como operações primitivas no contexto do padrão Template Method. Estas operações são definidas como métodos abstratos e o Método Template define o algoritimo.
Uma classe concreta que for subclasse desta classe abstrata implementa os passos do algoritimo específico para a subclasse.

​

### Exemplos de casos de uso do padrão Template Method

- Quando vários algoritimos ou classes implementam uma lógica semelhante ou idêntica
- Quando a implementação dos algoritimos em subclasses ajuda a reduzir a duplicação de código
- Quando vários algoritimos podem ser definidos ao deixar que as subclasses implementem o comportamento usando o recurso de subescrita

Outro exemplo simples é o compilador usado pelas linguagens de programação. Um compilador executa essencialmente duas tarefas:

- Reúne o código fonte
- Compila gerando um objeto-alvo

Desta forma se precisarmos definir um compilador para dispositivos iOS ou Android, podemos implementar isso com a ajuda do padrão Template Method. É assim que o padrão Template Method evita duplicação de código.

​

### Os principais objetivos do padrão Template Method

- Definir o esqueleto de um algoritimo com operações primitivas
- Redefinir determinadas operações na subclasse sem alterar a estrutura do algoritimo
- Reutilizar o código e evitar esforços duplicados
- Tirar proveito de interfaces ou implementações comuns

​

* * *

​

### Exemplo de Código

```python
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
```

​

* * *

​

### Hooks

No padrão Template Method, um hook (gancho) é um método declarado na classe abstrata, que em geral, recebe uma implementação default. A ideia por trás dos hooks é dar uma subclasse a capacidade de fazer um uso padrão do algoritimo sempre que for necessário.
Um exemplo de utilização de hooks seria, no caso da nossa implementação Agência de Viagens. Pense que poderíamos ter turistas mais idosos que talvez não queiram sair em todos os três dias da viagem, pois poderão se cansar facilmente. Neste caso, podemos desenvolver um hook que garantirá que o segundo dia seja mais leve, o que significa que o turista poderá ir a lugares próximos e retornar ao plano normal no segundo dia.

​

### Princípio Hollywood e o Template Method

O Princípio de Hollywood é um princípio de design de software que diz: *Não ligue para nós; nós ligaremos para você.*

No mundo da Oritentação a Objetos, permitimos que componentes de baixo nível se associem ao sistema usando o princípio de Hollywood. No entanto, os componentes de alto nível determinam como e quando os sistemas de baixo nível serão necessários, ou seja, os componentes de alto nível tratam os componentes de baixo nível assim: *Não ligue para nós; nós ligaremos para você.*

Isso se relaciona ao padrão Template Method no sentido de que é a classe abstrata de alto nível que organiza os passos para definir o algoritimo. Com base no algoritimo, as classes de baixo nível são solicitadas a definir a implementação concreta dos passos.

​

* * *

​

### Vantagens e Desvantagens do padrão Command

### - Vantagens

- Uma das principais vantagens é que não há duplicação de código
- A reutilização de código ocorre normalmente já que o padrão Template Method utiliza herança e não composição. Somente alguns métodos precisam ser sobrescritos.
- A flexibilidade permite que as subclasses decidam como implementar os passos do algoritimo.

### - Desvantagens

- Debugar a aplicação e compreender a sequência do fluxo no padrão Template Method às vezes pode ser confuso. Você pode acabar implementando um método que não deveria ser implementado ou deixando de implementar um método abstrato. Vale a pena documentar bem o código e realizar tratamento de erros para evitar problemas.
- A manutenção dos comportamentos de alto ou baixo nível pode causar problemas na implementação.

​

### Principais Dúvidas sobre o padrão Command

- D1 - Um componente de baixo nível deveria ser proibido de chamar um método em um componente de alto nível?
  - R1 - Não. Um componente de baixo nível pode chamar o componente de mais alto nível por meio de herança. No entant o programador deve garantir que não haja dependência circular, na qual os componentes de baixo nível e de alto nível sejam dependentes uns dos outros.
- D2 - O padrão Strategy (Estratégia) não é semelhante ao padrão Template Method?
  - R2 - Tanto o padrão Strategy quanto o padrão Template Method encapsulam algoritimos. O Template Method depende de herança, enquanto o Strategy usa composição. O padrão Template Method faz uso do algoritimo em tempo de compilação usando subclasses, enquanto o padrão Strategy faz uso em tempo de execução.
