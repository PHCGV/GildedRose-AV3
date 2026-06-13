# Plano de Contingencia e Refatoracao

## Estrategia adotada

1. Capturar o comportamento inicial do legado por meio do fixture textual.
2. Escrever testes automatizados cobrindo as regras de negocio esperadas.
3. Criar uma nova base de trabalho isolada em `gilded-rose-modernizacao/`.
4. Manter o contrato externo do kata e mover a logica para componentes menores.
5. Implementar `Conjured` somente apos estabilizar a malha principal de testes.
6. Validar a solucao com `pytest`, fixture textual e cobertura de codigo.

## Partes que podem ser alteradas

- `src/gilded_rose.py`
- `src/texttest_fixture.py`
- `src/domain/*`
- `tests/*`
- `README.md`
- `docs/*`

## Partes que nao podem ser alteradas

- a interface da classe `Item`;
- a propriedade `items` da classe `GildedRose`;
- o metodo publico `update_quality()` como contrato de uso.

## Riscos identificados

### Risco 1. Quebrar comportamento legado

Acao preventiva:

- criar testes para cada tipo de item;
- validar um snapshot textual do fluxo completo.

### Risco 2. Implementar `Conjured` com degradacao incorreta

Acao preventiva:

- cobrir explicitamente cenarios antes e depois do vencimento;
- testar limite inferior de qualidade.

### Risco 3. Alterar estruturas proibidas pelo enunciado

Acao preventiva:

- preservar `Item` sem modificacoes;
- manter `items` e `update_quality()` como fachada publica.

### Risco 4. Introduzir arquitetura excessiva para um kata pequeno

Acao preventiva:

- usar `Clean` leve;
- separar apenas o necessario: selecao de politica, regras comuns e politicas de atualizacao.

### Risco 5. Dependencia de ambiente Windows

Acao preventiva:

- documentar comandos simples;
- desabilitar cache do `pytest` via `pytest.ini` para evitar problemas de permissao observados neste ambiente.

## Ordem segura de execucao

1. Preparar dependencias.
2. Registrar linha de base do legado.
3. Escrever testes.
4. Executar testes em vermelho.
5. Implementar o minimo para verde.
6. Refatorar internamente mantendo a suite verde.
7. Gerar evidencias finais.

## Criterios de validacao

- todos os testes automatizados devem passar;
- `Conjured` deve degradar em dobro e respeitar limites;
- `Sulfuras` deve permanecer imutavel;
- o fixture textual deve produzir a saida esperada;
- a cobertura do codigo fonte deve ser suficiente para sustentar a confianca na refatoracao.
