Sistema Especialista para Filtragem de Mensagens Indesejadas

Este projeto foi desenvolvido por mim para a disciplina de Linguagens Formais e Autômatos (LFA). Ele analisa mensagens usando regras definidas no programa e informa se elas são indesejadas ou suspeitas.

Como o sistema funciona
Indesejada: quando uma ou mais regras conhecidas são identificadas na mensagem.
Suspeita: quando nenhuma regra conhecida é identificada. Nesse caso, a mensagem deve ser revisada por uma pessoa.

O sistema não usa probabilidades nem pontuação gradual: a classificação depende das regras cadastradas.

O que o sistema verifica

Entre outras características, o programa verifica:

Menções a senha;
Termos relacionados a prêmios, urgência ou bloqueio;
Solicitações de dados ou informações bancárias;
Pedidos de pagamento urgente;
Presença de três ou mais links.
Como executar o programa

O GitHub armazena os arquivos, mas não executa o programa na página. Para usar o sistema:

Baixe main.exe e palavras_suspeitas.txt do repositório para o computador.
Coloque os dois arquivos na mesma pasta.
Abra o main.exe com dois cliques.

O arquivo palavras_suspeitas.txt contém os termos cadastrados. Se baixar somente o executável, esses termos não estarão disponíveis. Por isso, é importante manter o arquivo TXT junto do main.exe. O sistema também pode usar esse arquivo para salvar novos termos cadastrados.

Como executar pelo código-fonte

O arquivo main.py contém o código-fonte do projeto. Para executá-lo, é necessário ter o Python instalado. Abra um terminal na pasta do projeto e digite:

python main.py

Como gerar o executável?

Usei o PyInstaller para criar o executável. Para gerá-lo novamente, instale o PyInstaller e execute este comando na pasta onde está o main.py:

python -m PyInstaller --onefile main.py


O executável será criado na pasta dist. Para usar os termos cadastrados, mantenha o palavras_suspeitas.txt junto do main.exe.

Arquivos principais
main.py — código-fonte do sistema;
main.exe — executável para Windows;
palavras_suspeitas.txt — arquivo que armazena os termos cadastrados;
dist/ e outros arquivos do PyInstaller — arquivos gerados ao criar o executável.
Observação

O sistema segue regras que defini previamente. Por isso, quando uma mensagem não corresponde a nenhuma regra conhecida, ela é classificada como suspeita e precisa ser revisada por uma pessoa.
