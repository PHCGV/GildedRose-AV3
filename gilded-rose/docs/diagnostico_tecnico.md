# Diagnostico Tecnico do Legado

## Contexto

O codigo original analisado foi a variante Python do repositório `emilybache/GildedRose-Refactoring-Kata`, especialmente o arquivo `python/gilded_rose.py`.

## Principais problemas encontrados

### 1. Excesso de condicionais aninhadas

O metodo `update_quality()` do legado concentra toda a regra de negocio em uma estrutura extensa de `if/else`, como pode ser visto em `python/gilded_rose.py:8-36`.

Impactos:

- leitura dificil;
- alto custo para localizar regras de cada item;
- maior risco de regressao ao adicionar novo comportamento.

### 2. Responsabilidades misturadas

O mesmo metodo decide o tipo do item, altera `quality`, altera `sell_in`, trata expiracao e impõe excecoes para itens lendarios.

Impactos:

- baixa coesao;
- pouca reutilizacao;
- manutencao mais arriscada.

### 3. Forte acoplamento a strings literais

As categorias dos itens sao reconhecidas diretamente por comparacoes textuais repetidas, como `Aged Brie`, `Backstage passes...` e `Sulfuras...`.

Impactos:

- duplicacao de conhecimento;
- dificuldade para adicionar novas categorias como `Conjured`;
- maior chance de erro por digitacao.

### 4. Duplicaçao de regras

A degradacao de qualidade aparece em mais de um ponto do metodo, inclusive em blocos diferentes para antes e depois do vencimento.

Impactos:

- comportamento espalhado;
- dificuldade de evolucao;
- necessidade de validar varios trechos para uma mudanca simples.

### 5. Baixa testabilidade inicial

O projeto original traz:

- um teste placeholder em `python/tests/test_gilded_rose.py`;
- um teste por approval em `python/tests/test_gilded_rose_approvals.py`, dependente de configuracao adicional.

Na pratica, a suite inicial nao oferece protecao suficiente para refatoracao segura.

### 6. Nova regra ausente no legado

O fixture original ja lista `Conjured Mana Cake`, mas o codigo legado trata esse item como se fosse um item comum. Isso indica um gap explicito entre requisito e implementacao.

## Conclusao do diagnostico

O sistema original funciona para boa parte das regras basicas, mas sua estrutura dificulta manutencao, testes e extensao. A modernizacao precisou priorizar:

- isolamento das regras por tipo de item;
- centralizacao de invariantes de dominio;
- criacao de testes automatizados antes da refatoracao estrutural;
- implementacao especifica dos itens `Conjured`.
