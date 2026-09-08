Questão 3 — Expressão regular para identificadores
Enunciado

Construir uma expressão regular para reconhecer identificadores formados por:

exatamente duas letras maiúsculas;
exatamente três algarismos;
uma letra minúscula opcional;
nenhum caractere adicional.
Expressão regular
Regex
Copiar
^
[A-Z]{2}[0-9]{3}[a-z]?
$
Explicação
Parte	Significado
^	Início da cadeia
[A-Z]	Uma letra maiúscula
{2}	Exatamente duas letras maiúsculas
[0-9]	Um algarismo
{3}	Exatamente três algarismos
[a-z]	Uma letra minúscula
?	A letra minúscula é opcional
$	Fim da cadeia
Exportar
Copiar

A expressão exige que a cadeia inteira siga o formato:

Text
Copiar
DUAS_MAIÚSCULAS + TRÊS_ALGARISMOS + MINÚSCULA_OPCIONAL
Exemplos aceitos
Cadeia	Divisão	Resultado
AB123	AB + 123	Aceita
AB123a	AB + 123 + a	Aceita
CC202	CC + 202	Aceita
ES202b	ES + 202 + b	Aceita
SI123s	SI + 123 + s	Aceita
ZZ999z	ZZ + 999 + z	Aceita
Exportar
Copiar
Exemplos rejeitados
Cadeia	Motivo
A123	Possui apenas uma letra maiúscula
ABC123	Possui três letras maiúsculas
AB12	Possui apenas dois algarismos
AB1234	Possui quatro algarismos
ab123	As letras iniciais não são maiúsculas
AB123A	A letra opcional é maiúscula
AB123ab	Possui duas letras minúsculas
AB-123	Contém o caractere -
AB 123	Contém espaço
AB123_	Contém caractere adicional
123AB	A ordem dos elementos está incorreta
AB	Não possui três algarismos
ε	Cadeia vazia
Exportar
Copiar
Tabela de testes
Nº	Cadeia	Resultado esperado	Resultado obtido
1	AB123	Aceita	Aceita
2	AB123a	Aceita	Aceita
3	CC202	Aceita	Aceita
4	ES202b	Aceita	Aceita
5	SI123s	Aceita	Aceita
6	ZZ999z	Aceita	Aceita
7	A123	Rejeita	Rejeita
8	ABC123	Rejeita	Rejeita
9	AB12	Rejeita	Rejeita
10	AB1234	Rejeita	Rejeita
11	ab123	Rejeita	Rejeita
12	AB123A	Rejeita	Rejeita
13	AB123ab	Rejeita	Rejeita
14	AB-123	Rejeita	Rejeita
Exportar
Copiar
Conclusão

A expressão regular:

Regex
Copiar
^
[A-Z]{2}[0-9]{3}[a-z]?
$

reconhece corretamente identificadores com duas letras maiúsculas, três algarismos e uma letra minúscula opcional. As âncoras ^ e $ garantem que nenhum caractere extra seja aceito antes ou depois do identificador.
