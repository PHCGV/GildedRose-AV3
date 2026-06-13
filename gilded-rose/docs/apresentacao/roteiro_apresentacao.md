# Roteiro de Apresentacao

## 1. Problema

- O sistema legado atualiza a qualidade do estoque diariamente.
- O comportamento principal funciona, mas o codigo original tem baixa manutenibilidade.
- A nova demanda era implementar corretamente os itens `Conjured`.

## 2. Diagnostico

- Metodo unico com muitas condicionais.
- Regras espalhadas e duplicadas.
- Poucos testes uteis no ponto de partida.
- Alto risco de regressao ao evoluir o legado.

## 3. Estrategia adotada

- Captura do comportamento inicial do legado.
- Escrita de testes automatizados com `pytest`.
- Refatoracao incremental para uma arquitetura `Clean` leve.
- Implementacao isolada das politicas por tipo de item.

## 4. Melhorias realizadas

- `GildedRose.update_quality()` virou uma fachada simples.
- Regras foram separadas em politicas para item comum, `Aged Brie`, `Backstage passes`, `Sulfuras` e `Conjured`.
- Limites de qualidade foram centralizados.
- O contrato externo do kata foi preservado.

## 5. Resultados

- `13` testes automatizados passando.
- Snapshot textual cobrindo o fluxo completo.
- Cobertura de `91%` sobre `src`.
- `Conjured` implementado com degradacao dobrada, conforme o requisito.

## 6. Aprendizados

- Refatorar legado sem testes aumenta muito o risco.
- Testes de caracterizacao ajudam a preservar comportamento.
- Separacao de responsabilidades reduz o custo de evolucao.
- Documentacao e evidencias contam tanto quanto o codigo final.
