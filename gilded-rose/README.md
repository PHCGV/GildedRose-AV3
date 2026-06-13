# Gilded Rose REfactory

Modernizacao do Gilded Rose em Python com base na Clean Architecture.

## Objetivo

- preservar o comportamento dos itens existentes;
- refatorar o codigo para melhorar legibilidade, coesao e testabilidade;
- implementar corretamente a regra dos itens `Conjured`;
- entregar evidencias tecnicas alinhadas ao barema.

## Regras de negocio principais

- Itens comuns perdem `1` ponto de qualidade por dia.
- Itens comuns vencidos perdem `2` pontos de qualidade por dia.
- `Aged Brie` aumenta de qualidade com o tempo.
- `Sulfuras` nao altera `sell_in` nem `quality`.
- `Backstage passes` aumentam de valor perto do show e vao para `0` apos o evento.
- Itens `Conjured` degradam duas vezes mais rapido que itens comuns.
- A qualidade minima e `0`.
- A qualidade maxima e `50`, exceto `Sulfuras`, que permanece em `80`.

## Estrutura

```text
gilded-rose/
|-- README.md
|-- requirements.txt
|-- pytest.ini
|-- src/
|   |-- gilded_rose.py
|   |-- texttest_fixture.py
|   |-- application/
|   |   `-- update_inventory.py
|   |-- domain/
|   |   |-- constants.py
|   |   |-- item_classifier.py
|   |   |-- item_rules.py
|   |   `-- quality_rules.py
|   |-- interface_adapters/
|   |   |-- controllers/
|   |   |   `-- inventory_controller.py
|   |   `-- presenters/
|   |       `-- report_presenter.py
|   `-- frameworks/
|       `-- texttest.py
|-- tests/
|   |-- conftest.py
|   |-- test_gilded_rose.py
|   `-- snapshots/
|       `-- expected_inventory_report_2_days.txt

```

## Arquitetura em camadas

- `domain`
  Contem as regras de negocio mais estaveis.
  Aqui ficam as constantes dos itens, a classificacao por tipo e as regras de atualizacao.

- `application`
  Contem o caso de uso principal do sistema.
  No projeto, isso aparece em `UpdateInventoryUseCase`, que coordena a atualizacao do estoque.

- `interface_adapters`
  Faz a ponte entre a entrada/saida e o caso de uso.
  Aqui ficam o controller que aciona o caso de uso e o presenter que formata o relatorio textual.

- `frameworks`
  Contem os drivers externos.
  Neste projeto, o principal driver e o fixture textual usado para simular varios dias do inventario.

- `gilded_rose.py`
  Mantem a interface tradicional do kata.
  Ele funciona como fachada compativel com o enunciado original.

## Fluxo da atualizacao

Quando `update_quality()` e chamado em `GildedRose`, o fluxo ocorre assim:

1. `src/gilded_rose.py`
   Recebe a chamada e delega para o controller.

2. `src/interface_adapters/inventory_controller.py`
   Encaminha a atualizacao para o caso de uso.
   Na estrutura atual, esse arquivo fica em `src/interface_adapters/controllers/inventory_controller.py`.

3. `src/application/update_inventory.py`
   Percorre os itens do estoque.

4. `src/domain/item_classifier.py`
   Decide qual regra usar para cada item.

5. `src/domain/item_rules.py`
   Aplica a regra correta ao item.

6. `src/domain/quality_rules.py`
   Garante os limites de qualidade quando necessario.

## Requisitos

- Python 3.13 ou compativel
- `pip`

## Instalacao das dependencias

```powershell
python -m pip install -r requirements.txt
```

## Como executar os testes

```powershell
python -m pytest
```

## Como executar o fixture textual

Exemplo para X dias:

```powershell
python src\texttest_fixture.py X
```

Esse comando imprime o estado do inventario no dia `0`, no dia `1` e no dia `2`.

## Resumo da solucao

- O contrato externo do kata foi mantido em `src/gilded_rose.py`, incluindo `Item`, `GildedRose.items` e `update_quality()`.
- A estrutura segue uma separacao explicita de `Clean Architecture`.
- A camada `domain` concentra regras de negocio e classificacao dos itens.
- A camada `application` coordena o caso de uso de atualizacao do inventario.
- A camada `interface_adapters` traduz a chamada do sistema para o caso de uso e formata a saida textual.
- A camada `frameworks` concentra o fixture textual usado como driver externo.
- A suite de testes cobre itens comuns, `Aged Brie`, `Sulfuras`, `Backstage passes`, `Conjured`, o caso de uso e o presenter.

## Testes do projeto

Os testes ficam em `tests/test_gilded_rose.py` e cobrem tres niveis:

- Regras de negocio
  Verificam item comum, `Aged Brie`, `Sulfuras`, `Backstage passes` e `Conjured`.

- Camadas da arquitetura
  Validam o caso de uso `UpdateInventoryUseCase` e o presenter textual.

- Comportamento integrado
  Comparam a saida textual completa do sistema com um snapshot esperado.

### O arquivo `tests/snapshots/expected_inventory_report_2_days.txt` guarda a saida esperada do inventario apos simular 2 dias.

Ele funciona como um gabarito textual:

- o teste chama `render_inventory_report(2)`;
- o resultado gerado e comparado com o conteudo desse arquivo;
- se qualquer linha mudar indevidamente, o teste falha.
