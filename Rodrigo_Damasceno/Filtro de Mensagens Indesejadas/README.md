Sistema Especialista de Filtragem de Mensagens Indesejadas 
Um pouco sobre o sistema e como terminar-lo

Desenvolvi este projeto para a disciplina de Linguagens Formais e Autômatos (LFA). O sistema analisa mensagens com base em regras definidas no programa e informa se elas são indesejadas ou suspeitas. Também permite cadastrar e excluir termos suspeitos, que ficam armazenados em um arquivo de texto.

Como o sistema funciona O sistema compara o conteúdo da mensagem com um conjunto de regras. A classificação é determinada pelo resultado dessas verificações:

Indesejada: uma ou mais regras conhecidas foram identificadas na mensagem. Suspeita: nenhuma das regras conhecidas foi identificada. Nesse caso, o sistema recomenda que uma pessoa revise a mensagem. O programa não usa probabilidades, inteligência artificial generativa nem uma pontuação gradual. A classificação é determinística: diante da mesma mensagem e das mesmas regras cadastradas, o sistema aplica os mesmos critérios e produz o mesmo resultado.

Motor de inferência e regras determinísticas O motor de inferência é uma parte do sistema que aplica as regras às informações recebidas. Neste projeto, ele analisa o texto da mensagem e verifica se há elementos associados a situações ambientais indesejadas.

Cada regra funciona como uma condição objetiva. Por exemplo: se a mensagem contém uma menção a senha, ou se apresenta três ou mais links, a condição correspondente é considerada atendida. O sistema verifica as regras e usa os resultados para chegar a uma conclusão.

A lógica da decisão é direta:

O sistema recebe uma mensagem. Analise o texto e verifique as regras programadas, além dos termos cadastrados no arquivo palavras_suspeitas.txt. Se pelo menos uma regra para acionada, a mensagem é definida como indesejada. Se nenhuma regra for acionada, a mensagem é tão suspeita e deve ser avaliada por uma pessoa. As regras são determinísticas porque não dependem de sorteio, probabilidade ou interpretação variável do sistema. Elas são condições predefinidas: quando uma condição é satisfeita, a regra é acionada; quando não é, não é acionado. Cadastrar ou excluir termos altera os dados usados ​​na análise, mas não transforma o sistema em uma classificação probabilística.

O que o sistema verifica Entre outras características, o programa verifica:

Menções a senhas; Termos relacionados a prêmios; Linguagem de urgência; Avisos de conta bloqueada; Solicitações de dados pessoais ou bancários; Pedidos de pagamento urgente; Presença de três ou mais links;

Termos suspeitos cadastrados pelo usuário. As regras programadas são avaliadas pelo sistema durante a análise. Os termos cadastrados pelo usuário são salvos em palavras_suspeitas.txt, para que possam continuar disponíveis nas próximas execuções, desde que esse arquivo seja excluído junto com o programa.

Como executar o programa O GitHub armazena os arquivos, mas não executa o programa diretamente na página. Para usar a versão pronta para Windows:

Baixe main.exe e palavras_suspeitas.txt do repositório. Coloque os dois arquivos na mesma pasta do computador. Abra main.exe com dois cliques. O arquivo palavras_suspeitas.txt contém os termos cadastrados. Se você baixar apenas o seguinte, esses termos não estarão disponíveis. O programa também usa o arquivo TXT para salvar os novos termos cadastrados. Por isso, mantenha-o junto com main.exe.

Como executar pelo código-fonte O arquivo main.py contém o código-fonte do projeto. Para repeti-lo, é necessário ter o Python instalado.

Abra um terminal na pasta do projeto e execute:

python main.py Como gerar o seguintevel Usei o PyInstaller para gerar o seguintevel. Para criá-lo novamente, instale o PyInstaller e execute este comando no terminal, dentro da pasta onde está main.py:

python -m PyInstaller --onefile main.py O seguinte nível será criado na pasta dist. Para que o programa utilize e salve os termos cadastrados, coloque palavras_suspeitas.txt na mesma pasta que o seguimentovel gerado.

Arquivos principais main.py — código-fonte do sistema; main.exe — continuaçãovel para Windows; palavras_suspeitas.txt — arquivo que armazena os termos cadastrados; dist/ e outros arquivos gerados pelo PyInstaller — arquivos criados durante o processo de geração do seguintevel.

Observação sobre a revisão humana O sistema só consegue identificar situações que tenham sido previstas nas regras do programa ou representadas pelos termos cadastrados. Ele não compreende todos os contextos possíveis nem consegue garantir que uma mensagem seja segura apenas por não encontrar uma regra conhecida.

Por isso, quando nenhuma regra é acionada, o sistema não declara que a mensagem é segura: ele a classifica como suspeita, diminuindo que precisa de revisão humana. Uma pessoa pode considerar o contexto, a identidade do remetente e outros sinais que o programa talvez não consiga buscar. Essa escolha torna o resultado mais cauteloso: mensagens que não atendem a padrões conhecidos não são automaticamente liberadas como confiáveis.
