# Questão 3 — Identificador com duas maiúsculas, três algarismos e uma minúscula opcional

## 1. Definição da linguagem

O identificador deve obedecer exatamente ao seguinte formato:

```text
DUAS_MAIÚSCULAS + TRÊS_ALGARISMOS + UMA_MINÚSCULA_OPCIONAL
```

Formalmente:

|$$
L = \{w \in \Sigma^* \mid w \text{ possui duas letras maiúsculas, três algarismos e uma letra minúscula opcional}\}
$$|

A ordem dos elementos é obrigatória:

1. duas letras maiúsculas;
2. três algarismos;
3. zero ou uma letra minúscula.

Não são permitidos espaços, hífens, símbolos especiais ou caracteres adicionais.

---

## 2. Expressão regular

```regex
^[A-Z]{2}[0-9]{3}[a-z]?$
```

---

## 3. Explicação da expressão regular

| Parte | Significado |
|---|---|
| `^` | Início da cadeia |
| `[A-Z]` | Uma letra maiúscula |
| `{2}` | Exatamente duas ocorrências |
| `[0-9]` | Um algarismo |
| `{3}` | Exatamente três ocorrências |
| `[a-z]` | Uma letra minúscula |
| `?` | A letra minúscula pode aparecer zero ou uma vez |
| `$` | Final da cadeia |

A expressão regular exige que a cadeia inteira corresponda ao padrão. Por isso, os símbolos `^` e `$` impedem caracteres extras antes ou depois do identificador.

---

## 4. Exemplos aceitos

| Entrada | Estrutura | Resultado |
|---|---|---|
| `AB123` | `AB` + `123` | Aceita |
| `AB123a` | `AB` + `123` + `a` | Aceita |
| `CC202` | `CC` + `202` | Aceita |
| `CC202x` | `CC` + `202` + `x` | Aceita |
| `ES202` | `ES` + `202` | Aceita |
| `ES202b` | `ES` + `202` + `b` | Aceita |
| `SI999` | `SI` + `999` | Aceita |
| `ZZ000z` | `ZZ` + `000` + `z` | Aceita |

---

## 5. Exemplos rejeitados

| Entrada | Motivo da rejeição |
|---|---|
| `A123` | Possui apenas uma letra maiúscula |
| `ABC123` | Possui três letras maiúsculas |
| `AB12` | Possui apenas dois algarismos |
| `AB1234` | Possui quatro algarismos |
| `ab123` | As letras iniciais são minúsculas |
| `Ab123` | A segunda letra não é maiúscula |
| `AB123A` | A letra opcional deveria ser minúscula |
| `AB123ab` | Possui duas letras minúsculas |
| `AB-123` | Contém hífen |
| `AB 123` | Contém espaço |
| `AB123_` | Contém caractere extra |
| `AB123!` | Contém símbolo especial |
| `123AB` | Ordem dos elementos incorreta |
| `AB` | Não possui três algarismos |
| `ε` | Cadeia vazia |

---

## 6. Casos de fronteira

Os casos de fronteira verificam os menores e maiores formatos permitidos.

| Entrada | Resultado | Justificativa |
|---|---|---|
| `AA000` | Aceita | Formato mínimo sem minúscula |
| `AA000a` | Aceita | Formato mínimo com minúscula |
| `ZZ999` | Aceita | Limites superiores sem minúscula |
| `ZZ999z` | Aceita | Limites superiores com minúscula |
| `A000` | Rejeita | Falta uma letra maiúscula |
| `AAA000` | Rejeita | Há uma letra maiúscula extra |
| `AA00` | Rejeita | Falta um algarismo |
| `AA0000` | Rejeita | Há um algarismo extra |
| `AA000ab` | Rejeita | Há duas letras minúsculas |
| `AA000 a` | Rejeita | Contém espaço |

---

## 7. Tabela de testes

| Nº | Entrada | Resultado esperado | Resultado obtido |
|---:|---|---|---|
| 1 | `AB123` | Aceita | Aceita |
| 2 | `AB123a` | Aceita | Aceita |
| 3 | `CC202` | Aceita | Aceita |
| 4 | `CC202x` | Aceita | Aceita |
| 5 | `ES202b` | Aceita | Aceita |
| 6 | `ZZ999z` | Aceita | Aceita |
| 7 | `A123` | Rejeita | Rejeita |
| 8 | `ABC123` | Rejeita | Rejeita |
| 9 | `AB12` | Rejeita | Rejeita |
| 10 | `AB1234` | Rejeita | Rejeita |
| 11 | `ab123` | Rejeita | Rejeita |
| 12 | `AB123A` | Rejeita | Rejeita |
| 13 | `AB123ab` | Rejeita | Rejeita |
| 14 | `AB-123` | Rejeita | Rejeita |
| 15 | `AB 123` | Rejeita | Rejeita |
| 16 | `AB123!` | Rejeita | Rejeita |

---

## 8. Justificativa

A expressão regular:

```regex
^[A-Z]{2}[0-9]{3}[a-z]?$
```

representa corretamente a linguagem porque:

- `[A-Z]{2}` exige exatamente duas letras maiúsculas;
- `[0-9]{3}` exige exatamente três algarismos;
- `[a-z]?` permite nenhuma ou uma letra minúscula;
- `^` e `$` garantem que toda a cadeia siga o formato;
- qualquer caractere extra faz com que a entrada seja rejeitada.

Todos os exemplos aceitos seguem o formato definido, enquanto os exemplos rejeitados violam pelo menos uma das regras da linguagem.

---

## 9. Conclusão

A Regex final é:

```regex
^[A-Z]{2}[0-9]{3}[a-z]?$
```

Ela reconhece identificadores no formato:

```text
Duas letras maiúsculas + três algarismos + uma letra minúscula opcional
```

Exemplos válidos:

```text
AB123
AB123a
CC202
ES202b
ZZ999z
```
