## 📝 Observer

** *Exemplos e conteúdos adptados e retirados do curso ["Padrões de Projeto (Design Patterns) com Python"](https://www.udemy.com/course/padroes-de-projeto-com-python)*

​

### Introdução

No padrão de projeto Observer um objeto mantém uma lista de dependentees de modo que este objeto possa notificar todos os dependentes acerca de mudanças pelas quais ele passa usando qualquer um dos meodos definidos pelo objeto.
No mundo das aplicações distrbuídas, vários serviços interagem uns com os outros para executar uma operação mais complexa que o usuário queira fazer.
Os serviços podem realzar várias operações, mas a operação que eles executam é diretamente ou altamente dependente do estado dos objetos do serviço com o qual a interação ocorre.

​

### Contextualizando o padrão Observer

Imagine um blog onde diversas pessoas postam diariamente diversos textos em tópicos diversos. Pessoas, como eu ou você, podem se cadastrar no blog e se inscrever em determinados tópicos.
Quando um novo post for realizado sobre o tópico na qual você está inscrito você receberá uma notificação informando a nova postagem. Por baixo dos panos, temos neste sistema o padrão Observer sendo utilizado.
Neste nosso exemplo, o blog será o Objeto que mantém uma lista de dependentes (inscritos) e a qualquer mudança serão notificados pois os inscritos estão "observando" as mudanças no objeto observado.

​

### Principais objetivos do padrão Observer

- Define uma dependência de um-para-muitos (one-to-many) entre os objetos, de modo que qualquer muudança em um objeto será notificada aos demais objetos dependentes automaticamente
- Encapsula o componente "objeto"

### Casos de uso do padrão Observer

- Na implementação de um serviço de eventos em sistemas distribuídos
- Na implementação de um sistema de notícias
- No mercado de ações

​

* * *

​

### Exemplo

```python
from abc import ABCMeta, abstractmethod


# Assunto/Tópico
class AgenciaNoticias:

    def __init__(self):
        self.__inscritos = []
        self.__ultima_noticia = None

    def inscrever(self, inscrito):
        self.__inscritos.append(inscrito)

    def desinscrever(self, inscrito=None):
        if not inscrito:
            return self.__inscritos.pop()
        return self.__inscritos.remove(inscrito)

    def notificar_todos(self):
        [inscrito.notificar() for inscrito in self.__inscritos]

    def adicionar_noticia(self, noticia):
        self.__ultima_noticia = noticia

    def mostrar_noticia(self):
        return f'Urgente: {self.__ultima_noticia}'

    def inscritos(self):
        return [type(valor).__name__ for valor in self.__inscritos]


# Interface Observer
class TipoInscricao(metaclass=ABCMeta):

    @abstractmethod
    def notificar(self):
        pass


# Observador A
class InscritosSMS(TipoInscricao):

    def __init__(self, agencia_noticia):
        self.agencia_noticia = agencia_noticia
        self.agencia_noticia.inscrever(self)

    def notificar(self):
        print(f'{type(self).__name__} {self.agencia_noticia.mostrar_noticia()}')


# Observador B
class InscritosEmail(TipoInscricao):

    def __init__(self, agencia_noticia):
        self.agencia_noticia = agencia_noticia
        self.agencia_noticia.inscrever(self)

    def notificar(self):
        print(f'{type(self).__name__} {self.agencia_noticia.mostrar_noticia()}')


# Observador N
class InscritosOutroMeio(TipoInscricao):

    def __init__(self, agencia_noticias):
        self.agencia_noticias = agencia_noticias
        self.agencia_noticias.inscrever(self)

    def notificar(self):
        print(f'{type(self).__name__} {self.agencia_noticias.mostrar_noticia()}')


# Cliente
if __name__ == '__main__':
    agencia_noticias = AgenciaNoticias()

    InscritosSMS(agencia_noticias)
    InscritosEmail(agencia_noticias)
    InscritosOutroMeio(agencia_noticias)

    print(f'Inscritos: {agencia_noticias.inscritos()}')

    agencia_noticias.adicionar_noticia('Novo conteúdo sendo aprendido.')
    agencia_noticias.notificar_todos()

    print(f'Descadastrado: {type(agencia_noticias.desinscrever()).__name__}')
    print(f'Inscritos: {agencia_noticias.inscritos()}')

    agencia_noticias.adicionar_noticia('Design Patterns em Python!')
    agencia_noticias.notificar_todos()

```

​

* * *

​

### Modelos do padrão Observer

- Modelo Pull - O padrão Observer desempenha um papel ativo na seguinte forma:
  - O assunto/tópico faz um broadcast (espalhamento) para todos os inscritos registrados quando há uma mudança
  - O observador é responsável por obter as mudanças, ou seja, o assinante deve buscar os dados quando houver alteração
  - O modelo pull não é eficiente, pos envolve dois passos, sendo o primeiro passo para o assunto/tópico notificar o observador e o segundo passo para o observador obter os dados necessários do assunto/tópico
- Modelo Push - No modelo push, o assunto/tópico é quem desempenha um papel dominante, conforme:
  - De modo diferente do modelo pull, as mudanças são enviadas pelo assunto/tópico ao observador
  - Neste modelo, o assunto/tópico pode enviar informações detalhadas ao observador (mesmo que não seja necessário). Isso pode resultar em tempos de resposta mais lentos quando uma grande quantidade de dados é enviada pelo assunto/tópico, mas não é realmente usada pelo observador
  - Somente os dados necessários devem ser enviados pelo assunto/tópico para que o desempenho seja melhor

​

* * *

​

### Baixo acoplamento e o padrão Observer

Em Programação Orientada a Objetos, o Baixo Acoplamento é um princípio de design de software importante e que deve ser usado em aplicações. O propósito principal deste princípio é esforcar-se para ter designs com baixo acoplamento, ou seja, baixa dependência, entre objetos que interagem uns com os outros.
O acoplamento refere-se ao grau de conhecimento que um objeto tem sobre outro com o qual interage. Designs com baixo acoplamento nos permitem construir sistemas orientados aobjetos flexíveis, capazes de lidar com mudanças, pois reduzem a dependência entre vários objetos.

A arquitetura com baixo acoplamento garante as seguintes características:

- Reduz o risco de que uma mudança em um elemento possa gerar impacto imprevisto em outros elementos
- Simplifica os testes, a manutenção e a resolução de problemas
- O sistema pode ser facilmente separado em elementos definidos

O padrão Observer possibilita um design de objetos em que o Assunto/Tópico e o Observador tenham baixo acoplamento pois:

- A única informação que o Assunto/Tópico deve ter sobre o Observador é que ele implementa uma determinada interface. Ele não precisa conhecer as classes dos observadores.
- Qualquer novo observador poderá ser adicionado a qualquer momento
- O Assunto/Tópico não precisa ser nem um pouco modificado para adicionar qualquer novo observador
- O Assunto/Tópico ou os Observadores não estão "amarrados" e podem ser usados de modo independente. Desta forma, o observador poderá ser reutilizado em qualquer outro lugar caso necessário
- Alterações no Assunto/Tópico ou no Observador não afetarão um ao outro. Como ambos são independentes, isto é, tem baixo acoplamento, eles são livres para fazer suas próprias alterações

​

* * *

​

### Vantagens e Desvantagens do padrão Observer

### - Vantagens

- Oferece suporte para o princípio do baixo acoplamento entre objetos que interajam uns com os outros
- Permite enviar dados a outros objetos de modo eficiente, sem qualquer mudança nas classes Assunto/Tópico ou Observer
- Os Observers podem ser adicionados/removidos a qualquer momento

### - Desvantagens

- A interface Observer deve ser implementada pelos Observers, o que envolve herança. Não há opção para usar composição, pois a inteface Observer não pode ser instanciada
- Se não for implementado corretamente, o Observer pode acrescentar complexidade e levar a problemas imprevistos de desempenho
- Em uma aplicação de software, às vezes, as notificações podem não ser confiáveis e resultar em condições de concorrência (race conditions) ou inconsistência

​

* * *

​

### Principais Dúvidas sobre o padrão Facade

- D1 - É possível havar vários Assuntos/Tópicos e Observers?
  - R1 - Sim. É possível que haja alguma situação em que tenhamos vários Assuntos/Tópicos e Observers. Para que tudo funcione normalmente, os Observers devem ser notificados das mudanças nos Assuntos/Tópicos que estão inscritos.
- D2 - Quem é responsável por disparar a atualização/notificação?
  - R2 - Estudamos nesta seção que o padrão Observer pode trabalhar tanto com o Modelo Pull ou com o Modelo Push. Geralmente, o Assunto/Tópico dispoara o método de atualização/notificação quando há mudanças; ás vezes, porém, conforme as necessidades da aplicação, o Observer também pode disparar notificações. Entretanto é preciso ter cuidado para que a frequência não seja muito alta; caso contrário, isso poderá resultar na degradação do desempenho, especialmente quando as atualizações para o Assunto/Tópico forem menos frequentes.
- D3 - O Assunto/Tópico ou o Observer podem ser usados para acesso em qualquer outro caso de uso?
  - R3 - Sim, esta é a eficácia do baixo acoplamento manifestada diretamente no padrão Observer. Ambos, Assunto/Tópico e Observer, podem ser usados de forma indepentende.
