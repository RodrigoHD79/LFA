# Exercícios Práticos para Fixação

## Bloco 1 — Derivação

Dada a gramática **G1**:

**S → aS | b**

### A) Gere a palavra `aaab`.

**Resposta:**

`S ⇒ aS ⇒ aaS ⇒ aaaS ⇒ aaab`

### B) Explique como você sabe que a derivação terminou.

**Resposta:**

A derivação termina quando não há mais símbolos não terminais, como `S`, na palavra gerada. Nesse caso, após aplicar a produção `S → b`, obtemos `aaab`, que contém apenas símbolos terminais.

## Bloco 2 — GLC

Dada a gramática **G2**:

**S → aSb | ε**

### A) Gere a palavra `aaabbb`.

**Resposta:**

`S ⇒ aSb ⇒ aaSbb ⇒ aaaSbbb ⇒ aaabbb`

### B) É possível gerar `aabbb`? Justifique.

**Resposta:**

Não. A cada aplicação da produção `S → aSb`, é acrescentado um `a` no início e um `b` no final. Portanto, a quantidade de `a`s e `b`s deve ser sempre igual. Como `aabbb` possui dois `a`s e três `b`s, essa palavra não pode ser gerada pela gramática.

## Bloco 3 — Classificação

Classifique a gramática como **Regular** ou **Livre de Contexto**:

**S → aA**  
**A → b**

**Resposta:** Regular.
