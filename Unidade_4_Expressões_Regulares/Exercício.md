## Questão 1 —  Sobre {0,1}, descreva palavras que terminam em 00

Todas as sequências que possuem um comprimento mínimo de dois caracteres e cujos dois últimos símbolos são obrigatoriamente zeros.
Exemplos de palavras aceitas: 00, 100, 000, 1100, 010100, 111100...

## Questão 2 — Sobre {a,b}, descreva palavras com exatamente dois a

Todas as sequências que possuem exatamente dois símbolos a, podendo conter qualquer quantidade de símbolos b antes, entre ou depois dos dois a.

Exemplos de palavras aceitas: aa, aab, aba, baa, abba, baba, aabbbb, bbaabb, bbabb a...



## Questão 3 — Desafio: matrícula acadêmica

## Enunciado

Construa uma expressão regular para reconhecer identificadores no formato:

```text
CURSO-ANO-NÚMERO-TURNO
```

A matrícula deve obedecer a todas as regras definidas no desafio.

---

## Desafio: matrícula acadêmica

### Regras

- **Formato:** `CURSO-ANO-NÚMERO-TURNO`
- **Curso:** `CCO`, `ESW` ou `SIS`
- **Ano:** de `2024` a `2029`
- **Número:** exatamente quatro algarismos
- **Turno:** `M`, `T` ou `N`
- devem ser utilizados hífens entre os blocos;
- não são permitidos caracteres extras.

---

## 1. Linguagem

A linguagem dos identificadores válidos pode ser representada por:

|$$
L =
\{
c-a-n-t
\mid
c \in \{CCO, ESW, SIS\},
a \in \{2024,2025,2026,2027,2028,2029\},
n \in [0-9]^4,
t \in \{M,T,N\}
\}
$$|

Em palavras, a linguagem contém todas as cadeias que possuem:

```text
um curso válido
+ um hífen
+ um ano entre 2024 e 2029
+ um hífen
+ exatamente quatro algarismos
+ um hífen
+ um turno válido
```

---

## 2. Expressão regular

```regex
^(CCO|ESW|SIS)-202[4-9]-[0-9]{4}-(M|T|N)$
```

---

## 3. Explicação da expressão regular

| Parte da Regex | Significado |
|---|---|
| `^` | Indica o início da cadeia |
| `(CCO\|ESW\|SIS)` | Permite os cursos `CCO`, `ESW` ou `SIS` |
| `-` | Exige um hífen após o curso |
| `202[4-9]` | Permite os anos de `2024` até `2029` |
| `-` | Exige um hífen após o ano |
| `[0-9]{4}` | Exige exatamente quatro algarismos |
| `-` | Exige um hífen após o número |
| `(M\|T\|N)` | Permite os turnos `M`, `T` ou `N` |
| `$` | Indica o final da cadeia |

Os símbolos `^` e `$` garantem que a cadeia inteira seja validada. Assim, caracteres extras no início ou no final causam rejeição.

---

## 4. Estrutura da matrícula

A estrutura exigida é:

```text
CURSO-ANO-NÚMERO-TURNO
```

Exemplo:

```text
CCO-2024-1234-M
```

Separação do exemplo:

| Parte | Valor | Regra |
|---|---|---|
| Curso | `CCO` | Deve ser `CCO`, `ESW` ou `SIS` |
| Ano | `2024` | Deve estar entre `2024` e `2029` |
| Número | `1234` | Deve possuir exatamente quatro algarismos |
| Turno | `M` | Deve ser `M`, `T` ou `N` |

---

## 5. Exemplos aceitos

| Entrada | Justificativa |
|---|---|
| `CCO-2024-1234-M` | Todos os blocos são válidos |
| `ESW-2025-0001-T` | Curso, ano, número e turno válidos |
| `SIS-2026-9999-N` | Número possui quatro algarismos |
| `CCO-2027-4321-M` | Ano dentro do intervalo permitido |
| `ESW-2028-0100-T` | Formato completo e válido |
| `SIS-2029-9876-N` | Ano máximo permitido e turno válido |

---

## 6. Exemplos rejeitados

| Entrada | Motivo da rejeição |
|---|---|
| `ABC-2024-1234-M` | Curso não permitido |
| `CCO-2023-1234-M` | Ano inferior a `2024` |
| `CCO-2030-1234-M` | Ano superior a `2029` |
| `CCO-2024-123-M` | Número possui apenas três algarismos |
| `CCO-2024-12345-M` | Número possui cinco algarismos |
| `CCO-2024-1234-X` | Turno não permitido |
| `CCO-2024-1234-MT` | Turno possui dois caracteres |
| `CCO2024-1234-M` | Falta o hífen após o curso |
| `CCO-2024_1234-M` | Foi utilizado `_` em vez de hífen |
| `CCO-2024-1234M` | Falta o hífen antes do turno |
| `CCO/2024/1234/M` | Foram utilizadas barras em vez de hífens |
| `CCO-2024-1234-M-extra` | Existem caracteres extras |
| `CCO-2024-1234` | Falta o turno |
| `CCO-2024-1234-m` | O turno está em minúscula |
| `cco-2024-1234-M` | O curso está em minúsculas |

---

## 7. Casos de fronteira

Os casos de fronteira verificam os limites da linguagem.

| Entrada | Resultado esperado | Justificativa |
|---|---|---|
| `CCO-2024-0000-M` | Aceita | Menor ano e menor número válidos |
| `SIS-2029-9999-N` | Aceita | Maior ano e maior número válidos |
| `ESW-2024-0001-T` | Aceita | Primeiro ano permitido |
| `CCO-2029-9999-M` | Aceita | Último ano permitido |
| `CCO-2023-9999-M` | Rejeita | Ano abaixo do limite |
| `CCO-2030-0000-M` | Rejeita | Ano acima do limite |
| `CCO-2024-000-M` | Rejeita | Número possui três algarismos |
| `CCO-2024-00000-M` | Rejeita | Número possui cinco algarismos |
| `CCO-2024-0000` | Rejeita | Turno ausente |
| `CCO-2024-0000-MM` | Rejeita | Turno possui dois símbolos |

---

## 8. Tabela de testes

| Nº | Entrada | Resultado esperado | Resultado obtido |
|---:|---|---|---|
| 1 | `CCO-2024-1234-M` | Aceita | Aceita |
| 2 | `ESW-2025-0001-T` | Aceita | Aceita |
| 3 | `SIS-2026-9999-N` | Aceita | Aceita |
| 4 | `CCO-2027-4321-M` | Aceita | Aceita |
| 5 | `ESW-2028-0100-T` | Aceita | Aceita |
| 6 | `SIS-2029-9876-N` | Aceita | Aceita |
| 7 | `ABC-2024-1234-M` | Rejeita | Rejeita |
| 8 | `CCO-2023-1234-M` | Rejeita | Rejeita |
| 9 | `CCO-2030-1234-M` | Rejeita | Rejeita |
| 10 | `CCO-2024-123-M` | Rejeita | Rejeita |
| 11 | `CCO-2024-12345-M` | Rejeita | Rejeita |
| 12 | `CCO-2024-1234-X` | Rejeita | Rejeita |
| 13 | `CCO2024-1234-M` | Rejeita | Rejeita |
| 14 | `CCO-2024-1234-M-extra` | Rejeita | Rejeita |

---

## 9. Entradas quase corretas

As entradas abaixo são semelhantes às válidas, mas violam uma regra específica:

| Entrada | Regra violada |
|---|---|
| `CCO-2024-123-M` | O número deve ter quatro algarismos |
| `CCO-2024-12345-M` | O número deve ter exatamente quatro algarismos |
| `CCO-2023-1234-M` | O ano deve começar em `2024` |
| `CCO-2030-1234-M` | O ano máximo é `2029` |
| `ABC-2024-1234-M` | O curso não está entre os permitidos |
| `CCO-2024-1234-X` | O turno deve ser `M`, `T` ou `N` |
| `CCO-2024-1234-M-extra` | A cadeia não pode conter caracteres extras |
| `CCO2024-1234-M` | Os blocos devem ser separados por hífens |

---

## 10. Justificativa

A Regex:

```regex
^(CCO|ESW|SIS)-202[4-9]-[0-9]{4}-(M|T|N)$
```

representa corretamente a linguagem porque:

1. limita o curso às opções `CCO`, `ESW` e `SIS`;
2. permite somente os anos de `2024` a `2029`;
3. exige exatamente quatro algarismos para o número;
4. limita o turno às opções `M`, `T` e `N`;
5. exige os três hífens entre os blocos;
6. impede caracteres extras no início ou no final da cadeia.

---

## 11. Conclusão

A expressão regular final do desafio é:

```regex
^(CCO|ESW|SIS)-202[4-9]-[0-9]{4}-(M|T|N)$
```

Ela reconhece exatamente as matrículas no formato:

```text
CURSO-ANO-NÚMERO-TURNO
```

com as seguintes restrições:

```text
CURSO: CCO, ESW ou SIS
ANO: 2024 até 2029
NÚMERO: exatamente quatro algarismos
TURNO: M, T ou N
SEPARAÇÃO: hífens obrigatórios
CARACTERES EXTRAS: não permitidos
```



