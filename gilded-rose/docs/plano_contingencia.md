# Plano de Contingência e Refatoração

## Estratégia adotada

1. Capturar o comportamento inicial do legado por meio do fixture textual.
2. Escrever testes automatizados cobrindo as regras de negócio esperadas.
3. Criar uma nova base de trabalho isolada para a solução final.
4. Manter o contrato externo do kata e mover a lógica para componentes menores.
5. Implementar `Conjured` somente após estabilizar a malha principal de testes.
6. Validar a solução com `pytest` e fixture textual.

## Partes que podem ser alteradas

- `src/gilded_rose.py`
- `src/texttest_fixture.py`
- `src/application/*`
- `src/domain/*`
- `src/interface_adapters/*`
- `src/frameworks/*`
- `tests/*`
- `README.md`
- `docs/*`

## Partes que não podem ser alteradas

- a interface da classe `Item`;
- a propriedade `items` da classe `GildedRose`;
- o método público `update_quality()` como contrato de uso.

## Riscos identificados

### Risco 1. Quebrar comportamento legado

Ação preventiva:

- criar testes para cada tipo de item;
- validar um snapshot textual do fluxo completo.

### Risco 2. Implementar `Conjured` com degradação incorreta

Ação preventiva:

- cobrir explicitamente cenários antes e depois do vencimento;
- testar limite inferior de qualidade.

### Risco 3. Alterar estruturas proibidas pelo enunciado

Ação preventiva:

- preservar `Item` sem modificações;
- manter `items` e `update_quality()` como fachada pública.

### Risco 4. Introduzir arquitetura excessiva para um kata pequeno

Ação preventiva:

- usar `Clean` leve;
- separar apenas o necessário: regras de domínio, caso de uso, adaptadores e driver textual.

### Risco 5. Dependência de ambiente Windows

Ação preventiva:

- documentar comandos simples;
- evitar dependências de configuração externa para executar os testes.

## Ordem segura de execução

1. Preparar dependências.
2. Registrar linha de base do legado.
3. Escrever testes.
4. Executar testes em vermelho.
5. Implementar o mínimo para verde.
6. Refatorar internamente mantendo a suíte verde.
7. Gerar evidências finais.

## Critérios de validação

- todos os testes automatizados devem passar;
- `Conjured` deve degradar em dobro e respeitar limites;
- `Sulfuras` deve permanecer imutável;
- o fixture textual deve produzir a saída esperada;
- a arquitetura deve permanecer coerente com a separação em camadas adotada.
