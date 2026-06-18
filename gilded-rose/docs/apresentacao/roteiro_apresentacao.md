# Roteiro de Apresentação

## 1. Problema

- O sistema legado atualiza a qualidade do estoque diariamente.
- O comportamento principal funciona, mas o código original tem baixa manutenibilidade.
- A nova demanda era implementar corretamente os itens `Conjured`.

## 2. Diagnóstico

- Método único com muitas condicionais.
- Regras espalhadas e duplicadas.
- Poucos testes úteis no ponto de partida.
- Alto risco de regressão ao evoluir o legado.

## 3. Estratégia adotada

- Captura do comportamento inicial do legado.
- Escrita de testes automatizados com `pytest`.
- Refatoração incremental para uma arquitetura inspirada em Clean Architecture.
- Implementação isolada das regras por tipo de item.

## 4. Melhorias realizadas

- `GildedRose.update_quality()` virou uma fachada simples.
- As regras foram separadas em `domain`, `application`, `interface_adapters` e `frameworks`.
- Os adaptadores foram organizados em `controllers` e `presenters`.
- O contrato externo do kata foi preservado.

## 5. Resultados

- `15` testes automatizados passando.
- Snapshot textual cobrindo o fluxo completo.
- `Conjured` implementado com degradação dobrada, conforme o requisito.
- Projeto mais legível e preparado para crescimento.

## 6. Aprendizados

- Refatorar legado sem testes aumenta muito o risco.
- Testes de caracterização ajudam a preservar comportamento.
- Separação de responsabilidades reduz o custo de evolução.
- Documentação e evidências contam tanto quanto o código final.
