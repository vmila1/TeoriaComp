# Parser de Gramática Arbitrária

Este projeto consiste em um simulador de derivações para gramáticas formais, abrangendo toda a **Hierarquia de Chomsky** (desde gramáticas regulares até irrestritas). O script permite verificar se uma palavra pertence à linguagem  de uma gramática fornecida, exibindo o passo a passo da derivação.

---

## 1. Introdução Teórica

### 1.1 Linguagens Formais e Gramáticas

Uma gramática formal é um modelo matemático composto por:

* **Símbolos Terminais:** Elementos finais da cadeia (letras minúsculas/dígitos).
* **Símbolos Não-terminais (Variáveis):** Símbolos auxiliares (letras maiúsculas).
* **Símbolo Inicial (S):** O ponto de partida de todas as derivações.
* **Produções:** Regras de substituição que definem a estrutura da linguagem.

### 1.2 Parsing e o Problema de Pertencimento

O processo de determinar se uma palavra pertence a uma gramática é chamado de **parsing**. Enquanto gramáticas de Tipo 2 (Livres de Contexto) e Tipo 3 (Regulares) são decidíveis, gramáticas de Tipo 0 (Irrestritas) podem ser indecidíveis, o que exige limites técnicos de busca para garantir a finalização do programa.

---

## 2. Funcionamento

O algoritmo utiliza uma **Busca em Largura (BFS)** apoiada por uma estrutura de dados `deque`.

* **Estratégia:** O parser explora todas as possibilidades de substituição de strings nível por nível.
* **Prevenção de Loops:** Utiliza um conjunto de `visitados` para não processar strings repetidas.
* **Limites:** Impõe `max_passos` e `max_tamanho` para evitar o esgotamento de memória em gramáticas recursivas ou irrestritas.

---

## 3. Manual de Uso

### 2.1 Requisitos

* Python 3.8 ou superior.
* Bibliotecas nativas: `re`, `collections`.

### 2.2 Formato das Produções

As regras de produção devem seguir rigorosamente o padrão:
`LADO_ESQUERDO -> LADO_DIREITO: comentário opcional`

* **Símbolo Inicial:** Deve ser sempre `S`.
* **Palavra Vazia:** Representada por `ε` ou `λ`.
* **Exemplo:** `S -> aAB: Início`

### 2.3 Como executar

O script pode receber as gramáticas tanto como uma lista de strings quanto como um bloco de texto multilinhas:

```python
from parser_gramatica import ler_producoes, parser_gramatica

grammar = """
S -> aS
S -> b
"""
parser_gramatica(ler_producoes(grammar), "aaab")

```

---

## 4. Exemplos de Gramáticas

O parser foi validado com os seguintes cenários:

| Tipo | Descrição | Exemplo de Regra |
| --- | --- | --- |
| **FNC** | Forma Normal de Chomsky | `S -> L1C1` |
| **Tipo 1** | Sensível ao Contexto | `CB -> BC` |
| **Tipo 0** | Irrestrita | `bCd -> X` |

---

## 5. Relatório de IA

Em conformidade com as exigências da atividade:

* **Modelos Utilizados:** Gemini 2.0 Flash e ChatGPT.
* **Finalidade:** Refatoração do código inicial, remoção de redundâncias, implementação de lógica para gramáticas sensíveis ao contexto e estruturação desta documentação.
* **Ajustes Realizados:** Implementação de limites de segurança (`max_passos`) e normalização da entrada de texto.

---

**Autor:** Vithória Bastos
