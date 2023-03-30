import solver_mochila as sm
from gera_instancias import gera_instancia

def exemplo_solver():
    sm.ALGORITMO = 1
    arq_instancia = "Testes/inst_teste.csv"
    sm.resolve_instancia(arq_instancia, "arq_solucao1.csv")
    sm.ALGORITMO = 2
    sm.resolve_instancia(arq_instancia, "arq_solucao2.csv")
    sm.ALGORITMO = 3
    sm.resolve_instancia(arq_instancia, "arq_solucao3.csv")

def exemplo_geracao_instancia():
    gera_instancia(50, "instancia_exemplo.csv")

if __name__ == "__main__":
    # Escolher alguma das opções abaixo para rodar
    exemplo_solver()
    # exemplo_geracao_instancia()
