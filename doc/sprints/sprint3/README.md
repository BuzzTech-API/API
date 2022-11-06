# Sprint 3 - Layout Editável
<p align="center">
      <img src="/doc/frontend/logo-BuzzTech.png" alt="logo da Buzz Tech" width="200">
      <h2 align="center"> Buzz Tech</h2>




<hr>
<br>
<p align="center">
  <a href ="#backlog"> Backlog da Sprint </a>  | 
  <a href ="#tarefas"> Tarefas </a>  | 
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
 <a href="https://developer.mozilla.org/pt-BR/docs/Web/JavaScript"><img src = "https://img.shields.io/badge/javascript-%23323330.svg?style=for-the-badge&logo=javascript&logoColor=%23F7DF1E"/></a>
 <a href="https://getbootstrap.com/docs/4.1/getting-started/introduction/"><img src = "https://img.shields.io/badge/bootstrap-%23563D7C.svg?style=for-the-badge&logo=bootstrap&logoColor=white"/></a>
 <a href="https://flask.palletsprojects.com/en/2.2.x/"><img src = "https://img.shields.io/badge/flask-%23000.svg?style=for-the-badge&logo=flask&logoColor=white"/></a>
 <a href="https://docs.github.com/pt"><img src = "https://img.shields.io/badge/github-%23121011.svg?style=for-the-badge&logo=github&logoColor=white"/></a>
 <a href="https://dev.mysql.com/doc/"><img src = "https://img.shields.io/badge/mysql-%2300f.svg?style=for-the-badge&logo=mysql&logoColor=white"/></a>
</h4>




<br>

> Status da Sprint: Concluída :heavy_check_mark:

<br>

Para a terceira sprint o foco foi tornar o layout dos laboratórios editável, um dos requisitos mínimos para a entrega do produto. Foi utilizado JavaScript como a linguagem base para tornar o front end dinâmico e, assim, possibilitar que o técnico, quando logado, possa adicionar computadores, mesas, portas, quadros brancos e servidores. Além disso, é possível editar o nome dos computadores e alterar tamanho, posição e rotação de todos os objetos da sala. Todas essas funções são armazenadas no banco de dados, dando segurança ao técnico que suas alterações serão mantidas, além de dar a possibilidade de fazer essas alterações de qualquer computador com acesso à internet.



### 	:wrench: Layout editável

<img src="img/teste/layout editável.gif" alt="layout editável dos laboratórios" style="zoom: 150%;" />



### :microscope: Layout dos laboratórios

<img src="img/teste/layout dos labs.gif" alt="layout dos laboratórios" style="zoom: 150%;" />



### 	:electric_plug: Componentes editáveis

<img src="img/teste/componentes editáveis.gif" alt="edição de características dos computadores" style="zoom: 150%;" />



### :calling: Confirmação de chamado enviado

<img src="img/teste/confirmação de envio.gif" alt="confirmação de envio do chamado" style="zoom: 150%;" />



<br>

##  :date: Backlog da Sprint<a id="backlog"></a>



|                            Tarefa                            |                          Descrição                           |               Histórias de Usuários                | Prioridade | Sprint | Estimativa de Esforço |       Status       |
| :----------------------------------------------------------: | :----------------------------------------------------------: | :------------------------------------------------: | :--------: | :----: | :-------------------: | :----------------: |
|  <a href='#enviada'>Confirmação  de solicitação enviada</a>  | Sinalizar  ao usuário solicitante da abertura do chamado quando esse chamado tiver sido  recebido pelo sistema. |              <a href='#us12'>US12</a>              |    Alta    |   3    |          7h           | :white_check_mark: |
| <a href='#CriacaoLayout'>Criação  do layout de todos os laboratórios</a> | Implementação  de todos layouts dos laboratórios utilizando o levantamento feito em sprints anteriores. | <a href='#us13'>US13</a>, <a href='#us14'>US14</a> |    Alta    |   3    |          20h          | :white_check_mark: |
| <a href='#LayoutEditavel'>Tornar  o layout dos laboratórios editável</a> | Fazer  com que o layout do laboratório possa ser editável em relação ao design e  disposição de todos os itens: computadores, mesa, servidores e lousa. | <a href='#us15'>US15</a>, <a href='#us22'>US22</a> |    Alta    |   3    |          13h          | :white_check_mark: |
| <a href='#EditarMaquinas'>Possibilitar a edição das características das máquinas</a> | Possibilitar que detalhes do computador sejam alterados e armazenados: processador, RAM e sistema operacional. |              <a href='#us23'>US23</a>              |    Alta    |   3    |          10h          | :white_check_mark: |
| <a href='#ConectarBanco'>Conectar o Banco de Dados com o layout do laboratório e informações das máquinas</a> | Criar funções para que o banco de dados consulte e persista o que o técnico salvar durante as edições de layout do laboratório, bem como as alterações das carecterísticas dos computadores. |              <a href='#us10'>US10</a>              |    Alta    |   3    |          20h          | :white_check_mark: |

<br>

## :checkered_flag: Tarefas<a id="tarefas"></a>



1. ### Confirmação  de solicitação enviada<a id='enviada'></a>

   Sinalizar  ao usuário solicitante da abertura do chamado quando esse chamado tiver sido  recebido pelo sistema para melhorar compreensão de finalização do processo e diálogo com o usuário. Assim, criou-se uma rota que redireciona o usuário a uma página com uma mensagem de confirmação de envio e agradecimento quando a ordem de serviço é efetivada.

   

   <img src="img/confirmação de envio.jpg" alt="confirmação de envio do chamado" style="zoom: 150%;" />

   

2. ### Criação  do layout de todos os laboratório<a id='CriacaoLayout'></a>

   Para a implementação  de todos layouts dos laboratórios utilizando o levantamento feito em sprints anteriores, criou-se a representação visual dos laboratórios com a disposição interna deste, abrangendo o posicionamento dos computadores, mesas, quadro branco e servidor. Esse processo foi feito na própria aplicação através da função e página de editar, após a conclusão da tarefa de layout editável, um dos requisitos do projeto. 
   
   

|       Laboratório grande de 32 computadores - sala 402       | Laboratório médio de 24 computadores - salas 301, 302 e 401  |
| :----------------------------------------------------------: | ------------------------------------------------------------ |
| <img src="img/layout labs/lab 32comps.jpg" alt="lab grande de 32 computadores" style="zoom: 150%;" /> | <img src="img/layout labs/lab 24comps.jpg" alt="lab médio de 24 computadores" style="zoom: 150%;" /> |

| Laboratório médio de 18 computadores - salas 403, 405, 406, 407, 408, 409, 411 e 412 |   Laboratório pequeno de 18 computadores - salas 303 e 404   |
| :----------------------------------------------------------: | :----------------------------------------------------------: |
| <img src="img/layout labs/lab 18comps a.jpg" alt="lab médiode 18 computadores" style="zoom: 150%;" /> | <img src="img/layout labs/lab 18comps b.jpg" alt="lab pequeno de 18 computadores" style="zoom: 150%;" /> |



3. ### Tornar  o layout dos laboratórios editável<a id='LayoutEditavel'></a>

   Através da descrição de como os dados serão armazenados no banco e também seus relacionamentos, bem como com diversas discussões com o cliente sobre as suas necessidades, foi feita a criação da modelagem conceitual do banco de dados relacional. Chegou-se à conclusão que, para essa atual etapa do projeto, eram necessárias apenas duas tabelas: uma para os chamados, outra para os usuários. Essa tabelas teriam cardinalidade de 1 para N, com a chave primária da tabela de usuários sendo usada como a chave estrangeira na tabela de chamados. A partir desse conceito foi esboçado o Diagrama Estrutural de Entidade Relacional que pode ser visto na próxima tarefa.

   

   <img src="img/layout editavel.png" alt="Editar layout dos laboratórios" style="zoom: 150%;" />

   

4. ### Possibilitar a edição das características das máquinas<a id='EditarMaquinas'></a>

   Para possibilitar que detalhes do computador sejam alterados e armazenados (processador, RAM e sistema operacional), a visualização do técnico das especificações das máquinas para o solicitante passou a ser a mesa da  da visualização do técnico, que possibilta a atualização das informações. O que diferencia as visualizações é o fato do usuário estar ou não logado. Os códigos de CSS de ambos foram espelhados para que o estilo permaneça o mesmo, independentemente das informações recebidas pelo código HTML.	

   

   <img src="img/editar componentes.jpg" alt="Editar componentes dos computadores" style="zoom: 150%;" />

   

5. ### Conectar o Banco de Dados com o layout do laboratório e informações das máquinas<a id='ConectarBanco'></a>

   Foram criadas funções para que o banco de dados consulte e persista o que o técnico salvar durante as edições de layout do laboratório, bem como as alterações das carecterísticas dos computadores.Isso é importante porque permite ao técnico que ele altere as informações das máquinas e o layout dos laboratórios e, a partir daí, os usuáios tenham infomações sempre atualizadas sobre cada laboratório e cada computador.

   

<br>

## :fire: Burndown<a id='burndown'></a>

<img src="img/burndown.png" alt="Burndown" style="zoom: 150%;" />



<br>

## :hatching_chick: Evolução do Backolog<a id='evolução'></a>

Como a metodologia ágil Scrum tem como princípios a adaptabilidade e o processo iteraitvo, mudanças ocorrem para que o produto chegue ao final da Sprint com o maior valor possível. Para isto, foram necessárias alterações de tarefas que geraram 4 atualizações de versão do Backlog do Produto:



<img src="img/evolução do backlog/evolução do backlog.jpg" alt="Burndown" style="zoom: 150%;" />

<br>

## :key: Histórias de Usuário<a id="historia"></a>



|          ID           |                     História de Usuário                      |
| :-------------------: | :----------------------------------------------------------: |
| US10<a id='us10'></a> | Pedro precisa de um sistema integrado que faça a interação direta entre os chamados abertos e a  área do técnico para um fundamental bom gerenciamento do tempo e tarefas |
| US12<a id='us12'></a> | Para Natália e Andréia um aviso de "confirmação de envio" da solicitação na própria página de abertura de chamados é necessário para que tenha conhecimento do envio, assim evitando que seja enviado repetidas vezes o mesmo problema, melhorando a interface com o usuário e impedindo que Pedro tenha muitos recebimentos com as mesmas solicitações. |
| US13<a id='us13'></a> | Natália, aluna e Andréa, professora, precisam de uma forma de identificação visual do computador dentro do laboratório disposto para confirmar que estão falando do computador correto quando abrirem o chamado. |
| US14<a id='us14'></a> | Pedro, técnico, precisa de uma identificação visual para saber exatamente qual computador está com problemas e onde está esse computador, pois isso evitará confusões e perda de tempo. |
| US15<a id='us15'></a> | Para que Natália, aluna, e Andréa, professora, possam especificar para qual computador estão abrindo o chamado, é necessário que o layout das máquinas esteja ligado ao banco de dados, evitando possíveis erros de digitação e interpretação. |
| US22<a id='us22'></a> | É muito importante para o cliente que o técnico Pedro possa editar facilmente a disposição dos itens dentro do laboratório de forma simples e rápida, para acompanhar possíveis mudanças físicas do laboratório em tempo real e facilitando assim que o programa apresentado para Andréia e Natália não fiquem desatualizado. |
| US23<a id='us23'></a> | Pedro precisa de algumas utilidades em sua área do técnico para que haja facilidade em seu dia-a-dia de trabalho. Entre essas funcionalidades estão: layout editável e mudança da nomenclatura, pois Pedro pode um dia sentir a necessidade de mudar o nome dos computadores; características da máquina, pois Pedro pode precisar fazer alguma alteração no hardware e deixa isso detalhado. |
