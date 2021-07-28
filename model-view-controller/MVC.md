## 📝 Model-View-Controller (MVC)

** *Exemplos e conteúdos adptados e retirados do curso ["Padrões de Projeto (Design Patterns) com Python"](https://www.udemy.com/course/padroes-de-projeto-com-python)*

​

### Introdução

O padrão de projeto Model-View-Controller, ou MVC, é um padrão de software para implementar interfaces de usuário com uma arquitetura que pode ser facilmente modificada e mantida. Basicamente, o padrão MVC diz respeito à separação da aplicação em três partes básicas:

- Model (modelo)
- View (visão)
- Controller (controlador)

Estas três partes estão interconectadas e ajudam a separar os modos como a informação é representada da forma como ela é apresentada.

​

### Como funciona o padrão MVC?

- O **model** (modelo) representa os dados e a lógica de negócios (como a informação é armazenada e consultada).
- A **view** (visão) nada mais é que a representação (como ela é apresentada) dos dados.
- O **controller** (controlador) é a "cola" que une ambos, ou seja, é a parte que direciona o modelo e a visão para que se comportem de determinada maneira de acordo com as necessidades de um usuário.

É importante observar que a view e o controller são independentes do model, mas não o contrário. Isso ocorre porque um usuário está preocupado com os dados. Desta forma, podemos trabalhar com o model de forma independente, e este é o aspecto principal do padrão MVC.

As aplicações web são exemplos clássicos para o padrão MVC. Você clica em um botão, algumas operações ocorrem e você passa a ver o que desejava na página.
​

#### Como isso ocorre?

- Você é o usuário e interage com a view. A view é a pagina web apresentada. Você clica nos botões e ela informa ao controller o que deve ser feito.
- O controller obtém a entrada da view e a envia ao model. O model é manipulado com base nas ações do usuário.
- O controller também pode pedir à view para mudar conforme a ação recebida do usuário, por exemplo, alterar os botões, apresentar elementos adicionais na interface, etc...
- O model notifica a alteração de estado à view. Isso pode ser feito com base em alterações internas ou por acionamentos externos, como cliques em um botão.
- A view então exibe o estado que ela obtém diretamente do modelo.

​

### O padrão de projeto MVC trabalha com os seguintes termos

- Model - Declara uma classe para armazenar e manipular dados
- View - Declara uma classe para construir interfaces de usuário e fazer exibição de dados
- Controller - Declara uma classe que conecta o Model e a View

Temos ainda o usuário (cliente) que solicita determinados resultados com base em certas ações.

​

### Objetivos do padrão MVC

- Manter os dados e a sua apresentação separados
- Facilitar a manutenção das classes e de sua implementação
- Ter flexibilidade para mudar o modo como os dados são armazenados e exibidos; ambos são independentes e, portanto, tem flexibilidade para mudar

​

### Exemplo Básico de Código

```python
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
```

​

* * *

​

### Vantagens e Desvantagens do padrão MVC

### - Vantagens

- Usando o padrão MVC, os desenvolvedores podem separar a aplicação de software em três partes principais: o model, view e controller. Isso ajuda a simplificar a manutenção, garante um baixo acoplamento e reduz a complexidade
- O MVC permite alterações independentes no frontend com poucas mudanças, ou nenhuma, na lógica do backend; desde modo, os esforços de desenvolvimento podem correr de forma independente
- Os models ou a lógica de negócios podem ser alterados sem qualquer mudança na view
- O controller pode ser alterado sem qualquer impacto na view ou model
- Este padrão ajuda na contratação de pessoas com capacidades específicas, por exemplo, engenheiros especializados em plataformas de UI (User Interface) ou UX (User Experience) que poderão trabalhar de forma independente em suas área de especialização

### - Desvantagens

- No início, pode ser confuso entender como separar a lógica da aplicação entre o model e o controller ou view
- Alguns frameworks utilizam nomenclaturas diferentes para o mesmo conceito
- Alguns frameworks criam uma estrutura complexa desnecessária deixando o projeto "grande" desde o início

### Principais Dúvidas sobre o padrão MVC

- D1 - O MVC não é um padrão? Por que ele é chamado de padrão composto?
  - R1 - Os padrões compostos são essencialmente grupos de padrões reunidos para resolver problemas maiores de design no desenvolvimento de software. O MVC é o padrão composto mais popular e mais amplamente utilizado. Por ser tão usado e ser  extremamente confiável, ele é tratado por si só como um padrão
- D2 - O MVC é usado somente para aplicações web?
  - R2 - Não. Uma aplicação web é o melhor exemplo para descrever o padrão MVC. No entanto este padrão pode ser usado em várias áreas, como aplicações desktop, mobile, etc..
- D3 - Várias views podem trabalhar com vários models?
  - R3 - Sim, com frequência você acabará em uma situação que os dados precisam ser agrupados a partir de vários models e apresentados em uma única ou em múltiplas views.