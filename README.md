# Problema da Mochila Única

Este projeto implementa 3 algoritmos para solucionar o problema da mochila:
- **Algoritmo 1:** Inserir primeiro na mochila os itens de maior valor
- **Algoritmo 2:** Inserir primeiro na mochila os itens de menor peso
- **Algoritmo 3:** Inserir primeiro na mochila os itens de maior valor/peso

As implementações assumem que as instâncias são fornecidas em formato CSV seguindo o padrão definido na pasta `Instancias`. As soluções resultantes da aplicação dos algoritmos são salvas em arquivo CSV no formato definido na pasta `Solucoes`.

## Instruções de uso

Os algoritmos de resolução estão implementados em `solver.py`. A forma mais simples de rodar o algoritmo é usando o método `resolve_instancia`, como no exemplo abaixo:

```python
import solver

solver.resolve_instancia("arq_instancia.csv", "arq_solucao.csv")
```

No exemplo anterior, os dados da instância `arq_instancia.csv` serão lidos e o Algoritmo 1 será executado. A solução obtida será salva no arquivo `arq_solucao.csv`. Note que por padrão, o Algoritmo 1 é sempre chamado.

Para chamar outros algoritmos, use a variável `ALGORITMO` definida em `solver.py`, a qual pode assumir os valores 1, 2 ou 3. Qualquer valor diferente desses fará com que o Algoritmo 1 seja chamado.

O exemplo a seguir resolve uma mesma instância aplicando os 3 algoritmos:

```python
import solver

solver.ALGORITMO = 1
arq_instancia = "Testes/inst_teste.csv"
solver.resolve_instancia(arq_instancia, "arq_solucao1.csv")
solver.ALGORITMO = 2
solver.resolve_instancia(arq_instancia, "arq_solucao2.csv")
solver.ALGORITMO = 3
solver.resolve_instancia(arq_instancia, "arq_solucao3.csv")
```
