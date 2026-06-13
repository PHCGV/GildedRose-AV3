# Evidencias de Execucao

## 1. Linha de base do legado original

Comando executado no repositório original:

```powershell
python python\texttest_fixture.py 2
```

Trecho relevante observado:

```text
-------- day 1 --------
Conjured Mana Cake, 2, 5

-------- day 2 --------
Conjured Mana Cake, 1, 4
```

Interpretacao:

- o legado estava tratando `Conjured Mana Cake` como item comum;
- a degradacao ocorria em `1` ponto por dia, em desacordo com o requisito.

## 2. Suite automatizada da solucao final

Comando executado:

```powershell
python -m pytest
```

Saida obtida:

```text
.............
13 passed in 0.19s
```

## 3. Execucao do fixture textual da solucao final

Comando executado:

```powershell
python src\texttest_fixture.py 2
```

Trecho relevante observado:

```text
-------- day 1 --------
Conjured Mana Cake, 2, 4

-------- day 2 --------
Conjured Mana Cake, 1, 2
```

Interpretacao:

- a regra de `Conjured` passou a degradar em dobro antes do vencimento;
- os demais itens mantiveram comportamento coerente com as regras do kata.

## 4. Cobertura de codigo do modulo fonte

Comandos executados:

```powershell
python -m coverage run --source=src --data-file=docs\coverage\src.coverage -m pytest
python -m coverage report --data-file=docs\coverage\src.coverage -m
```

Resumo obtido:

```text
Name                      Stmts   Miss  Cover
src\domain\inventory.py      20      0   100%
src\domain\policies.py       52      5    90%
src\domain\rules.py           8      0   100%
src\gilded_rose.py           14      0   100%
src\texttest_fixture.py      22      6    73%
TOTAL                       122     11    91%
```

## 5. Evidencia de abordagem TDD

- primeiro foram escritos os testes em `gilded-rose-modernizacao/tests/test_gilded_rose.py`;
- a execucao inicial falhou por ausencia do modulo `gilded_rose`;
- depois foi implementado o codigo minimo em `src/`;
- por fim, a suite ficou verde com `13` testes passando.
