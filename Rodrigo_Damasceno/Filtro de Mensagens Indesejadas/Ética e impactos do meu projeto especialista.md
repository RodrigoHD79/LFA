Aluno: Rodrigo Damasceno Santos

RGM: 39188949

Disciplina: Linguagens Formais e Autômatos — CC-N1

Professor(a): Kadidja Valéria

Data: 18/11/2026



                                        Ética e impactos do meu projeto especialista



1. Leitura do artigo e análise do vídeo


Artigo científico
Li o artigo “Da proibição à governança: uso ético da inteligência artificial generativa na educação superior — uma revisão integrativa (2023–2026)”, de Francisco Pires de Lacerda Júnior.
Uma ideia importante do artigo é que o uso ético da inteligência artificial não se resume a permitir ou proibir a tecnologia. É necessário definir sua finalidade, verificar os resultados, proteger os dados
envolvidos e manter a responsabilidade humana. O autor organiza essa proposta em cinco movimentos: definir, ensinar, redesenhar, proteger e acompanhar.
Essa reflexão também se aplica ao meu projeto. Embora meu sistema não use um modelo de inteligência artificial para classificar mensagens, o resultado pode influenciar a decisão de quem o utiliza.
Por isso, considero importante explicar como as regras funcionam, reconhecer suas limitações e permitir que uma pessoa revise a classificação.


Trecho do vídeo
No vídeo “Da proibição à governança: o estado da arte em Ética na Inteligência Artificial”, escolhi o trecho entre 05:30 e 06:34. Nesse momento, o palestrante, Steven Gouveia da Universidade do Porto, 
usa a história da pintura para mostrar que as mudanças artísticas também alteraram quais perspectivas e elementos eram considerados importantes. Em seguida, relaciona essa discussão à ética em inteligência artificial 
e questiona uma visão que trate a tecnologia apenas como uma questão técnica ou como uma lista de requisitos a cumprir.
A ideia que levo ao debate é que os critérios de um sistema refletem escolhas humanas. Quem define as regras também escolhe, em parte, o que o sistema reconhece e o que pode deixar de perceber. 
No meu projeto, fui eu quem escolheu quais características seriam tratadas como sinais de mensagens indesejadas. Essas regras identificam alguns padrões, mas não abrangem todos os contextos ou formas de escrita.
Relaciono esse trecho ao artigo porque ambos me levam a pensar além da aparência do resultado. Informar uma classificação e apresentar os motivos é importante, mas não basta se os critérios forem inadequados, 
se os testes forem limitados ou se ninguém puder questionar a conclusão. A ética precisa fazer parte da construção e do uso do sistema.
Trecho selecionado: 05:30–06:34
Ideia para o debate: os critérios de um sistema refletem escolhas humanas; por isso, é importante avaliar quem os definiu, quem pode ser afetado por eles e como uma decisão pode ser revista.


2. Análise ética do projeto

Apresentação do projeto
Desenvolvi um sistema especialista em Python para analisar mensagens e identificar características que associei a conteúdos indesejados. O usuário digita uma mensagem, e o programa verifica regras determinísticas
definidas por mim e termos armazenados em palavras_suspeitas.txt.
Se pelo menos uma regra for acionada, a mensagem é classificada como indesejada e o sistema apresenta os motivos encontrados. Se nenhuma regra for acionada, a mensagem é classificada como suspeita e recomenda-se uma revisão humana. A classificação não vem de uma previsão de modelo de inteligência artificial: ela resulta da aplicação das regras e da consulta aos termos cadastrados.


Privacidade e dados
Para analisar uma mensagem, o usuário digita ou cola seu conteúdo no programa. Esse texto pode incluir nomes, números de telefone, informações bancárias ou outros dados pessoais. Por exemplo, alguém pode usar uma mensagem real de um banco para testar as regras. Nesse caso, o conteúdo pode revelar informações do destinatário ou de outras pessoas mencionadas.
Para reduzir esse risco, nos testes e nas apresentações devo utilizar exemplos fictícios ou remover dados que identifiquem alguém. O projeto não precisa manter um histórico das mensagens analisadas. O arquivo palavras_suspeitas.txt serve para armazenar os termos cadastrados, não informações sobre as pessoas envolvidas.


Viés e equidade
As regras do sistema representam critérios que escolhi. Elas podem favorecer determinadas palavras ou formas de expressão e não reconhecer outras. Uma mensagem legítima que mencione senha, prêmio, urgência ou conta bloqueada pode ser classificada como indesejada. Por outro lado, uma mensagem maliciosa que use palavras diferentes das previstas pode não acionar nenhuma regra.
Quem recebe a mensagem pode ser prejudicado se confiar demais na classificação e ignorar uma comunicação legítima. O remetente também pode ser afetado se sua mensagem for tratada como fraudulenta sem uma análise do contexto. Para verificar esses riscos, devo testar exemplos legítimos e indesejados, incluindo mensagens legítimas que contenham termos reconhecidos e mensagens suspeitas escritas de formas diferentes. A classificação deve servir como alerta para revisão, não como veredito.


Transparência
O programa informa a classificação e, quando identifica uma ou mais condições, apresenta os motivos correspondentes. Isso permite ao usuário verificar quais regras foram acionadas, em vez de receber apenas uma resposta sem explicação.
Também é importante não atribuir ao resultado um significado maior do que ele tem. O sistema não calcula uma probabilidade de fraude, não confirma a identidade do remetente e não verifica, por si só, se um link é seguro. Quando nenhuma regra é acionada, o resultado “suspeita” não significa que a mensagem seja comprovadamente perigosa; significa que o programa não encontrou uma regra conhecida para classificá-la como indesejada. Da mesma forma, uma regra acionada indica uma correspondência com os critérios do programa, não uma prova definitiva de fraude.


Supervisão e responsabilidade
A classificação deve ser revisada por quem utiliza o programa antes de uma decisão importante, como bloquear um remetente, excluir uma mensagem ou encaminhar uma denúncia. A pessoa pode considerar informações que o sistema não avalia, como a relação com o remetente, o contexto da conversa e a legitimidade do serviço mencionado.
Sou responsável pelas regras e funcionalidades que defini e implementei, além de explicar as limitações do sistema. Quem utiliza o programa deve avaliar o contexto e decidir o que fazer. O sistema auxilia a análise, mas não substitui a responsabilidade humana.


Impacto social
O sistema pode ajudar a identificar sinais comuns em mensagens indesejadas. Ao apresentar os motivos encontrados, chama a atenção para elementos que podem merecer uma verificação mais cuidadosa. Porém, uma classificação incorreta pode levar alguém a ignorar uma mensagem legítima. Também é possível que uma mensagem maliciosa não seja reconhecida por não corresponder às regras.
Por esse motivo, o programa não declara segura uma mensagem quando nenhuma regra é acionada. Ele a classifica como suspeita e recomenda revisão humana. Essa medida não elimina todos os erros, mas evita apresentar o resultado como uma garantia.


3. Dilema ético e reflexão individual

Dilema
Um dilema do projeto surge quando uma mensagem legítima aciona uma regra. Um aviso verdadeiro de um banco, por exemplo, pode mencionar uma senha ou uma conta bloqueada. O programa pode associar esses termos a uma 
característica suspeita, mesmo quando a mensagem não é fraudulenta.
Uma possibilidade seria bloquear ou descartar automaticamente toda mensagem classificada como indesejada. Isso poderia chamar a atenção para alguns riscos, mas também poderia impedir que o usuário recebesse uma 
comunicação legítima ou importante.
Outra possibilidade é apresentar a classificação e os motivos, deixando a decisão final para uma pessoa. Essa alternativa exige que o usuário examine a mensagem, mas permite considerar informações que o programa 
não conhece. No meu projeto, considero mais responsável seguir essa segunda opção: as regras identificam padrões, mas não comprovam, sozinhas, a intenção de quem enviou a mensagem.


Relação com o vídeo e o artigo
No trecho entre 05:30 e 06:34 do vídeo, a reflexão sobre mudanças de perspectiva mostra que aquilo que recebe atenção depende, em parte, das escolhas de quem observa. Relacionei essa ideia ao meu sistema 
porque os critérios que defini determinam quais sinais o programa reconhece. Se as regras forem tratadas como completas ou neutras, posso deixar de considerar mensagens e contextos que não se encaixam nos padrões escolhidos.
O artigo complementa essa reflexão ao defender que os usos de inteligência artificial sejam justificados e verificados, com proteção de dados e responsabilidade humana. Embora meu projeto não use um modelo de 
IA para classificar mensagens, esses princípios também são pertinentes: as regras podem afetar decisões e, por isso, precisam ser explicadas, testadas e revistas.


Reflexão individual
Depois de analisar o dilema, eu manteria a decisão de não bloquear automaticamente as mensagens. O argumento que mais influenciou minha posição é que uma regra pode identificar uma palavra sem compreender o contexto em que ela foi usada.
Para verificar se essa medida funciona, testaria mensagens legítimas e indesejadas, registraria as situações em que a classificação parece incorreta e revisaria as regras. Também avaliaria se a explicação apresentada ajuda o usuário a compreender o resultado sem levá-lo a tratá-lo como certeza. Mesmo depois de aperfeiçoar as regras, manteria a revisão humana antes de decisões importantes.

4. Declaração de uso de sistemas de IA

IA incorporada ao projeto
Meu projeto não incorpora um modelo de inteligência artificial. Desenvolvi um sistema especialista em Python que utiliza regras determinísticas e termos cadastrados pelo usuário. O programa recebe o texto 
de uma mensagem e gera a classificação “indesejada” ou “suspeita”, apresentando os motivos encontrados quando uma ou mais regras são acionadas.
As escolhas sobre a proposta, as regras, as funcionalidades e o modo de funcionamento partiram de mim. Durante o desenvolvimento, pensei nos critérios que o sistema deveria analisar e nas opções que o usuário 
poderia utilizar, como analisar mensagens, cadastrar termos, listar os termos existentes e excluir termos. Também implementei o programa e testei suas funções.
Entre as limitações estão a possibilidade de classificar uma mensagem legítima como indesejada e a dificuldade de reconhecer mensagens que não correspondam às regras conhecidas. Por isso, o resultado serve como 
apoio à análise e deve ser revisado por uma pessoa. A decisão final cabe ao usuário; as regras e o funcionamento do sistema são de minha responsabilidade.


IA utilizada na elaboração do trabalho
Utilizei o ChatGPT como apoio durante o desenvolvimento e a elaboração deste trabalho. Pedi ajuda para esclarecer algumas dúvidas, organizar a apresentação, revisar a redação e melhorar a estrutura da análise ética. 

As decisões sobre o projeto - a proposta, as regras, as funcionalidades que eu idealizei e as que ví necessidade de acrescentar e o modo de funcionamento, foram pensadas e definidas por mim. Desenvolvi o sistema e 
verifiquei seu funcionamento; o ChatGPT apenas me assessorou e ajudou com algumas dúvidas e pesquisas.
Neste documento, aproveitei sugestões de organização e escrita. Conferi as informações com o funcionamento do projeto, o enunciado da atividade, o artigo e o vídeo. Revisei o conteúdo e assumo a responsabilidade por
todas as escolhas, por todo trabalho desenvolvido, pelas verificações e pelo texto final.


5. Síntese da entrega
   
Este trabalho reúne a análise de privacidade, viés, transparência, supervisão humana e impacto social do projeto, além de apresentar um dilema ético, uma reflexão individual e as declarações sobre o uso de
inteligência artificial. Do artigo, utilizei a discussão sobre governança, verificação e responsabilidade humana. Do vídeo, selecionei o trecho entre 05:30 e 06:34, que me levou a refletir sobre como as 
perspectivas e escolhas humanas influenciam os critérios de um sistema.
Minha principal conclusão é que regras claras e explicações compreensíveis são importantes, mas não eliminam as limitações de um sistema. No meu projeto, a classificação deve ajudar a pessoa a examinar uma mensagem,
não decidir por ela. Testar diferentes exemplos, apresentar os motivos encontrados e manter a revisão humana são medidas que ajudam a evitar que o resultado seja tratado como uma certeza.
