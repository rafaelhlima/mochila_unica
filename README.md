# Problema da Mochila Única

**Importante:** Este repositório foi criado como material de apoio para a disciplina *Pesquisa Operacional 2A*, ministrada no curso de Engenharia de Produção da Universidade Tecnológica Federal do Paraná (UTFPR, Campus Londrina). O intuito das implementações aqui disponíveis é ensinar aos discentes a lógica de programação em Python na implementação de algoritmos usados em problemas de otimização.

Estão disponíveis 3 algoritmos para solucionar o problema da mochila única:
- **Algoritmo 1:** Inserir primeiro na mochila os itens de maior valor
- **Algoritmo 2:** Inserir primeiro na mochila os itens de menor peso
- **Algoritmo 3:** Inserir primeiro na mochila os itens de maior valor/peso

As implementações assumem que as instâncias são fornecidas em formato CSV seguindo o padrão definido na pasta `Instancias`. As soluções resultantes da aplicação dos algoritmos são salvas em arquivo CSV no formato definido na pasta `Solucoes`.

## Instruções de uso

Os algoritmos de resolução estão implementados em `solver_mochila.py`. A forma mais simples de rodar o algoritmo é usando o método `resolve_instancia`, como no exemplo abaixo:

```python
import solver_mochila as sm

sm.resolve_instancia("arq_instancia.csv", "arq_solucao.csv")
```

No exemplo anterior, os dados da instância `arq_instancia.csv` serão lidos e o Algoritmo 1 será executado. A solução obtida será salva no arquivo `arq_solucao.csv`. Note que por padrão, o Algoritmo 1 é sempre chamado.

Para chamar outros algoritmos, use a variável `ALGORITMO` definida em `solver_mochila.py`, a qual pode assumir os valores 1, 2 ou 3. Qualquer valor diferente desses fará com que o Algoritmo 1 seja chamado.

O exemplo a seguir resolve uma mesma instância aplicando os 3 algoritmos disponíveis:

```python
import solver_mochila as sm

arq_instancia = "Testes/inst_teste.csv"

sm.ALGORITMO = 1
sm.resolve_instancia(arq_instancia, "arq_solucao1.csv")

sm.ALGORITMO = 2
sm.resolve_instancia(arq_instancia, "arq_solucao2.csv")

sm.ALGORITMO = 3
sm.resolve_instancia(arq_instancia, "arq_solucao3.csv")
```

## Geração de instâncias aleatórias

É possível gerar instâncias de teste aleatórias usando o método `gera_instancia` disponível em `gera_instancias.py`. Para isso, basta informar a quantidade de itens a serem incluídos na instância.

O exemplo a seguir gera uma instância com 50 itens e salva os dados gerados no arquivo `instancia_exemplo.csv`:

```python
from gera_instancias import gera_instancia

gera_instancia(50, "instancia_exemplo.csv")
```

As instâncias geradas com este método sempre estarão no formato esperado pelos algoritmos implementados em `solver_mochila.py`.
