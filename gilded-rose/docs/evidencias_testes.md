# Evidências de Execução

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

Interpretação:

- o legado estava tratando `Conjured Mana Cake` como item comum;
- a degradação ocorria em `1` ponto por dia, em desacordo com o requisito.

## 2. Suíte automatizada da solução final

Comando executado:

```powershell
python -m pytest
```

Resultado mais recente:

```text
15 passed
```

## 3. Execução do fixture textual da solução final

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

Interpretação:

- a regra de `Conjured` passou a degradar em dobro antes do vencimento;
- os demais itens mantiveram comportamento coerente com as regras do kata.

## 4. Evidência de abordagem TDD

- primeiro foram escritos os testes do comportamento esperado;
- a execução inicial falhou por ausência de módulos da nova estrutura;
- depois foi implementado o código mínimo para a nova arquitetura;
- por fim, a suíte ficou verde com todos os testes passando.

## 5. Observação sobre cobertura

O projeto chegou a gerar evidências de cobertura durante a validação, mas os arquivos brutos de cobertura foram removidos da entrega final para manter o repositório mais enxuto.
