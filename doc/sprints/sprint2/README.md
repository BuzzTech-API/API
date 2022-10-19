# Sprint 2 - Banco de Dados & Layout
<p align="center">
      <img src="/doc/frontend/logo-BuzzTech.png" alt="logo da Buzz Tech" width="200">
      <h2 align="center"> Buzz Tech</h2>




<hr>
<br>
<p align="center">
  <a href ="#backlog"> Backlog da Sprint </a>  | 
  <a href ="#burndown"> Burndown </a>  |
  <a href ="#evolução"> Evolução do Backlog </a>  |
  <a href ="#hitoria"> Histórias de Usuários </a>
</p>



</p>



<br>

<h4 align="center">
 <a href="https://docs.python.org/3/"><img src = "https://img.shields.io/badge/python-3670A0?style=for-the-badge&logo=python&logoColor=ffdd54"/></a>
 <a href="https://www.w3schools.com/tags/tag_doctype.asp"><img src = "https://img.shields.io/badge/html5-%23E34F26.svg?style=for-the-badge&logo=html5&logoColor=white"/></a>
 <a href="https://www.w3schools.com/css/"><img src = "https://img.shields.io/badge/css3-%231572B6.svg?style=for-the-badge&logo=css3&logoColor=white"/></a>
 <a href="https://getbootstrap.com/docs/4.1/getting-started/introduction/"><img src = "https://img.shields.io/badge/bootstrap-%23563D7C.svg?style=for-the-badge&logo=bootstrap&logoColor=white"/></a>
 <a href="https://flask.palletsprojects.com/en/2.2.x/"><img src = "https://img.shields.io/badge/flask-%23000.svg?style=for-the-badge&logo=flask&logoColor=white"/></a>
 <a href="https://docs.github.com/pt"><img src = "https://img.shields.io/badge/github-%23121011.svg?style=for-the-badge&logo=github&logoColor=white"/></a>
 <a href="https://dev.mysql.com/doc/"><img src = "https://img.shields.io/badge/mysql-%2300f.svg?style=for-the-badge&logo=mysql&logoColor=white"/></a>
</h4>



<br>

> Status da Sprint: Concluída :heavy_check_mark:

<br>

Na segunda sprint buscou-se aprimorar o produto através da criação e consolidação de um banco de dados relacional utilizando-se MySQL e Flask-SQLAlchemy. Para atingir um maior valor do produto, foram adicionadas diversas funcionalidades no produto na perspectiva da utilização do técnico. A versão sintética e funcional do um sistema foi acrescida primeiro da modelagem de um banco de dados relacional com duas entidades, relacionando as Ordens de Serviço aos  Usuários cadastrados, ou seja, os técnicos que atenderão cada ordem. Através dessa atualização, o técnico será cadastrados com usuário e senha e terá uma visão diferenciada dos chamados, podendo atualizar e deletar os registros de ordens de serviço criados no banco de dados.

Outra mudança que vale destacar é a implementação e atualização de soluções visuais que visam facilitar a utilização do sistema pelos usuários que desejarem abrir uma ordem de serviço de reclamação de problemas. O wireframe foi pensando para criar um uso mais fluido e intuitivo para os usuários. Para isso, foram utilizados  ícones, paletas de cores, bem como botões para preenchimento de algumas informações, ao invés dos formulários por escrito.

Para visualizar o *Wireframe* em PDF, acesse o [link :link:](img/wireframe.pdf).

### :bust_in_silhouette: Cadastro do técnico

![Cadastro do técnico](img/teste/gif/cadastrar.gif)

### :telephone_receiver: Abertura de chamado

![Abertura de chamado](img/teste/gif/chamado.gif)

### 	:eyes: Visualização do chamado

![Visualização de chamados](img/teste/gif/visualizar.gif)



<br>

##  :date: Backlog da Sprint<a id="backlog"></a>



|                            Tarefa                            |                          Descrição                           |  Histórias de Usuários   | Prioridade | Sprint | Estimativa de Esforço |       Status       |
| :----------------------------------------------------------: | :----------------------------------------------------------: | :----------------------: | :--------: | :----: | :-------------------: | :----------------: |
|               Levantamento dos tipos de danos                | Listagem dos hardware integrantes das máquinas dos laboratórios passíveis de erros e má funcionamento . | <a href='#us07'>US07</a> |   Baixa    |   2    |          3h           | :white_check_mark: |
| Inserção dos principais tipos de danos de hardware no sistema | Inserção dos principais tipos de danos no sistema contendo os problemas de hardware com maior probabilidade de ocorrência. | <a href='#us07'>US07</a> |    Alta    |   2    |          9h           | :white_check_mark: |
|      Criação da Modelagem Conceitual do Banco de Dados       | Criação da Modelagem Conceitual através da descrição de como os dados serão armazenados no banco e também seus relacionamentos. | <a href='#us08'>US08</a> |    Alta    |   2    |          8h           | :white_check_mark: |
| Criação do Esquema Conceitual através do Diagrama Estrutural de Entidade Relacional (DEER) | Criação de um modelo de mais alto nível, ou seja, que esta mais próximo da realidade dos usuários. Esse modelo pode é elaborado por meio Diagrama Estrutural de Entidade e Relacionamento (DEER). | <a href='#us08'>US08</a> |    Alta    |   2    |          1h           | :white_check_mark: |
|                Criação do Banco de Dados SQL                 | Criação do Banco de Dados relacional e funcional baseado na modelagem e no esquema aprovados. | <a href='#us20'>US20</a> |    Alta    |   2    |          13h          | :white_check_mark: |
|     Funções de ligação da aplicação com o banco de dados     | Criação de funções em Python que levem os dados preenchidos pelos usuários nos campos de abertura de chamado até o banco de dados, e assim salvem esses dados de uma maneira persistida. | <a href='#us21'>US21</a> |    Alta    |   2    |          12h          | :white_check_mark: |
|                  Criação da área do Técnico                  | Criar uma área para o técnico administrar esses chamados recebidos com a entrada em ordem cronológica | <a href='#us09'>US09</a> |    Alta    |   2    |          12h          | :white_check_mark: |
| Login simplificado para o técnico e diferenciação da interface dependendo de  quem está utilizando | Possibilidade de criar usuários para o sistema de ordem de serviço para que os técnicos tenham uma maneira segura e privada de visualizar, deletar, procurar, filtrar e atualizar os chamados criados pelos usuários. | <a href='#us09'>US09</a> |    Alta    |   2    |          9h           | :white_check_mark: |
|               Implementar facilitações visuais               | Utilização de cores, ícones e outras soluções gráficas que facilitem o entendimento das informações dos sistemas para os usuários que desejem utilizá-lo. | <a href='#us17'>US17</a> |   Baixa    |   2    |          3h           | :white_check_mark: |



<br>

## :fire: Burndown<a id='burndown'></a>

![Burndown](img/burndown.png)



<br>

## :hatching_chick: Evolução do Backolog<a id='evolução'></a>

Como a metodologia ágil Scrum tem como princípios a adaptabilidade e o processo iteraitvo, mudanças ocorrem para que o produto chegue ao final da Sprint com o maior valor possível. Para isto, foram necessárias alterações de tarefas que geraram 4 atualizações de versão do Backlog do Produto:

|              **Backlog 3.0** <br>10% █▒▒▒▒▒▒▒▒▒              |
| :----------------------------------------------------------: |
|          Levantamento e listagem dos tipos de danos          |
|      Criação da Modelagem Conceitual do Banco de Dados       |
| Criação do Esquema Conceitual através do Diagrama Estrutural de Entidade Relacionamento (DEER) |
|             Início da Criação do Banco de Dados              |
| Criação da área do Técnico para diferenciar a interface dependendo de quem está utilizando |

|               Backlog 3.22<br>99% ██████████]                |
| :----------------------------------------------------------: |
|          Levantamento e listagem dos tipos de danos          |
| Inserção dos principais tipos de danos no sistema em lista hardware, software, rede |
|      Criação da Modelagem Conceitual do Banco de Dados       |
| Criação do Esquema Conceitual através do Diagrama Estrutural de Entidade Relacional (DEER) |
|                Criação do Banco de Dados SQL                 |
|     Funções de ligação da aplicação com o banco de dados     |
|                  Criação da área do Técnico                  |
| Login simplista para o técnico com diferenciação da interface dependendo de  quem está utilizando |
| Implementar algumas facilitações visuais (hard, software, rede, mouse, monitor etc) |

<br>

## :key: Histórias de Usuário<a id="historia"></a>



|          ID           |                     História de Usuário                      |
| :-------------------: | :----------------------------------------------------------: |
| US07<a id='us07'></a> | Como profissional de outra geração, Andréia pode ter dificuldades para relatar o problema em sua máquina, ela quer uma lista dos principais possíveis problemas para facilitar seu relato na solicitação. |
| US08<a id='us08'></a> | Pedro precisa de um ambiente com sistema integrado para que seja melhor e confiável a administração das tarefas |
| US09<a id='us09'></a> | Pedro necessita de uma área de acesso único para que ele visualize os pedidos de assistência e entenda sua propriedade, sem outros usuários vejam ou interferirem no fechamento dos chamados. |
| US17<a id='us04'></a> | Por ser mais velha, Andréia pode ter dificuldade de entender o que está escrito ou mesmo ao que se refere cada parte da solicitação de informações. Por isso, deverá ser criada identificações visuais, facilitando a comunicação e entendimento do usuário. |
| US20<a id='us20'></a> | Pedro precisa de um ambiente o qual os dados das ordens de serviço fiquem armazenados mesmo depois que sua sessão acabar. |
| US21<a id='us21'></a> | Pedro precisa de uma maneira de conectar o sistema web ao o banco de dados e, a partir dessa conexão, poder inserir, deletar, procurar, filtrar e atualizar os dados registrados nesse banco de dados. |
