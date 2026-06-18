# Gilded Rose REfactory

Modernização do Gilded Rose em Python com base na Clean Architecture.

## Objetivo

- preservar o comportamento dos itens existentes;
- refatorar o código para melhorar legibilidade, coesão e testabilidade;
- implementar corretamente a regra dos itens `Conjured`;
- entregar evidências técnicas alinhadas ao barema.

## Regras de negócio principais

- Itens comuns perdem `1` ponto de qualidade por dia.
- Itens comuns vencidos perdem `2` pontos de qualidade por dia.
- `Aged Brie` aumenta de qualidade com o tempo.
- `Sulfuras` não altera `sell_in` nem `quality`.
- `Backstage passes` aumentam de valor perto do show e vão para `0` após o evento.
- Itens `Conjured` degradam duas vezes mais rápido que itens comuns.
- A qualidade mínima é `0`.
- A qualidade máxima é `50`, exceto `Sulfuras`, que permanece em `80`.

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
`-- docs/
    |-- diagnostico_tecnico.md
    |-- requisitos.md
    |-- plano_contingencia.md
    |-- evidencias_testes.md
    `-- apresentacao/
        `-- roteiro_apresentacao.md
```

## Arquitetura em camadas

- `domain`
  Contém as regras de negócio mais estáveis. Aqui ficam as constantes dos itens, a classificação por tipo e as regras de atualização.

- `application`
  Contém o caso de uso principal do sistema. No projeto, isso aparece em `UpdateInventoryUseCase`, que coordena a atualização do estoque.

- `interface_adapters`
  Faz a ponte entre a entrada/saída e o caso de uso. A estrutura foi subdividida em `controllers` e `presenters` para facilitar o crescimento do projeto.

- `frameworks`
  Contém os drivers externos. Neste projeto, o principal driver é o fixture textual usado para simular vários dias do inventário.

- `gilded_rose.py`
  Mantém a interface tradicional do kata. Ele funciona como fachada compatível com o enunciado original.

## Fluxo da atualização

Quando `update_quality()` é chamado em `GildedRose`, o fluxo ocorre assim:

1. `src/gilded_rose.py`
   Recebe a chamada e delega para o controller.

2. `src/interface_adapters/controllers/inventory_controller.py`
   Encaminha a atualização para o caso de uso.

3. `src/application/update_inventory.py`
   Percorre os itens do estoque.

4. `src/domain/item_classifier.py`
   Decide qual regra usar para cada item.

5. `src/domain/item_rules.py`
   Aplica a regra correta ao item.

6. `src/domain/quality_rules.py`
   Garante os limites de qualidade quando necessário.

## Requisitos

- Python 3.13 ou compatível
- `pip`

## Instalação das dependências

```powershell
python -m pip install -r requirements.txt
```

## Como executar os testes

```powershell
python -m pytest
```

## Como executar o fixture textual

Exemplo para 2 dias:

```powershell
python src\texttest_fixture.py 2
```

Esse comando imprime o estado do inventário no dia `0`, no dia `1` e no dia `2`.

## Resumo da solução

- O contrato externo do kata foi mantido em `src/gilded_rose.py`, incluindo `Item`, `GildedRose.items` e `update_quality()`.
- A estrutura segue uma separação explícita de `Clean Architecture`.
- A camada `domain` concentra regras de negócio e classificação dos itens.
- A camada `application` coordena o caso de uso de atualização do inventário.
- A camada `interface_adapters` traduz a chamada do sistema para o caso de uso e formata a saída textual.
- A camada `frameworks` concentra o fixture textual usado como driver externo.
- A suíte de testes cobre itens comuns, `Aged Brie`, `Sulfuras`, `Backstage passes`, `Conjured`, o caso de uso e o presenter.

## Testes do projeto

Os testes ficam em `tests/test_gilded_rose.py` e cobrem três níveis:

- Regras de negócio
  Verificam item comum, `Aged Brie`, `Sulfuras`, `Backstage passes` e `Conjured`.

- Camadas da arquitetura
  Validam o caso de uso `UpdateInventoryUseCase` e o presenter textual.

- Comportamento integrado
  Comparam a saída textual completa do sistema com um snapshot esperado.

### O arquivo `tests/snapshots/expected_inventory_report_2_days.txt`

Esse arquivo guarda a saída esperada do inventário após simular 2 dias.

Ele funciona como um gabarito textual:

- o teste chama `render_inventory_report(2)`;
- o resultado gerado é comparado com o conteúdo desse arquivo;
- se qualquer linha mudar indevidamente, o teste falha.

Isso ajuda a detectar regressão de comportamento no sistema como um todo, e não apenas em itens isolados.

## Principais decisões de refatoração

- evitar reescrita total do legado;
- introduzir uma arquitetura `Clean` mais explícita, sem perder a simplicidade do kata;
- manter `gilded_rose.py` e `texttest_fixture.py` como fachadas compatíveis;
- criar testes antes da nova separação em camadas;
- usar evidências objetivas de execução em vez de depender apenas de descrição textual.

## Documentação de apoio

- `docs/diagnostico_tecnico.md`
  Apresenta os problemas encontrados no legado original.

- `docs/requisitos.md`
  Organiza os requisitos funcionais e não funcionais.

- `docs/plano_contingencia.md`
  Registra os riscos e a estratégia de refatoração segura.

- `docs/evidencias_testes.md`
  Resume os comandos executados e os resultados obtidos.

- `docs/apresentacao/roteiro_apresentacao.md`
  Traz um roteiro curto para defesa do trabalho.
