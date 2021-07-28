## 📝 Antipadrões

** *Exemplos e conteúdos adptados e retirados do curso ["Padrões de Projeto (Design Patterns) com Python"](https://www.udemy.com/course/padroes-de-projeto-com-python)*

​

### Introdução

Os princípios de design de software apresentam um conjunto de regras ou diretrizes que ajudam os desenvolvedores a tomar decisões no nível de design.
Existem quatro características em um design de software ruim:

- **Imóvel** - Uma aplicação é desenvolvida de modo que se torne muito difícil de ser reutilizada
- **Rígido** - Uma aplicação é desenvolvida de modo que qualquer alteração pequena possa resultar na mudança de muitas partes de software
- **Frágil** - Qualquer mudança na aplicação atual resulta em falhas no sistema existente com muita facilidade
- **Viscoso** - Mudanças são feitas pelo desenvolvedor no código ou no próprio ambiente para evitar mudanças difíceis no nível da arquitetura

Estas características, se forem aplicadas, resultam em soluções que não deveriam ser implementadas na arquitetura ou no desenvolvimento de software.
Um **antipadrão** é o resultado de uma solução ineficiente e contraproducente para problemas recorrentes.

Imagine que você está desenvolvendo um software e se depare com um problema de design. Você decide então solucionar este problema. Porém, o que acontece se a solução tiver um impacto negativo no design e causar qualquer problema de desempenho na aplicação?
Os **antipadrões** são processos e implementações defeituosas e comuns em aplicações de software.

#### Os antipadrões podem ser resultado de:

- Um desenvolvedor que desconhece boas práticas de desenvolvimento de software
- Um desenvolvedor que não aplica os padrões de projeto de forma correta

Os antipadrões, apesar de tudo, podem se mostrar vantajosos pois:

- Nos ajudam a reconhecer problemas recorrentes no mercado de software e buscar soluções detalhadas para a maioria destes problemas, fazendo bom uso dos padrões de projeto
- Nos ajudam a pensar em ferramentas para reconhecer os problemas e determinar suas causas
- Nos ajudam a descrever as medidas que podem ser tomadas em vários níveis para melhorar a aplicação e a arquitetura

Os antipadrões, podem ser classificados em duas categorias principais:

- **Antipadrões** no desenvolvimento de software
- **Antipadrões** na arquitetura de software

​

### Antipadrão no Desenvolvimento de Software

Quando damos início ao desenvolvimento de software em uma aplicação ou projeto, pensamos na estrutura do código. Esta estrutura é consistente com a arquitetura do projeto, o design, os casos de uso do cliente e muitas outras considerações de desenvolvimento.
Com frequência, enquanto o software é desenvolvido, ele se desvia da estrutura de código original por alguns dos motivos:

- O processo de raciocínio do desenvolvedor evolui com o desenvolvimento
- Os casos de uso tendem a mudar com base no feedback dos clientes
- As estruturas de dados projetadas inicialmente podem passar por mudanças de acordo com as considerações de funcionalidade ou de escalabilidade

Pelos motivos apresentados, o software com frequência passa por refatorações. A refatoração tem uma conotação negativa para muitas pessoas; na verdade, porém, ela é uma das partes mais relevantes na jornada do desenvolvimento de software, oferecendo uma oportunidade aos desenvolvedores de revisar as estruturas de dados e pensar na escalabilidade e nas necessidades sempre em evolução dos clientes e sistemas.

São vários os antipadrões observados no desenvolvimento de software, dentre eles:

- Código Espaguete (Macarrônico)
- Martelo de Ouro
- Fluxo de Lava
- CTRL + C / CTRL + V

​

### Código Espaguete

Este é o antipadrão mais comum e mais conhecido no desenvolvimento de software. O código espaguete é difícil de manter e de otimizar.

As causas típicas do código espaguete incluem:

- Desconhecimento de programação e análise orientada a objetos
- A arquitetura ou o design do produto não são considerados
- A mentalidade do desenvolvedor é voltada à correções rápidas

Você saberá que tem um código espaguete em mãos quando os seguintes pontos forem verdadeiros:

- Somente uma reutilização mínima das estrutuas é possível
- Os esforços de manutenção são muito altos
- A capacidade de extensão e flexibilidade para mudar são reduzidas

​

### Martelo de Ouro

No desenvolvimento de software, você deve ter visto váriso exemplos (ou poderá ver) em que uma dada solução (tecnologia, design ou módulo) é usada em muitos lugares porque esta solução traria vantagens a diversos projetos, funcionando quase como uma *bala de prata*.
Felizmente, você aprendeu que uma solução é mais adequada em um determinado contexto e é aplicada a determinados tipos de problema. No entanto, as equipes de desenvolvimento de software tendem a optar por uma solução comprovada sem considerar se ela é apropriada às reais necessidades.
Este é o motivo pelo qual este antipadrão é conhecido como Martelo de Ouro, um martelo para todos os pregos possíveis (ou uma solução para todos os problemas).

As causas típicas do Martelo de Ouro, incluem:

- A solução chega como uma recomendação vinda de cima (de arquitetos ou líderes de tecnologia), de pessoas que não estão próximas ao problema específico em mãos
- Uma solução gerou muitos benefícios no passado, mas em projetos com um contexto e requisitos diferentes
- Uma empresa está presa a essa tecnologia, pois investiu dinheiro em treinamento dos funcionários ou estes se sentem mais confortáveis com ela

As consequências do Martelo de Ouro, incluem:

- Uma solução é obsessivamente aplicada a todos os projetos de software
- O produto é descrito não pelo seus recursos, mas pela tecnologia usada no desenvolvimento
- Nos corredores da empresa, você ouve os desenvolvedores dizendo que "aquilo poderia ter sido melhor do que isso"
- Os requisitos não são concluídos e não estão em sincronia com as expectativas dos usuários

​

### Fluxo de Lava

Este padrão está relacionado ao Código Morto (Dead Code), isto é, um trecho de código inutilizável, que permanece na aplicação de software por medo de que ele cause falhas em outros lugares caso seja modificado. Á medida que o tempo passa, este trecho de código continua no softwware e solidifica a sua posição, como se fosse lava se transformando em rocha sólida.
Pode ocorrer nos casos em que começarmos a desenvolver um software para dar suporte a determinado caso de uso, mas este muda com o tempo.

As causas de um Fluxo de Lava (Lava Flow) incluem:

- Muito código de tentativa e erro na produção
- Código escrito por uma só pessoa, que não é revisado e é passado para outras equipes de desenvolvimento sem qualquer treinamento sobre este código
- O raciocínio inicial usado na arquitetura ou no design de software é implementado na base de código, mas ninguém mais o entende

O sintomas de um Fluxo de Lava são:

- Baixa cobertura de código para testes desenvolvidos (se é que existem testes)
- Muitas ocorrências de código comentado sem motivo, ou pior ainda, código sem comentário
- Interfaces obsoletas ou desenvolvedores tentando contornar código existente

​

### CTRL + C / CTRL + V

Este é o principal antipadrão, desenvolvedores experientes disponibilizam trechos de códigos online, seja no Github, seja no StackOverflow, que são soluções para alguns problemas que ocorrem comumente. Com frequência, os desenvolvedores copiam estes códigos exatamente como estão e os usam em suas aplicações para avançar no desenvolvimento.
Neste caso, não há nehuma validação para saber se esse é o código mais otimizado ou se ele é realmente apropriado ao contexto. isso resulta em uma aplicação de software sem flexibilidade e de difícil manutenção.

As causas de uma programação do tipo "CTRL + C / CTRL + V" são:

- Desenvolvedores iniciantes não acostumados a escrever código ou que não saibam como desenvolver
- Correção de bug ou avanços rápidos no desenvolvimento
- Duplicação de código por necessidade de uma estrutura de código ou de uma padronização entre os módulos
- Falta de pensamento em longo prazo ou planejamento antecipado

As consequências de uma programação do tipo "CTRL + C / CTRL + V" são:

- Tipos de problemas semelhantes entre aplicações de software
- Custos mais altos de manutenção e ciclo de vida mais longos para bugs
- Base de código menos modular, com o mesmo código executado em várias linhas
- Problemas de herança que ja existam antes

​

### Antipadrão no Arquitetura de Software

A arquitetura de software é uma parte importante da arquitetura de sistemas em geral. Enquanto a arquitetura de sistemas tem como foco aspectos como o design, ferramentas e hardware, entre outros, a arquitetura de software está voltada para a modelagem do software, que deve ser bem compreendida pelas equipes de desenvolvimento e de testes, por gerentes de produtos e outros stakeholders (pessoas-chave).
Esta arquitetura desempenha um papel crucial para determinar o sucesso da implementação e no modo como o produto funcionará para os clientes.
​

### Reinventando a Roda

Com frequência, ouvimos os líderes de tecnologia falarem de não reinventar a roda. O que isso quer dizer essencialmente?
Para alguns, pode significar a reutilização de arquitetura. Por exemplo, você resolveu um problema e concebeu uma solução no nível de arquitetura. Se voce se deparar com um problema semelhante em qualquer outra aplicação, o processo de racioncínio (arquitetura ou design) desenvolvido anteriormente deve ser reutilizado.
Ou seja, não há motivos para rever o mesmo problema e conceber uma nova solução, o que, essencialmente significa reinventar a roda.

Causas que levam à reinvenção da roda:

- Ausência de uma documentação ou de um repositório central que discutam problemas no nível de arquitetura e soluções implementadas
- Falta de comunicação entre líderes de tecnologia na comunidade ou na empresa
- Construir do zero é o processo seguido pela empresa; basicamente, há processos imaturos, sem uma sólida implementação e aderência ao processo

As consequências deste antipadrão incluem:

- Soluções em demasia para resolver um problema-padrão, com muitas delas não tendo a atenção merecida
- Mais tempo e utilização de recursos para a equipe de engenharia, resultando em estouros no orçamento e mais tempo para alcançar o mercado
- Uma arquitetura de sistema fechada (a arquitetura é útil apenas para um produto), duplicação de esforços e gerenciamento de riscos precário

​

### Vendor Lock-in (Dependência de Fornecedor)

Como o nome deste antipadrão sugere, as empresas de produto tendem a ser dependentes de algumas tecnologias oferecidas pelos fornecedores. Essas tecnologias estão muitos amarradas a seus sistemas, a ponto de ser díficil afastar-se delas.

Causas de um Vendor Lock-in:

- Familiaridade com as pessoas que tem autoridade na empresa fornecedora e possíveis descontos na compra da tecnologia
- Tecnologia escolhida com base em ofertas de marketing de vendas, e não na avaliação da tecnologia
- Uso de uma tecnologia comprovada, indicando que o retorno sobre os investimentos com essa tecnologia realmente foram elevados na experiência anterior, no projeto atual, mesmo quando ela não é apropriada para as necessidades ou os requisitos do projeto
- Especialistas em tecnologias/desenvolvedores já estão treinados para usar essa tecnologia

Consequências de um Vendor Lock-in:

- Ciclos de lançamento e de manutenção do projeto de uma empresa são diretamente dependentes do ciclo de lançamentos do fornecedor
- O produto é desenvolvido em torno da tecnologia, e não com base nos requisitos do cliente
- O tempo para o produto alcançar o mercado não é confiável e não atende às expectativas do cliente

​

### Design by Committee (Design por Comitê)

As vezes com base no processo de uma organização, um grupo de pessoas se reúne e faz o design de um sistema em particular. A arquitetura de software resultante muitas vezes é complexa ou fica abaixo do padrão, pois envolve muitos processos de racioncínio, e os especialistas em tecnologia, que podem não ter o conjunto de habilidades adequado nem a experiência para fazer o design dos produtos, impõem suas ideias.

Causas do Design por Comitê:

- O processo da empresa envolve a aprovação da arquitetura ou do design por muitos stakeholders
- Não há nenhum ponto de contato ou arquiteto único responsável pelo design
- As prioridades do design são definidas pelo marketing ou por especialistas em tecnologia, e não pelo feedback do cliente

Sintomas observados neste antipadrão:

- Pontos de vista conflitantes entre desenvolvedores e arquitetos, mesmo após o design ter sido concluído
- Design excessivamente complexo, muito difícil de ser documentado
- Qualquer mudança na especificação ou no design passa por revisão de muitas pessoas, resultando em atrasos na implementação
