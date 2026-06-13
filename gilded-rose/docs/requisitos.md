# Documento de Requisitos

## Requisitos Funcionais

- `RF01` O sistema deve atualizar diariamente o `sell_in` e a `quality` de todos os itens do estoque.
- `RF02` Itens comuns devem perder `1` ponto de qualidade por dia antes da data de venda.
- `RF03` Itens comuns devem perder `2` pontos de qualidade por dia apos a data de venda.
- `RF04` A qualidade de qualquer item comum nao pode ser negativa.
- `RF05` O item `Aged Brie` deve aumentar `1` ponto de qualidade por dia antes da data de venda.
- `RF06` O item `Aged Brie` deve aumentar `2` pontos de qualidade por dia apos a data de venda.
- `RF07` A qualidade do `Aged Brie` nao pode ultrapassar `50`.
- `RF08` O item `Sulfuras, Hand of Ragnaros` deve manter `quality = 80` e nao deve alterar `sell_in`.
- `RF09` `Backstage passes to a TAFKAL80ETC concert` deve aumentar `1` ponto de qualidade quando `sell_in > 10`.
- `RF10` `Backstage passes to a TAFKAL80ETC concert` deve aumentar `2` pontos de qualidade quando `sell_in <= 10`.
- `RF11` `Backstage passes to a TAFKAL80ETC concert` deve aumentar `3` pontos de qualidade quando `sell_in <= 5`.
- `RF12` `Backstage passes to a TAFKAL80ETC concert` deve ter qualidade `0` apos a data do show.
- `RF13` A qualidade de qualquer item nao lendario nao pode ultrapassar `50`.
- `RF14` Itens com prefixo `Conjured` devem perder `2` pontos de qualidade por dia antes da data de venda.
- `RF15` Itens com prefixo `Conjured` devem perder `4` pontos de qualidade por dia apos a data de venda.
- `RF16` Itens `Conjured` tambem devem respeitar o limite inferior de qualidade `0`.
- `RF17` O sistema deve manter o metodo publico `update_quality()` como ponto principal de atualizacao.

## Requisitos Nao Funcionais

- `RNF01` A classe `Item` nao pode ser alterada.
- `RNF02` A propriedade `items` da classe `GildedRose` deve ser preservada.
- `RNF03` O comportamento legado dos itens ja existentes deve ser preservado.
- `RNF04` A solucao deve adotar uma arquitetura `Clean` leve ou equivalente, com separacao clara de responsabilidades.
- `RNF05` O codigo deve ser legivel, modular e de facil manutencao.
- `RNF06` A suite de testes deve ser automatizada com `pytest`.
- `RNF07` Os testes devem cobrir itens comuns, `Aged Brie`, `Sulfuras`, `Backstage passes`, `Conjured` e casos de borda.
- `RNF08` A entrega deve incluir documentacao tecnica, evidencias de execucao e orientacoes reproduziveis no `README`.
- `RNF09` A refatoracao deve ser incremental e guiada por testes, reduzindo risco de regressao.
