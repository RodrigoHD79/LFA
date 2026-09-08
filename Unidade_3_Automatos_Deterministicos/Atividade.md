01/09/2026

# Lista de Exercícios — Autômatos Finitos Determinísticos (AFD)

> **Disciplina:** Teoria das Linguagens e Autômatos  
> **Tema:** Autômatos Finitos Determinísticos  
> **Modalidade:** Atividade prática em grupo  
> **Objetivo:** identificar, interpretar, construir e testar AFDs.

---

## Identificação do grupo

| Campo | Preenchimento |
|---|---|
| Turma |     Ciência da Computação - N1            |
|  Data |            01/09/2026                     |
| Integrante 1 | Filipe Pedais Carvalho             |
| Integrante 2 | Guilherme Rodrigues de Almeida     |
| Integrante 3 | Paulo Henrique de Melo Loiola      |
| Integrante 4 | Pedro Henrique Sipriano Cavalcante |
| Integrante 5 | Rodrigo Damasceno Santos           |

## Orientações

- Registre o raciocínio utilizado em cada resposta.
- Nos exercícios com cadeias, apresente o caminho percorrido estado por estado.
- Nos exercícios de construção, entregue a quíntupla, a tabela de transição e o diagrama.
- Use `ε` para representar a cadeia vazia.
- Quando solicitado, implemente e teste o autômato no JFLAP.

---

# Parte 1 — Fundamentos

## Exercício 1 — Entendendo um autômato finito

Uma lâmpada controlada por um interruptor possui os estados `Desligado` e `Ligado`. Sempre que o botão é pressionado, ocorre a mudança:

```text
Desligado --pressionar--> Ligado
Ligado    --pressionar--> Desligado
```

Responda:

1. Quantos estados existem?
   
   R: Dois estados. Ligado e Desligado.
2. Qual é o estado inicial, considerando que a lâmpada começa apagada?
   
   R: O estado inicial é desligado.
3. Qual entrada provoca uma transição?
   
   R: Pressionar
4. Partindo de `Desligado`, qual será o estado após um acionamento?
   
   R: O próximo estado será Ligado.
5. Partindo de `Desligado`, qual será o estado após dois acionamentos?
    
   R: Após dois acionamentos, o estado estará em Desligado novamente.
6. Explique o funcionamento do sistema com suas palavras.
    
   R: O sistema recebe um estado inicial, se o estado for desligado ao ser pressionado o estado muda para ligado. Já quando o sistema está com o
      estado igual a ligado, ao ser pressionado seu estado é alterado para desligado. Funcionando como um interruptor. 

## Exercício 2 — Porta automática

Uma porta automática possui os estados `Fechado` e `Aberto`. O sensor identifica `pessoa_detectada` ou `nenhuma_pessoa`. Quando uma pessoa é detectada, a porta deve ficar aberta; quando ninguém é detectado, deve ficar fechada.

Complete a tabela:

| Estado atual | Entrada | Próximo estado |
|---|---|---|
| Fechado | pessoa_detectada | Aberto |
| Fechado | nenhuma_pessoa | Fechado |
| Aberto | pessoa_detectada | Aberto |
| Aberto | nenhuma_pessoa | Fechado |

Depois, desenhe o diagrama de estados correspondente e indique o estado inicial.

---

# Parte 2 — Anatomia e definição formal

## Exercício 3 — Identificando os elementos

Considere um AFD com `Σ = {0,1}`, `Q = {q0,q1}`, estado inicial `q0`, estado final `q1` e as transições abaixo:

| δ | 0 | 1 |
|---|---|---|
| q0 | q0 | q1 |
| q1 | q0 | q1 |

Identifique e explique:

1. o alfabeto `Σ`;

   **R:** $\Sigma = \{0, 1\}$. Representa o conjunto finito de símbolos de entrada que a máquina pode ler.

2. o conjunto de estados `Q`;

   **R:** $Q = \{q0, q1\}$. É o conjunto finito de todas as etapas ou situações possíveis do autômato.

3. o estado inicial;

   **R:** $q0$ ($q0 \in Q$). Indica o estado onde o processamento de qualquer cadeia é iniciado.

4. o conjunto de estados finais `F`;

   **R:** $F = \{q1\}$ ($F \subseteq Q$). Representa o conjunto de estados que determinam a condição de aceitação da cadeia.

5. os símbolos que podem ser lidos;

   **R:** $0$ e $1$. São os caracteres pertencentes ao alfabeto $\Sigma$ que disparam as transições de estado.

6. o significado do círculo duplo em um diagrama;

   **R:** Identifica visualmente um estado final (de aceitação).

7. o significado da seta sem origem apontando para um estado.

   **R:** Indica qual estado é o estado inicial ($q0$) do autômato.


## Exercício 4 — A quíntupla do AFD

Um AFD é formalmente representado por:

```text
M = (Σ, Q, δ, q0, F)
```

Complete:

| Elemento | Significado |
|---|---|
| `Σ` | Alfabeto de símbolos de entrada |
| `Q` | Conjunto finito de estados do autômato |
| `δ` | Função de transição |
| `q0` | Estado inicial |
| `F` | Conjunto de estados finais ou de aceitação |

Explique por que esses cinco elementos são suficientes para definir o funcionamento de um AFD.

**R:** Esses elementos cobrem todo o funcionamento do autômato sem deixar nenhuma dúvida. Eles informam onde o processo começa (q0), quais símbolos a máquina consegue ler (Σ), quais situações ela pode assumir (Q), a regra exata de como mudar de estado a cada leitura (δ) e como decidir se a palavra digitada foi aceita ou rejeitada no final (F)

# Parte 3 — Tabela de transições e cadeias

## Exercício 5 — Interpretando uma tabela

Considere `Σ = {0,1}`, `Q = {q0,q1,q2}`, estado inicial `q0`, `F = {q1}` e:

| δ | 0 | 1 |
|---|---|---|
| q0 | q0 | q1 |
| q1 | q2 | q1 |
| q2 | q1 | q1 |

Responda:

1. Qual é o resultado de `δ(q0,0)`?
2. Qual é o resultado de `δ(q0,1)`?
3. Qual é o resultado de `δ(q1,0)`?
4. Qual é o resultado de `δ(q2,1)`?
5. Qual é o estado de aceitação?
6. Desenhe o diagrama correspondente à tabela.
7. Justifique por que o autômato é determinístico.

## Exercício 6 — Aceita ou rejeita?

Utilize o AFD do Exercício 5. Determine se cada cadeia é aceita ou rejeitada:

```text
a) 1
b) 0011001
c) 010010
d) 1101
e) 000011010
```

Para cada cadeia, registre todas as transições. Exemplo:

```text
Cadeia: 01
q0 --0--> q0
q0 --1--> q1
Estado final: q1
Resultado: ACEITA
```

| Cadeia | Caminho percorrido | Estado final | Resultado |
|---|---|---|---|
| `1` | | | |
| `0011001` | | | |
| `010010` | | | |
| `1101` | | | |
| `000011010` | | | |

---

# Parte 4 — Construção de AFDs

## Exercício 7 — Cadeias que terminam em `1`

Construa um AFD sobre `Σ = {0,1}` que reconheça todas as cadeias que terminam em `1`.

- Devem ser aceitas: `1`, `01`, `101`, `0001`, `1101`.
- Devem ser rejeitadas: `ε`, `0`, `10`, `100`, `1110`.

Entregue: conjunto de estados, alfabeto, estado inicial, estados finais, tabela, diagrama e teste de pelo menos cinco cadeias.

R =
A. Conjunto de estados
Q={q0,q1} Q={q0,q1}
•	q0q0: estado inicial, usado quando a cadeia está vazia ou termina em 00;
•	q1q1: estado final, usado quando a cadeia termina em 11.

B. Alfabeto
Σ={0,1} Σ={0,1}

C. Estado inicial
q0q0

D. Estados finais
F={q1} F={q1}

E. Função de transição
A função de transição é definida por:
•	Se for lido o símbolo 00, o autômato vai para q0q0;
•	Se for lido o símbolo 11, o autômato vai para q1q1.

F. Tabela de transições
Estado atual	Entrada 0	Entrada 1
q0q_0q0        q0q_0q0     q1q_1q1
q1q_1q1        q0q_0q0     q1q_1q1

G. Diagrama do AFD
┌──────1───────┐
│              ▼
→ (q0) ──1──> ((q1))
▲              │
│              │ 1
└─────0─────── ┘
(q0) --0--> (q0)
(q1) --1--> (q0)
(q1) --1--> (q1)

Uma representação mais detalhada:

┌──────1───────┐
│              │
│              ▼
→ (q0) ────> ((q1))
▲               │
│               │
└────── 0 ──────┘

Laços:
- q0 --0--> q0
- q1 --1--> q1

H. O estado q1q1 é representado com dois círculos porque é o estado final.

Cadeia	     Caminho percorrido	                                                                                   Resultado

111	        q0→1q1q_0 \xrightarrow{1} q_1q01q1                                                                    Aceita

010101	     q0→0q0→1q1q_0 \xrightarrow{0} q_0 \xrightarrow{1} q_1q00q01q1                                         Aceita

101101101     q0→1q1→0q0→1q1q_0 \xrightarrow{1} q_1 \xrightarrow{0} q_0 \xrightarrow{1} q_1q01q10q01q1              Aceita

000100010001	q0→0q0→0q0→0q0→1q1q_0 \xrightarrow{0} q_0 \xrightarrow{0} q_0 \xrightarrow{0} q_0 \xrightarrow{1}                             q_1q00q00q00q01q1                                                                                    Aceita

110111011101	q0→1q1→1q1→0q0→1q1q_0 \xrightarrow{1} q_1 \xrightarrow{1} q_1 \xrightarrow{0} q_0 \xrightarrow{1}                             q_1q01q11q10q01q1                                                                                   Aceita

ε\varepsilonε	Permanece em q0q_0q0                                                                                 Rejeita

000	         q0→0q0q_0 \xrightarrow{0} q_0q00q0                                                                   Rejeita

101010	      q0→1q1→0q0q_0 \xrightarrow{1} q_1 \xrightarrow{0} q_0q01q10q0                                        Rejeita

100100100	   q0→1q1→0q0→0q0q_0 \xrightarrow{1} q_1 \xrightarrow{0} q_0 \xrightarrow{0} q_0q01q10q00q0             Rejeita

111011101110	q0→1q1→1q1→1q1→0q0q_0 \xrightarrow{1} q_1 \xrightarrow{1} q_1 \xrightarrow{1} q_1 \xrightarrow{0}                             _0q01q11q11q10q0                                                                                     Rejeita





## Exercício 8 — Número par de símbolos `1`

Construa um AFD sobre `Σ = {0,1}` que reconheça cadeias com quantidade par de símbolos `1`.

Analise: `ε`, `0`, `1`, `11`, `101`, `1100` e `10101`.

Apresente a definição formal `M = (Σ, Q, δ, q0, F)`, a tabela, o diagrama e o processamento das cadeias. Lembre-se de que basta controlar duas situações: quantidade par ou ímpar de símbolos `1`.

## Exercício 9 — Pelo menos dois zeros consecutivos

Construa um AFD para:

```text
L(M) = {w ∈ {0,1}* | w possui pelo menos dois 0s consecutivos}
```

- Devem ser aceitas: `00`, `001`, `100`, `1001`, `110011`, `0000`.
- Devem ser rejeitadas: `ε`, `0`, `1`, `01`, `10`, `10101`.

Responda antes de construir:

1. O que o estado inicial representa?
2. O que ocorre quando aparece o primeiro `0`?
3. O que ocorre quando outro `0` aparece imediatamente depois?
4. Depois de encontrar `00`, a cadeia pode deixar de ser aceita?
5. Quantos estados são necessários?

Apresente a quíntupla, a tabela, o diagrama e os testes.

---

# Parte 5 — Desafios de modelagem

## Exercício 10 — Semáforo

Modele um semáforo com os estados `Verde`, `Amarelo` e `Vermelho`. Use a entrada `tempo` e represente o ciclo:

```text
Verde → Amarelo → Vermelho → Verde
```

Entregue o diagrama, a tabela de transições, a definição formal e uma explicação do funcionamento. Discuta se há sentido em definir estados de aceitação nesse modelo e justifique a escolha adotada.

## Exercício 11 — Sistema de login

Modele um sistema com as entradas `senha_correta` e `senha_incorreta`. Uma senha correta autentica o usuário; após três tentativas incorretas, o sistema fica bloqueado.

Determine:

1. todos os estados necessários para contar as tentativas;
2. o alfabeto de entrada;
3. o estado inicial;
4. os estados finais;
5. todas as transições;
6. o comportamento após a autenticação e após o bloqueio.

Responda: apenas os estados `Aguardando`, `Autenticado` e `Bloqueado` são suficientes para controlar três tentativas? Justifique e construa o AFD completo.

---

# Parte 6 — Prática no JFLAP

## Exercício 12 — Implementação e testes

Escolha um dos AFDs dos exercícios 7, 8 ou 9 e implemente-o no JFLAP.

1. Crie os estados.
2. Defina o estado inicial e os estados finais.
3. Crie todas as transições.
4. Teste três cadeias que devem ser aceitas.
5. Teste três cadeias que devem ser rejeitadas.
6. Compare os resultados esperados e obtidos.

Inclua um print do AFD, a tabela de testes e uma breve explicação.

| Cadeia | Resultado esperado | Resultado no JFLAP | Conferência |
|---|---|---|---|
| | | | |
| | | | |
| | | | |
| | | | |
| | | | |
| | | | |

---

# Desafio final

## Exercício 13 — Crie seu próprio problema

Escolha uma situação real representável por estados, como elevador, máquina de vendas, controle de acesso, estacionamento, pedido de delivery, semáforo, porta eletrônica ou protocolo de comunicação.

O grupo deverá:

1. descrever o problema e suas regras;
2. identificar as entradas e os estados;
3. definir o estado inicial e os estados finais;
4. criar a tabela de transições;
5. desenhar o AFD;
6. apresentar `M = (Σ, Q, δ, q0, F)`;
7. testar pelo menos cinco sequências de entrada;
8. explicar por que o modelo é determinístico;
9. apresentar uma conclusão sobre o que foi aprendido.

---

# Entregável

O grupo deverá entregar um único arquivo `README.md`, contendo:

- identificação do grupo;
- respostas dos exercícios indicados pela professora;
- diagramas e tabelas de transição;
- processamento estado por estado das cadeias;
- evidência dos testes no JFLAP;
- conclusão do grupo.

## Modelo para o desafio final

```markdown
## Desafio final

### Problema escolhido

### Estados e significado

### Alfabeto

### Estado inicial e estados finais

### Tabela de transições

### Diagrama

### Definição formal
M = (Σ, Q, δ, q0, F)

### Testes realizados
| Entrada | Resultado esperado | Resultado obtido |
|---|---|---|
| | | |

### Evidência no JFLAP

### Conclusão
```

> **Importante:** não basta apresentar o diagrama. Demonstre como o AFD processa cada cadeia, estado por estado, até decidir pela aceitação ou rejeição.

---

**Profa. Kadidja Valéria**

